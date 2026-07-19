<template>
  <div class="w-full max-w-4xl mx-auto pointer-events-auto bg-white/95 dark:bg-[#0a0a0a]/95 backdrop-blur-2xl p-8 rounded-3xl shadow-2xl border border-yellow-500/20 transform transition-all duration-500 translate-y-0 opacity-100 flex flex-col h-[80vh]">
    
    <div class="flex justify-between items-start mb-6 shrink-0">
      <div>
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-yellow-500/10 text-yellow-600 dark:text-yellow-400 text-xs font-bold uppercase tracking-widest mb-2 border border-yellow-500/20">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" /></svg>
          Koleksi Pribadi
        </div>
        <h2 class="text-3xl font-extrabold text-gray-900 dark:text-white tracking-tight">Aviary Konservasi</h2>
        <p class="text-sm text-gray-500 dark:text-gray-400 mt-1">Burung yang berhasil Anda temukan di pulau ini akan didokumentasikan di sini.</p>
      </div>
      <button @click="$emit('close')" class="w-10 h-10 rounded-full bg-gray-100 dark:bg-gray-800 hover:bg-gray-200 dark:hover:bg-gray-700 flex items-center justify-center text-gray-500 dark:text-gray-400 transition-colors shadow-sm">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
      </button>
    </div>

    <!-- Collection Grid -->
    <div class="flex-1 overflow-y-auto pr-2 custom-scrollbar relative">
      <!-- Empty State if No Birds Found for this Island -->
      <div v-if="filteredBirds.length === 0" class="absolute inset-0 flex flex-col items-center justify-center text-center p-8 z-10">
        <div class="w-24 h-24 bg-gray-100 dark:bg-gray-800 rounded-full flex items-center justify-center text-5xl mb-4 shadow-inner">
          🔍
        </div>
        <h3 class="text-xl font-bold text-gray-900 dark:text-white mb-2">Belum Ada Catatan</h3>
        <p class="text-gray-500 dark:text-gray-400 max-w-sm">Anda belum menemukan spesies burung dari pulau ini. Silakan kembali ke Peta Utama dan gunakan Scanner untuk memindai burung!</p>
      </div>

      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4" :class="{ 'opacity-20 pointer-events-none': filteredBirds.length === 0 }">
        
        <!-- Collected Bird Cards -->
        <div v-for="bird in filteredBirds" :key="bird.id" class="bg-gray-50 dark:bg-gray-900 rounded-2xl p-4 border border-gray-200 dark:border-gray-800 hover:border-emerald-500/50 transition-colors cursor-pointer group flex flex-col items-center text-center">
          <div class="w-20 h-20 bg-emerald-100 dark:bg-emerald-900/30 rounded-full overflow-hidden flex items-center justify-center text-4xl mb-3 shadow-inner group-hover:scale-110 transition-transform">
            <img v-if="bird.image" :src="bird.image" class="w-full h-full object-cover" alt="Bird" />
            <span v-else>🪶</span>
          </div>
          <h3 class="font-bold text-gray-900 dark:text-white text-sm">{{ bird.name }}</h3>
          <span class="text-[10px] text-emerald-600 dark:text-emerald-400 font-mono mt-1">{{ bird.name_en || 'Spesies Lokal' }}</span>
          <div class="mt-3 text-xs text-gray-500 dark:text-gray-400 bg-gray-200 dark:bg-gray-800 px-2 py-1 rounded w-full">
            Ditemukan: {{ new Date(bird.id).toLocaleDateString('id-ID') }}
          </div>
        </div>

        <!-- Empty Slots / Progress -->
        <div v-for="i in emptySlots" :key="'empty-'+i" class="bg-gray-50/50 dark:bg-gray-900/30 rounded-2xl p-4 border border-dashed border-gray-300 dark:border-gray-700 flex flex-col items-center justify-center opacity-50">
          <div class="w-16 h-16 rounded-full border-2 border-dashed border-gray-300 dark:border-gray-700 flex items-center justify-center text-gray-400 mb-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
          </div>
          <span class="text-xs text-gray-400 font-medium">Slot Kosong</span>
        </div>

      </div>
    </div>

    <!-- Status Bar -->
    <div class="mt-6 pt-4 border-t border-gray-200 dark:border-gray-800 flex justify-between items-center shrink-0">
      <div class="flex items-center gap-3">
        <div class="w-12 h-12 rounded-full bg-emerald-500 flex items-center justify-center text-white font-bold text-lg shadow-lg">
          {{ filteredBirds.length }}
        </div>
        <div>
          <h4 class="font-bold text-gray-900 dark:text-white text-sm">Level Peneliti: Ornitolog</h4>
          <div class="w-32 h-1.5 bg-gray-200 dark:bg-gray-800 rounded-full mt-1 overflow-hidden">
            <div class="h-full bg-emerald-500 rounded-full" :style="{ width: (filteredBirds.length / (filteredBirds.length + emptySlots)) * 100 + '%' }"></div>
          </div>
        </div>
      </div>
      <button class="px-5 py-2.5 bg-emerald-50 dark:bg-emerald-900/20 text-emerald-600 dark:text-emerald-400 font-bold text-sm rounded-xl hover:bg-emerald-100 dark:hover:bg-emerald-900/40 transition-colors">
        Lihat Statistik Lengkap
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  islandId: String
})

const emit = defineEmits(['close'])

const birdIslandMap = {
  'Jalak Bali': 'jawa',
  'Elang Jawa': 'jawa',
  'Burung Cendrawasih': 'papua',
  'Maleo': 'sulawesi',
  'Kasuari': 'papua',
  'Burung Merak': 'jawa',
  'Jalak Putih': 'jawa',
  'Rangkong Gading': 'kalimantan',
  'Kakatua Raja': 'papua',
  'Nuri Kepala Hitam': 'papua',
  'Murai Batu': 'sumatra',
  'Cucak Rawa': 'sumatra'
}

const faunaHistory = ref(JSON.parse(localStorage.getItem('fauna_history') || '[]'))

const filteredBirds = computed(() => {
  if (!props.islandId) return faunaHistory.value;
  return faunaHistory.value.filter(bird => birdIslandMap[bird.name] === props.islandId || (props.islandId === 'jawa' && !birdIslandMap[bird.name]))
})

const emptySlots = computed(() => Math.max(0, 10 - filteredBirds.value.length))
</script>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
  width: 6px;
}
.custom-scrollbar::-webkit-scrollbar-track {
  background: transparent;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
  background: rgba(156, 163, 175, 0.5);
  border-radius: 10px;
}
</style>
