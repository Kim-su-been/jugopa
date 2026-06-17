"""코스피·코스닥 등락률로 '투자 날씨'를 산출한다.

상승일수록 긍정(맑음), 하락일수록 부정(폭풍). 임계값은 아래 상수로 조정 가능.
"""

from django.utils import timezone

from .models import MarketIndexDaily, DailyMarketWeather

# combined(코스피·코스닥 평균 등락률, %) 구간별 (상태, 메시지).
# 큰 값(상승)부터 검사한다.
WEATHER_THRESHOLDS = [
	(1.5, DailyMarketWeather.WeatherStatus.SUNNY, "강세 마감 — 투자 심리가 좋은 날입니다."),
	(0.5, DailyMarketWeather.WeatherStatus.CLOUDY, "완만한 상승 흐름입니다."),
	(-0.5, DailyMarketWeather.WeatherStatus.RAINY, "약보합 — 관망세가 짙습니다."),
	(-1.5, DailyMarketWeather.WeatherStatus.SNOWY, "약세 — 변동성에 주의하세요."),
]
# 위 어느 구간에도 못 미치면(최저) STORMY.
WEATHER_FALLBACK = (DailyMarketWeather.WeatherStatus.STORMY, "큰 하락 — 변동성 경계가 필요합니다.")


def compute_weather(kospi_rate, kosdaq_rate):
	"""코스피·코스닥 등락률(%)로 (status, message, indicator_data)를 산출한다."""
	combined = (kospi_rate + kosdaq_rate) / 2

	status, message = WEATHER_FALLBACK
	for lower_bound, bound_status, bound_message in WEATHER_THRESHOLDS:
		if combined >= lower_bound:
			status, message = bound_status, bound_message
			break

	indicator_data = {
		"combined_rate": round(combined, 2),
		"kospi": {"change_rate": kospi_rate},
		"kosdaq": {"change_rate": kosdaq_rate},
	}
	return status, message, indicator_data


def store_today_weather():
	"""최신 코스피·코스닥 지수를 읽어 오늘자 DailyMarketWeather를 산출·저장한다.

	반환: 저장된 DailyMarketWeather 인스턴스. 지수 데이터가 없으면 None.
	"""
	kospi = MarketIndexDaily.objects.filter(index_name="코스피").first()
	kosdaq = MarketIndexDaily.objects.filter(index_name="코스닥").first()
	if not kospi or not kosdaq:
		return None

	status, message, indicator_data = compute_weather(kospi.change_rate, kosdaq.change_rate)
	indicator_data["kospi"]["close_price"] = kospi.close_price
	indicator_data["kosdaq"]["close_price"] = kosdaq.close_price

	obj, _ = DailyMarketWeather.objects.update_or_create(
		target_date=timezone.localdate(),
		defaults={
			"weather_status": status,
			"message": message,
			"indicator_data": indicator_data,
		},
	)
	return obj
