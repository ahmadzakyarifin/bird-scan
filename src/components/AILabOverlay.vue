<template>
  <div class="w-full max-w-2xl mx-auto pointer-events-auto bg-white/90 dark:bg-gray-900/90 backdrop-blur-xl p-8 rounded-3xl shadow-[0_0_50px_rgba(16,185,129,0.2)] border border-emerald-500/20 transform transition-all duration-500 translate-y-0 opacity-100 flex flex-col gap-6">
    
    <div class="flex justify-between items-start">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-600 dark:text-emerald-400 text-xs font-bold uppercase tracking-widest mb-2 border border-emerald-500/20">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z" /></svg>
          Sistem Analisis
        </div>
        <h2 class="text-3xl font-extrabold text-gray-900 dark:text-white tracking-tight">AI Laboratory</h2>
        <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Pusat identifikasi spesies menggunakan visi komputer canggih.</p>
      </div>
      <button @click="$emit('close')" class="w-10 h-10 rounded-full bg-gray-100 dark:bg-gray-800 hover:bg-red-100 dark:hover:bg-red-900/40 hover:text-red-600 flex items-center justify-center text-gray-500 dark:text-gray-400 transition-colors shadow-sm">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
      </button>
    </div>

    <!-- Scanner Area Simulation -->
    <div class="relative w-full aspect-[16/9] bg-black rounded-2xl overflow-hidden border border-gray-800 shadow-inner group flex items-center justify-center">
      
      <!-- Placeholder Camera / Scanner animation -->
      <div class="absolute inset-0 flex flex-col items-center justify-center gap-4 z-10" v-if="!isScanning && !scanResult">
        <div class="w-16 h-16 rounded-full bg-emerald-500/20 flex items-center justify-center text-emerald-400 animate-pulse border border-emerald-500/30">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-8 w-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" /></svg>
        </div>
        <p class="text-white font-medium text-sm">Kamera Siap</p>
      </div>

      <!-- Scanning Hologram Effect -->
      <div v-if="isScanning" class="absolute inset-0 z-20 flex flex-col items-center justify-center bg-emerald-900/80 backdrop-blur-sm">
        <div class="w-full h-1 bg-emerald-400 absolute top-0 left-0 animate-scan-line shadow-[0_0_20px_#34d399]"></div>
        <div class="text-emerald-400 text-6xl mb-4 animate-pulse">🌿</div>
        <p class="text-emerald-300 font-mono text-sm tracking-widest uppercase">Menganalisis Pola Daun...</p>
      </div>
      
      <!-- Scan Result -->
      <div v-if="scanResult" class="absolute inset-0 z-30 flex flex-col items-center justify-center bg-black/80 backdrop-blur-md p-6">
        <div class="bg-emerald-500/20 text-emerald-400 p-4 rounded-full mb-4">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
        </div>
        <h3 class="text-2xl font-bold text-white">{{ scanResult.name }}</h3>
        <p class="text-emerald-400 font-mono mt-1">{{ scanResult.accuracy }}% Akurasi</p>
        <p class="text-gray-300 text-center text-sm mt-4 max-w-sm">{{ scanResult.desc }}</p>
      </div>
    </div>

    <!-- Actions -->
    <div class="grid grid-cols-2 gap-4">
      <button 
        @click="simulateScan"
        class="w-full py-4 bg-emerald-600 hover:bg-emerald-500 text-white rounded-xl font-bold shadow-[0_0_15px_rgba(5,150,105,0.4)] transition-all active:scale-95 flex items-center justify-center gap-2"
        :disabled="isScanning"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" /></svg>
        Unggah Foto
      </button>
      <button 
        @click="simulateScan"
        class="w-full py-4 bg-gray-900 dark:bg-white text-white dark:text-gray-900 rounded-xl font-bold shadow-lg transition-all hover:-translate-y-1 active:scale-95 flex items-center justify-center gap-2"
        :disabled="isScanning"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" /></svg>
        Ambil Gambar
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const emit = defineEmits(['close'])
const isScanning = ref(false)
const scanResult = ref(null)

function simulateScan() {
  scanResult.value = null
  isScanning.value = true
  
  // Simulate AI processing time
  setTimeout(() => {
    isScanning.value = false
    scanResult.value = {
      name: "Monstera Deliciosa",
      accuracy: 98.5,
      desc: "Berhasil diidentifikasi! Data telah ditambahkan ke Ensiklopedia dan benihnya mulai ditanam di Botanical Garden Anda."
    }
  }, 2500)
}
</script>

<style scoped>
@keyframes scan-line {
  0% { top: 0; opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { top: 100%; opacity: 0; }
}
.animate-scan-line {
  animation: scan-line 2s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}
</style>
