"""data.go.kr 금융위원회 지수시세정보 API로 코스피·코스닥 지수를 수집한다.

stocks/views.py:save_stocks의 requests/parse 패턴을 따른다.
※ 주식시세정보(getStockPriceInfo)와 별개 API이므로, 공공데이터포털에서
   '지수시세정보(GetMarketIndexInfoService)' 활용신청이 되어 있어야 호출된다.
"""

import requests
from datetime import datetime

from django.conf import settings

from .models import MarketIndexDaily

API_URL = "https://apis.data.go.kr/1160100/service/GetMarketIndexInfoService/getStockMarketIndex"

# 수집 대상 지수명(idxNm). 한국 시장 기준이므로 코스피·코스닥만.
TARGET_INDICES = ("코스피", "코스닥")


def _parse_float(value):
	"""문자열 숫자를 float로 변환. 빈 값/오류는 None."""
	if value is None or value == "":
		return None
	try:
		return float(str(value).replace(",", ""))
	except ValueError:
		return None


def collect_indices():
	"""코스피·코스닥의 최신 지수를 수집해 MarketIndexDaily에 upsert한다.

	반환: 저장/갱신된 MarketIndexDaily 인스턴스 리스트.
	"""
	api_key = settings.FINANCIAL_API_KEY
	saved = []

	for index_name in TARGET_INDICES:
		params = {
			"serviceKey": api_key,
			"resultType": "json",
			"numOfRows": 1,
			"pageNo": 1,
			"idxNm": index_name,
		}
		response = requests.get(API_URL, params=params)
		data = response.json()
		items = data.get("response", {}).get("body", {}).get("items", {}).get("item", [])
		if isinstance(items, dict):       # 단건이면 dict로 올 수 있음
			items = [items]
		if not items:
			continue

		item = items[0]
		bas_dt = item.get("basDt")
		close_price = _parse_float(item.get("clpr"))
		if not bas_dt or close_price is None:
			continue

		try:
			base_date = datetime.strptime(bas_dt, "%Y%m%d").date()
		except ValueError:
			continue

		obj, _ = MarketIndexDaily.objects.update_or_create(
			index_name=index_name,
			base_date=base_date,
			defaults={
				"close_price": close_price,
				"change": _parse_float(item.get("vs")) or 0.0,
				"change_rate": _parse_float(item.get("fltRt")) or 0.0,
			},
		)
		saved.append(obj)

	return saved
