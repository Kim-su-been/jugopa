<script setup>
// 법적 고지 페이지(이용약관/개인정보/저작권/투자위험) 공통 레이아웃.
// 본문은 슬롯으로 전달하며, 슬롯 콘텐츠 스타일은 :slotted()로 적용한다.
defineProps({
	eyebrow: { type: String, required: true },
	title: { type: String, required: true },
	updated: { type: String, default: '' },
})
</script>

<template>
	<div class="page legal theme-light">
		<RouterLink :to="{ name: 'home' }" class="nav-arrow right" aria-label="메인 페이지">›</RouterLink>
		<span class="eyebrow">{{ eyebrow }}</span>
		<h1 class="legal-title">{{ title }}</h1>
		<p v-if="updated" class="legal-updated">시행일 {{ updated }}</p>
		<article class="legal-content card">
			<slot />
		</article>
		<RouterLink :to="{ name: 'home' }" class="legal-home">← 홈으로 돌아가기</RouterLink>
	</div>
</template>

<style scoped>
.page.legal {
	min-height: 100vh;
	background: var(--bg-base);
}
.eyebrow {
	display: inline-block;
	padding: 6px 12px;
	border-radius: var(--radius-pill);
	background: var(--accent);
	color: #ffffff;
	font-size: 12px;
	font-weight: 700;
	margin-bottom: var(--space-4);
}
.legal-title {
	font-size: 28px;
	font-weight: 800;
	margin-bottom: var(--space-2);
}
.legal-updated {
	color: var(--text-tertiary);
	font-size: 13px;
	margin-bottom: var(--space-5);
}
.legal-content {
	line-height: 1.8;
	font-size: 15px;
	color: var(--text-secondary);
}
.legal-home {
	display: inline-block;
	margin-top: var(--space-5);
	color: var(--accent);
	font-weight: 700;
	font-size: 14px;
}

/* 슬롯으로 주입되는 본문 마크업 스타일 */
.legal-content :slotted(h2) {
	font-size: 18px;
	font-weight: 800;
	color: var(--text-primary);
	margin: var(--space-6) 0 var(--space-3);
}
.legal-content :slotted(h2:first-child) {
	margin-top: 0;
}
.legal-content :slotted(h3) {
	font-size: 15px;
	font-weight: 700;
	color: var(--text-primary);
	margin: var(--space-4) 0 var(--space-2);
}
.legal-content :slotted(p) {
	margin-bottom: var(--space-3);
}
.legal-content :slotted(ul),
.legal-content :slotted(ol) {
	margin: 0 0 var(--space-3);
	padding-left: var(--space-5);
	list-style: disc;
}
.legal-content :slotted(ol) {
	list-style: decimal;
}
.legal-content :slotted(li) {
	margin-bottom: var(--space-2);
}
.legal-content :slotted(strong) {
	color: var(--text-primary);
	font-weight: 700;
}
.legal-content :slotted(a) {
	color: var(--accent);
	text-decoration: underline;
	word-break: break-all;
}
.legal-content :slotted(table) {
	width: 100%;
	border-collapse: collapse;
	margin: var(--space-3) 0;
	font-size: 14px;
}
.legal-content :slotted(th),
.legal-content :slotted(td) {
	border: 1px solid var(--border-subtle);
	padding: var(--space-2) var(--space-3);
	text-align: left;
	vertical-align: top;
}
.legal-content :slotted(th) {
	background: var(--bg-surface);
	color: var(--text-primary);
	font-weight: 700;
	border-top: 2px solid var(--accent);
}
.legal-content :slotted(.notice) {
	border: 1px solid var(--danger);
	background: var(--danger-soft);
	border-radius: var(--radius-md);
	padding: var(--space-4);
	color: var(--text-primary);
}
</style>
