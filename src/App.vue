<template>
  <div class="min-h-screen bg-white dark:bg-[#0a0a0a] text-gray-900 dark:text-gray-100 transition-colors duration-300 font-sans selection:bg-emerald-500/30 flex flex-col relative">
    <div v-if="globalError" class="absolute inset-0 z-[9999] bg-red-900 text-white p-10 overflow-auto">
      <h1 class="text-4xl font-bold mb-4">Aplikasi Crash!</h1>
      <pre class="bg-black/50 p-6 rounded-xl text-sm whitespace-pre-wrap">{{ globalError }}</pre>
      <pre class="bg-black/50 p-6 rounded-xl text-sm whitespace-pre-wrap mt-4">{{ globalErrorInfo }}</pre>
    </div>
    <router-view v-else />
  </div>
</template>

<script setup>
import { ref, onMounted, onErrorCaptured } from 'vue'

const globalError = ref(null)
const globalErrorInfo = ref(null)

onErrorCaptured((err, instance, info) => {
  globalError.value = err.stack || err.message || String(err)
  globalErrorInfo.value = info
  console.error("VUE ERROR:", err, info)
  return false // prevent propagation
})

onMounted(() => {
  if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    document.documentElement.classList.add('dark')
  } else {
    document.documentElement.classList.remove('dark')
  }
})
</script>

<style>
body {
  margin: 0;
  padding: 0;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
