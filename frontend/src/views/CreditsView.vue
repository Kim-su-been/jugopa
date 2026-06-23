<script setup>
import LegalPage from '@/components/LegalPage.vue'
</script>

<template>
	<LegalPage eyebrow="저작권 · 자료 출처" title="저작권 및 자료 출처" updated="2026년 6월 23일">
		<p>
			주고파는 다양한 공공데이터·언론사·오픈소스·AI 모델을 활용하여 정보를 가공·제공합니다. 각 자료의 저작권은
			원 제공처에 있으며, 본 서비스는 이를 학습·정보 제공 목적으로 가공하여 표시합니다.
		</p>

		<h2>1. 주식 · 지수 시세 데이터</h2>
		<table>
			<thead>
				<tr><th>데이터</th><th>출처</th></tr>
			</thead>
			<tbody>
				<tr><td>코스피·코스닥·코스피200·KRX300 지수 시세</td><td>공공데이터포털 — 금융위원회 지수시세정보</td></tr>
				<tr><td>개별 종목 시세(종가·시가·고가·저가·거래량·시가총액)</td><td>공공데이터포털 — 금융위원회 주식시세정보</td></tr>
				<tr><td>상장종목 유니버스(KOSPI/KOSDAQ)</td><td>FinanceDataReader (오픈소스)</td></tr>
			</tbody>
		</table>
		<p>공공데이터 출처: <a href="https://www.data.go.kr" target="_blank" rel="noopener">https://www.data.go.kr</a></p>

		<h2>2. 업종 분류</h2>
		<p>
			업종(섹터) 분류 정보는 네이버 금융의 업종분류 페이지를 기반으로 매핑하여 제공합니다. 해당 분류 데이터의
			저작권은 네이버(주)에 있습니다.
		</p>

		<h2>3. 뉴스 데이터</h2>
		<p>경제 뉴스는 각 언론사가 제공하는 RSS 피드를 통해 수집하며, 원 기사의 저작권은 각 언론사에 귀속됩니다.</p>
		<ul>
			<li>연합뉴스 경제</li>
			<li>매일경제</li>
			<li>SBS Biz</li>
		</ul>
		<p>본 서비스는 기사 원문을 복제·재배포하지 않으며, 요약·카드뉴스 형태로 가공하여 출처와 함께 제공합니다.</p>

		<h2>4. AI · 머신러닝 모델</h2>
		<table>
			<thead>
				<tr><th>용도</th><th>모델 · 제공처</th></tr>
			</thead>
			<tbody>
				<tr><td>뉴스 감성 분석</td><td>snunlp/KR-FinBert-SC (HuggingFace)</td></tr>
				<tr><td>경제용어 퀴즈 생성</td><td>Claude (Anthropic)</td></tr>
				<tr><td>AI 챗봇 · 뉴스 카드 요약</td><td>GMS (OpenAI 호환 API)</td></tr>
			</tbody>
		</table>

		<h2>5. 주요 오픈소스 라이브러리</h2>
		<p>본 서비스는 다음을 포함한 오픈소스 소프트웨어를 사용하며, 각 라이선스를 준수합니다.</p>
		<ul>
			<li>Django, Django REST Framework</li>
			<li>Vue 3, Vite</li>
			<li>transformers, PyTorch</li>
			<li>FinanceDataReader, feedparser, BeautifulSoup</li>
		</ul>

		<h2>6. 저작권 문의</h2>
		<p>자료 출처 표기 누락이나 저작권 관련 문의가 있으실 경우 아래로 연락해 주시면 신속히 확인하여 조치하겠습니다.</p>
		<ul>
			<li>정시영 — <a href="mailto:jsy002514@naver.com">jsy002514@naver.com</a></li>
			<li>정다운 — <a href="mailto:dawon1711@naver.com">dawon1711@naver.com</a></li>
			<li>김수빈 — <a href="mailto:kisu1012hka@gmail.com">kisu1012hka@gmail.com</a></li>
		</ul>
	</LegalPage>
</template>
