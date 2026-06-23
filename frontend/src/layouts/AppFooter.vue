<script setup>
const year = new Date().getFullYear()
</script>

<template>
	<footer class="footer">
		<div class="footer-inner">
			<nav class="footer-links">
				<RouterLink :to="{ name: 'terms' }">이용약관</RouterLink>
				<RouterLink :to="{ name: 'privacy' }">개인정보처리방침</RouterLink>
				<RouterLink :to="{ name: 'credits' }">저작권·자료출처</RouterLink>
				<RouterLink :to="{ name: 'disclaimer' }">투자 위험 고지</RouterLink>
			</nav>
			<p class="footer-disclaimer">
				본 서비스가 제공하는 정보는 투자 참고용이며, 투자 판단과 그 결과의 책임은 이용자 본인에게 있습니다.
			</p>
			<p class="footer-copy">© {{ year }} 주고파(Jugopa). All rights reserved.</p>
		</div>
	</footer>
</template>

<style scoped>
.footer {
	background: var(--bg-surface);
	border-top: 1px solid var(--border-subtle);
	padding: var(--space-5) var(--space-4);
}
.footer-inner {
	max-width: var(--content-max);
	margin: 0 auto;
	text-align: center;
}
.footer-links {
	display: flex;
	flex-wrap: wrap;
	justify-content: center;
	gap: var(--space-2) var(--space-4);
	margin-bottom: var(--space-3);
}
.footer-links a {
	color: var(--text-secondary);
	font-size: 13px;
	font-weight: 600;
}
.footer-links a:hover {
	color: var(--accent);
}
.footer-disclaimer {
	color: var(--text-tertiary);
	font-size: 12px;
	line-height: 1.7;
	margin-bottom: var(--space-2);
}
.footer-copy {
	color: var(--text-tertiary);
	font-size: 12px;
}
/* 모바일: 하단 고정 탭바에 가려지지 않도록 여백 확보 */
@media (max-width: 767px) {
	.footer {
		padding-bottom: calc(var(--space-5) + var(--bottom-tab-height) + env(safe-area-inset-bottom, 0px));
	}
}
</style>
