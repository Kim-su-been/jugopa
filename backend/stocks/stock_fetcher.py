"""종목명으로 data.go.kr 주식시세정보 API를 조회해 Stock·시세를 적재한다.

섹터별 대표 종목을 동적으로 확보하기 위해 사용한다(load_sector_stocks).
save_stocks 뷰와 동일한 getStockPriceInfo API를 쓰되, likeItmsNm(종목명 검색)으로 호출한다.
"""

import requests
from datetime import datetime

from django.conf import settings

from .models import Stock, StockPriceDaily

API_URL = "https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo"


def _parse_int(value):
	if value is None or value == "":
		return -1
	try:
		return int(value)
	except ValueError:
		return -1


def fetch_stock_by_name(name):
	"""종목명으로 최신 시세를 조회해 Stock + StockPriceDaily를 upsert하고 Stock을 반환한다.

	정확히 일치하는 종목명을 우선하고, 최신 기준일(basDt) 행을 사용한다.
	조회 실패 시 None.
	"""
	params = {
		"serviceKey": settings.FINANCIAL_API_KEY,
		"resultType": "json",
		"numOfRows": 10,
		"pageNo": 1,
		"likeItmsNm": name,
	}
	try:
		response = requests.get(API_URL, params=params, timeout=30)
		data = response.json()
	except Exception:
		return None

	items = data.get("response", {}).get("body", {}).get("items", {}).get("item", [])
	if isinstance(items, dict):
		items = [items]
	if not items:
		return None

	# 정확히 일치하는 종목명 우선, 없으면 전체 후보. 그중 최신 기준일 선택.
	exact = [it for it in items if it.get("itmsNm") == name]
	candidates = exact or items
	item = max(candidates, key=lambda it: it.get("basDt", ""))

	stock_code = item.get("srtnCd")
	if not stock_code:
		return None

	stock, _ = Stock.objects.get_or_create(
		stock_code=stock_code,
		defaults={"stock_name": item.get("itmsNm", name), "market_type": item.get("mrktCtg", "")},
	)

	bas_dt = item.get("basDt")
	if bas_dt:
		try:
			record_date = datetime.strptime(bas_dt, "%Y%m%d").date()
			StockPriceDaily.objects.update_or_create(
				stock=stock,
				record_date=record_date,
				defaults={
					"open_price": _parse_int(item.get("mkp")),
					"close_price": _parse_int(item.get("clpr")),
					"high_price": _parse_int(item.get("hipr")),
					"low_price": _parse_int(item.get("lopr")),
					"volume": _parse_int(item.get("trqu")),
				},
			)
		except ValueError:
			pass

	return stock
