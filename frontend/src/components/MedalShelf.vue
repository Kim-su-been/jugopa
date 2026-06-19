<script setup>
import { computed } from 'vue'

const props = defineProps({
  totalSolved: { type: Number, default: 0 },
  longestStreak: { type: Number, default: 0 },
})

// 연속 풀이 퀘스트 / 문제풀이 갯수 퀘스트
const STREAK_QUESTS = [3, 7, 30, 100, 200]
const COUNT_QUESTS = [5, 20, 50, 100, 200]
const MEDAL_ICONS = ['🥉', '🥈', '🥇', '🏅', '👑']

const streakMedals = computed(() =>
  STREAK_QUESTS.map((threshold, i) => ({
    threshold,
    icon: MEDAL_ICONS[i],
    label: `${threshold}일 연속`,
    unlocked: props.longestStreak >= threshold,
  })),
)
const countMedals = computed(() =>
  COUNT_QUESTS.map((threshold, i) => ({
    threshold,
    icon: MEDAL_ICONS[i],
    label: `${threshold}문제`,
    unlocked: props.totalSolved >= threshold,
  })),
)

const collected = computed(
  () => streakMedals.value.filter((m) => m.unlocked).length + countMedals.value.filter((m) => m.unlocked).length,
)
</script>

<template>
  <div class="shelf">
    <div class="shelf-head">
      <h3 class="shelf-title">수집한 메달</h3>
      <span class="collected num">{{ collected }} / {{ streakMedals.length + countMedals.length }}</span>
    </div>

    <div class="group">
      <p class="group-label">🔥 연속 풀이</p>
      <div class="medals">
        <div v-for="m in streakMedals" :key="'s' + m.threshold" class="medal" :class="{ locked: !m.unlocked }">
          <span class="icon">{{ m.unlocked ? m.icon : '🔒' }}</span>
          <span class="m-label">{{ m.label }}</span>
        </div>
      </div>
    </div>

    <div class="group">
      <p class="group-label">📚 문제풀이 갯수</p>
      <div class="medals">
        <div v-for="m in countMedals" :key="'c' + m.threshold" class="medal" :class="{ locked: !m.unlocked }">
          <span class="icon">{{ m.unlocked ? m.icon : '🔒' }}</span>
          <span class="m-label">{{ m.label }}</span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.shelf-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: var(--space-4);
}
.shelf-title {
  font-size: 15px;
  font-weight: 700;
}
.collected {
  font-size: 13px;
  font-weight: 700;
  color: var(--accent);
}
.group {
  margin-bottom: var(--space-4);
}
.group:last-child {
  margin-bottom: 0;
}
.group-label {
  font-size: 13px;
  font-weight: 700;
  color: var(--text-secondary);
  margin-bottom: var(--space-3);
}
.medals {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: var(--space-2);
}
.medal {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 4px;
  padding: var(--space-3) 4px;
  border-radius: var(--radius-md);
  background: var(--bg-surface);
  border: 1px solid var(--border-subtle);
}
.medal.locked {
  opacity: 0.45;
}
.icon {
  font-size: 24px;
}
.m-label {
  font-size: 11px;
  font-weight: 600;
  color: var(--text-secondary);
  text-align: center;
}
@media (max-width: 480px) {
  .icon {
    font-size: 20px;
  }
  .m-label {
    font-size: 10px;
  }
}
</style>
