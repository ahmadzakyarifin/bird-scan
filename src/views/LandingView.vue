<template>
  <div class="relative w-full h-screen bg-gradient-to-b from-sky-200 via-sky-100 to-[#f8fafc] overflow-hidden font-sans selection:bg-emerald-500/30">
    
    <!-- Aesthetic Background Elements -->
    <div class="absolute inset-0 bg-grid opacity-60 pointer-events-none"></div>
    <div class="absolute top-[20%] left-[20%] w-[500px] h-[500px] bg-emerald-300/20 rounded-full blur-[100px] pointer-events-none animate-pulse-slow"></div>
    <div class="absolute bottom-[20%] right-[20%] w-[600px] h-[600px] bg-teal-300/20 rounded-full blur-[120px] pointer-events-none animate-pulse-slow" style="animation-delay: 2s;"></div>
    
    <!-- Giant Indonesia Map Watermark Background -->
    <img src="/islands/map-outline.svg" class="absolute inset-0 w-full h-full object-cover opacity-15 pointer-events-none z-0 translate-y-[20%] scale-110" style="filter: drop-shadow(0 0 10px rgba(16,185,129,0.5));" />
    
    <!-- Environmental Particles (Clouds & Fireflies) -->
    <div @mouseenter="playCloudSound" class="cloud absolute top-[10%] left-[-20%] opacity-80 animate-cloud-1 cursor-pointer transition-opacity hover:opacity-100 text-[5rem] z-30">☁️</div>
    <div @mouseenter="playCloudSound" class="cloud absolute top-[25%] left-[-20%] opacity-70 animate-cloud-2 cursor-pointer transition-opacity hover:opacity-100 text-[6rem] z-30">☁️</div>
    <div @mouseenter="playCloudSound" class="cloud absolute top-[50%] left-[-20%] opacity-50 animate-cloud-2 cursor-pointer transition-opacity hover:opacity-100 text-[4rem] z-30" style="animation-delay: 8s; animation-duration: 35s;">☁️</div>
    <div @mouseenter="playCloudSound" class="cloud absolute top-[70%] left-[-20%] opacity-75 animate-cloud-1 cursor-pointer transition-opacity hover:opacity-100 text-[7rem] z-30" style="animation-delay: 2s; animation-duration: 50s;">☁️</div>
    <!-- Tambahan Awan -->
    <div @mouseenter="playCloudSound" class="cloud absolute top-[5%] left-[-20%] opacity-65 animate-cloud-2 cursor-pointer transition-opacity hover:opacity-100 text-[5rem] z-30" style="animation-delay: 12s; animation-duration: 40s;">☁️</div>
    <div @mouseenter="playCloudSound" class="cloud absolute top-[35%] left-[-20%] opacity-40 animate-cloud-2 cursor-pointer transition-opacity hover:opacity-100 text-[9rem] z-30" style="animation-delay: 3s; animation-duration: 60s;">☁️</div>
    
    <!-- Birds -->
    <div @mouseenter="playBirdSound" class="absolute top-[30%] left-[-10%] opacity-80 animate-bird-1 cursor-pointer text-2xl" style="filter: drop-shadow(0 10px 5px rgba(0,0,0,0.2)); z-index: 10;">🦅</div>
    <div @mouseenter="playBirdSound" class="absolute top-[50%] left-[-10%] opacity-60 animate-bird-2 cursor-pointer text-xl" style="animation-duration: 40s; filter: drop-shadow(0 10px 5px rgba(0,0,0,0.2)); z-index: 10;">🕊️</div>
    <!-- Tambahan Burung -->
    <div @mouseenter="playBirdSound" class="absolute top-[20%] left-[-10%] opacity-70 animate-bird-1 cursor-pointer text-xl" style="animation-delay: 7s; animation-duration: 35s; filter: drop-shadow(0 10px 5px rgba(0,0,0,0.2)); z-index: 10;">🦜</div>
    <div @mouseenter="playBirdSound" class="absolute top-[65%] left-[-10%] opacity-75 animate-bird-2 cursor-pointer text-2xl" style="animation-delay: 12s; animation-duration: 45s; filter: drop-shadow(0 10px 5px rgba(0,0,0,0.2)); z-index: 10;">🦅</div>
    <div @mouseenter="playBirdSound" class="absolute top-[80%] left-[-10%] opacity-65 animate-bird-1 cursor-pointer text-lg" style="animation-delay: 4s; animation-duration: 25s; filter: drop-shadow(0 10px 5px rgba(0,0,0,0.2)); z-index: 10;">🕊️</div>

    <div class="firefly absolute top-[40%] left-[30%] w-1.5 h-1.5 bg-yellow-300 rounded-full blur-[1px] animate-firefly-1 pointer-events-none"></div>
    <div class="firefly absolute top-[60%] left-[60%] w-2 h-2 bg-yellow-200 rounded-full blur-[2px] animate-firefly-2 pointer-events-none"></div>

    <!-- Gamified Header -->
    <header class="absolute top-0 left-0 w-full z-40 px-6 py-6 flex items-center justify-between pointer-events-none">
      <div class="flex items-center gap-4 bg-white/80 backdrop-blur-md px-5 py-3 rounded-2xl shadow-sm border border-emerald-100">
        <div class="w-12 h-12 bg-gradient-to-br from-emerald-400 to-emerald-600 rounded-xl flex items-center justify-center text-white shadow-inner">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </div>
        <div>
          <h1 class="text-xl font-black tracking-tight text-emerald-950">FloraNusantara</h1>
          <div class="flex items-center gap-2 mt-0.5">
            <span class="text-xs font-bold text-emerald-600">Buku Histori Flora</span>
            <span class="text-[10px] text-gray-500 font-medium px-2 py-0.5 bg-gray-100 rounded-full">Total: {{ floraHistory.length }} Flora</span>
          </div>
        </div>
      </div>
    </header>

    <!-- Map Container -->
    <div 
      class="absolute inset-0 w-full h-full flex items-center justify-center transition-transform duration-1000 ease-in-out origin-center"
      :style="mapTransformStyle"
    >
      <!-- The Archipelago Wrapper -->
      <div class="relative w-[1500px] h-[800px] max-w-full max-h-full scale-50 md:scale-75 lg:scale-100 mt-10">
        
        <!-- Islands -->
        <div 
          v-for="island in islands" 
          :key="island.id"
          class="absolute transition-all duration-500 cursor-pointer group flex flex-col items-center justify-center animate-float"
          :class="[island.positionClass, island.sizeClass]"
          :style="`animation-delay: ${island.animDelay}s; z-index: ${hoveredIsland?.id === island.id ? 20 : 10}`"
          @mouseenter="handleIslandHover(island)"
          @mouseleave="hoveredIsland = null"
          @click="selectIsland(island)"
        >
          <!-- Water Ripple / Fog Base -->
          <div class="absolute bottom-[-10%] w-[80%] h-[30%] bg-emerald-300/20 rounded-full blur-[8px] animate-ripple pointer-events-none -z-20"></div>

          <!-- Badges -->
          <div class="absolute -top-4 -right-4 z-30 flex gap-2">
            <!-- Lock Badge -->
            <div v-if="island.isLocked" class="bg-white/70 backdrop-blur-md text-emerald-900 w-9 h-9 rounded-full flex items-center justify-center shadow-[0_5px_15px_rgba(0,0,0,0.15)] border-2 border-white/80 group/lock cursor-not-allowed transition-transform hover:scale-110">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5 9V7a5 5 0 0110 0v2a2 2 0 012 2v5a2 2 0 01-2 2H5a2 2 0 01-2-2v-5a2 2 0 012-2zm8-2v2H7V7a3 3 0 016 0z" clip-rule="evenodd" /></svg>
              <div class="absolute top-11 w-36 bg-white/95 backdrop-blur-xl text-gray-700 text-[11px] text-center p-2 rounded-xl opacity-0 group-hover/lock:opacity-100 transition-opacity pointer-events-none font-bold border border-gray-100 shadow-xl">
                Masih belum tersedia
              </div>
            </div>
            <!-- Plant Count Badge -->
            <div v-else class="bg-emerald-500 text-white text-sm font-black w-8 h-8 rounded-full flex items-center justify-center shadow-lg border-2 border-white" title="Total Flora Ditemukan">
              <template v-if="getIslandPlantsCount(island.id) > 0">
                {{ getIslandPlantsCount(island.id) }}
              </template>
              <template v-else>
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd" /></svg>
              </template>
            </div>
          </div>

          <!-- The Island Image -->
          <img 
            :src="island.image" 
            :alt="island.name" 
            class="w-full h-auto drop-shadow-2xl transition-all duration-500 group-hover:scale-[1.08] group-hover:-translate-y-6"
            style="filter: drop-shadow(0 30px 25px rgba(0,0,0,0.3));"
          />
          
          <!-- Subtle Glow on Hover -->
          <div class="absolute inset-0 bg-emerald-400/0 group-hover:bg-emerald-400/30 blur-[40px] rounded-full transition-colors duration-500 -z-10"></div>
        </div>
      </div>
    </div>

    <!-- Global Scanner HUD -->
    <div 
      v-if="!isZooming && !activeOverlay"
      class="absolute bottom-10 left-1/2 -translate-x-1/2 z-40 flex flex-col items-center animate-fade-in-up pointer-events-auto"
    >
      <button 
        @click="openScanner"
        class="group relative flex items-center gap-3 px-8 py-4 bg-emerald-600 hover:bg-emerald-500 rounded-full shadow-[0_15px_40px_-10px_rgba(16,185,129,0.8)] border-4 border-emerald-100 transition-all duration-300 hover:scale-105 active:scale-95 overflow-hidden"
      >
        <div class="absolute inset-0 bg-white/20 translate-x-[-100%] group-hover:translate-x-[100%] transition-transform duration-700 skew-x-12"></div>
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-white animate-pulse" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z" />
        </svg>
        <span class="text-white font-bold tracking-wide">Mulai Scan</span>
      </button>
    </div>

    <!-- Island Info Detailed Hover Card -->
    <div 
      v-if="hoveredIsland && !isZooming"
      class="absolute bottom-10 left-10 z-30 pointer-events-none transition-all duration-300"
    >
      <div class="bg-white/95 backdrop-blur-md px-6 py-6 rounded-3xl shadow-2xl border border-emerald-50 w-72 transform animate-fade-in-up">
        <div class="flex items-center gap-3 mb-4">
          <span class="text-4xl">{{ hoveredIsland.icon }}</span>
          <div>
            <h3 class="text-2xl font-black text-gray-900 tracking-tight">{{ hoveredIsland.name }}</h3>
            <span v-if="hoveredIsland.isLocked" class="text-xs font-bold px-2 py-0.5 bg-gray-100 text-gray-500 rounded-md">Segera Hadir</span>
            <span v-else class="text-xs font-bold px-2 py-0.5 bg-emerald-100 text-emerald-700 rounded-md">Wilayah Eksplorasi</span>
          </div>
        </div>
        
        <div class="h-[1px] w-full bg-gray-100 mb-4"></div>
        
        <div v-if="!hoveredIsland.isLocked" class="flex flex-col gap-3 mb-5">
          <div class="flex items-center gap-3 text-sm font-medium text-gray-600">
            <span>🌱</span> {{ getIslandPlantsCount(hoveredIsland.id) }} Histori Penemuan
          </div>
        </div>
        
        <div v-if="hoveredIsland.isLocked" class="mt-2 w-full py-2 bg-gray-50 text-gray-400 text-center font-bold text-sm rounded-xl border border-gray-100">
          Belum Tersedia
        </div>
        <div v-else class="mt-2 w-full py-2 bg-emerald-50 text-emerald-600 text-center font-bold text-sm rounded-xl border border-emerald-100">
          Klik untuk Menjelajah
        </div>
      </div>
    </div>

    <!-- Scanner Modal Overlay -->
    <div v-if="activeOverlay === 'scanner'" class="absolute inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm animate-fade-in">
      <div class="bg-white rounded-[2rem] w-[90%] max-w-lg shadow-2xl relative overflow-hidden flex flex-col p-8 items-center text-center">
        <button @click="closeOverlay" class="absolute top-4 right-4 text-gray-400 hover:text-gray-800 transition-colors w-10 h-10 flex items-center justify-center rounded-full hover:bg-gray-100">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12" /></svg>
        </button>

        <div v-if="scanStep === 'upload'" class="w-full flex flex-col items-center">
          <div class="w-20 h-20 bg-emerald-100 text-emerald-600 rounded-full flex items-center justify-center mb-6">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" /></svg>
          </div>
          <h2 class="text-2xl font-black text-gray-800 mb-2">Identifikasi Flora</h2>
          <p class="text-gray-500 mb-8 font-medium">Unggah foto atau gunakan kamera untuk memindai tanaman.</p>
          
          <input type="file" ref="fileInput" @change="startScan" accept="image/*" class="hidden" />
          
          <div class="flex flex-col sm:flex-row w-full gap-4">
            <button @click="$refs.fileInput.click()" class="flex-1 bg-white border-2 border-emerald-600 text-emerald-600 hover:bg-emerald-50 font-bold py-4 rounded-xl shadow-sm transition-transform active:scale-95 flex flex-col items-center justify-center gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" /></svg>
              Upload File
            </button>
            <button @click="openCamera" class="flex-1 bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-4 rounded-xl shadow-lg transition-transform active:scale-95 flex flex-col items-center justify-center gap-2">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" /></svg>
              Buka Kamera
            </button>
          </div>
        </div>

        <div v-else-if="scanStep === 'camera'" class="w-full flex flex-col items-center">
          <div class="relative w-full h-64 bg-black rounded-xl overflow-hidden mb-6">
            <video ref="videoElement" autoplay playsinline class="w-full h-full object-cover"></video>
            <div class="absolute inset-0 border-4 border-emerald-500/50 m-4 rounded-lg pointer-events-none"></div>
          </div>
          <div class="flex gap-4 w-full">
            <button @click="closeCamera" class="flex-1 bg-gray-100 text-gray-700 font-bold py-3 rounded-xl hover:bg-gray-200 transition-colors">Batal</button>
            <button @click="takePhoto" class="flex-[2] bg-emerald-600 text-white font-bold py-3 rounded-xl hover:bg-emerald-700 transition-colors shadow-lg">Ambil Foto</button>
          </div>
          <canvas ref="canvasElement" class="hidden"></canvas>
        </div>

        <div v-else-if="scanStep === 'scanning'" class="w-full flex flex-col items-center py-8">
          <div class="relative w-40 h-40 rounded-2xl overflow-hidden mb-6 border-4 border-gray-100 shadow-md">
            <img :src="uploadedImageSrc" class="w-full h-full object-cover grayscale opacity-70" />
            <div class="absolute inset-0 bg-emerald-500/20"></div>
            <div class="absolute top-0 left-0 w-full h-2 bg-emerald-400 shadow-[0_0_15px_rgba(52,211,153,1)] animate-scan-line"></div>
          </div>
          <h2 class="text-xl font-bold text-gray-800 mb-2 animate-pulse">Menganalisis Flora...</h2>
          <p class="text-emerald-600 text-sm font-semibold">Mencocokkan ke 110 spesies lokal</p>
        </div>

        <div v-else-if="scanStep === 'result'" class="w-full flex flex-col items-center">
          <div class="relative w-48 h-48 rounded-2xl overflow-hidden mb-5 border-4 border-emerald-100 shadow-lg">
            <img :src="uploadedImageSrc" class="w-full h-full object-cover" />
            <div class="absolute bottom-0 left-0 right-0 bg-emerald-600 text-white text-xs font-bold py-1">Akurasi {{ scanResult.confidence }}%</div>
          </div>
          <h2 class="text-3xl font-black text-gray-800">{{ scanResult.name }}</h2>
          <p class="text-emerald-600 font-bold mb-4 flex items-center gap-1">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" /></svg>
            Ditemukan di {{ scanResult.islandName }}
          </p>
          <p class="text-sm text-gray-500 mb-6 px-4">{{ scanResult.desc }}</p>
          <button @click="saveScanToHistory" class="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-3.5 rounded-xl shadow-lg transition-transform active:scale-95">
            Simpan ke Histori
          </button>
        </div>
      </div>
    </div>

    <!-- Island Detailed Overlay (History Pagination) -->
    <div v-if="activeOverlay === 'island'" class="absolute inset-0 z-50 pointer-events-auto bg-black/40 backdrop-blur-sm flex justify-center items-center p-4 animate-fade-in">
      <div class="bg-white rounded-[2rem] w-full max-w-5xl shadow-2xl relative max-h-[90vh] flex flex-col border border-gray-100 overflow-hidden">
        
        <!-- Header -->
        <div class="px-8 py-6 border-b border-gray-100 flex items-center justify-between bg-gray-50/50">
          <div class="flex items-center gap-4">
            <span class="text-5xl">{{ activeIsland?.icon }}</span>
            <div>
              <h2 class="text-3xl font-black text-emerald-950 tracking-tight">Histori {{ activeIsland?.name }}</h2>
              <p class="text-gray-500 font-medium text-sm mt-0.5">Total {{ islandPlants.length }} penemuan spesifik flora</p>
            </div>
          </div>
          <button @click="closeOverlay" class="w-12 h-12 bg-white rounded-full flex items-center justify-center text-gray-400 hover:bg-gray-100 hover:text-red-500 transition-colors shadow-sm border border-gray-200">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12" /></svg>
          </button>
        </div>
        
        <!-- Body (Paginated Grid) -->
        <div class="p-8 flex-1 overflow-y-auto bg-white">
          <div class="grid grid-cols-2 sm:grid-cols-4 gap-4 md:gap-6">
             <div 
               v-for="(slot, index) in paginatedGridSlots" 
               :key="index"
               class="aspect-square rounded-2xl border flex flex-col items-center justify-center overflow-hidden relative transition-all duration-300"
               :class="slot ? 'bg-gray-50 border-gray-200 cursor-pointer shadow-sm hover:shadow-xl hover:-translate-y-2 group' : 'bg-gray-50/50 border-dashed border-gray-300'"
               @click="slot ? viewPlantDetail(slot) : null"
             >
               <template v-if="slot">
                 <img :src="slot.image" class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-700" />
                 <div class="absolute inset-0 bg-gradient-to-t from-emerald-900/90 via-emerald-900/20 to-transparent flex flex-col justify-end p-4 translate-y-2 group-hover:translate-y-0 transition-transform">
                   <span class="text-white font-black text-sm md:text-base leading-tight drop-shadow-md truncate">{{ slot.name }}</span>
                   <span class="text-emerald-300 text-[10px] md:text-xs font-bold mt-1 drop-shadow-md tracking-wider uppercase">{{ slot.confidence }}% MATCH</span>
                 </div>
               </template>
               <template v-else>
                 <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10 text-gray-300 mb-2 opacity-50" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
                 <span class="text-gray-400 text-xs font-bold opacity-70">Belum Ada</span>
               </template>
             </div>
          </div>
        </div>
        
        <!-- Pagination Controls -->
        <div v-if="totalPages > 1" class="px-8 py-4 border-t border-gray-100 flex items-center justify-between bg-gray-50/50">
          <button @click="currentPage--" :disabled="currentPage === 1" class="px-4 py-2 rounded-lg font-bold transition-colors" :class="currentPage === 1 ? 'text-gray-300 cursor-not-allowed' : 'text-emerald-600 hover:bg-emerald-100 bg-white shadow-sm border border-emerald-200'">
            &larr; Sebelumnya
          </button>
          <span class="font-bold text-gray-500 text-sm">Halaman {{ currentPage }} dari {{ totalPages }}</span>
          <button @click="currentPage++" :disabled="currentPage === totalPages" class="px-4 py-2 rounded-lg font-bold transition-colors" :class="currentPage === totalPages ? 'text-gray-300 cursor-not-allowed' : 'text-emerald-600 hover:bg-emerald-100 bg-white shadow-sm border border-emerald-200'">
            Selanjutnya &rarr;
          </button>
        </div>
      </div>
    </div>

    <!-- Specific Plant Detail Modal -->
    <div v-if="selectedPlantDetail" class="absolute inset-0 z-[60] flex items-center justify-center bg-black/80 backdrop-blur-md animate-fade-in">
      <div class="bg-white rounded-3xl w-[90%] max-w-lg shadow-2xl relative overflow-hidden flex flex-col">
        <button @click="selectedPlantDetail = null" class="absolute top-4 right-4 z-10 bg-black/50 hover:bg-black/80 text-white rounded-full p-2 backdrop-blur-md transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12" /></svg>
        </button>
        <img :src="selectedPlantDetail.image" class="w-full h-64 object-cover" />
        <div class="p-8">
          <div class="flex items-start justify-between mb-2">
            <h2 class="text-3xl font-black text-gray-800">{{ selectedPlantDetail.name }}</h2>
            <span class="bg-emerald-100 text-emerald-700 text-xs font-bold px-3 py-1 rounded-full whitespace-nowrap mt-1">Akurasi {{ selectedPlantDetail.confidence }}%</span>
          </div>
          <p class="text-emerald-600 font-bold mb-6 flex items-center gap-1 text-sm">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" /></svg>
            Wilayah Histori: {{ activeIsland?.name }}
          </p>
          <p class="text-gray-600 leading-relaxed">{{ selectedPlantDetail.desc }}</p>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { soundManager } from '../utils/SoundManager'

const isZooming = ref(false)
const activeOverlay = ref(null) // 'scanner' or 'island'
const activeIsland = ref(null)
const hoveredIsland = ref(null)
const mapZoomData = ref({ scale: 1, x: 0, y: 0 })
const floraHistory = ref(JSON.parse(localStorage.getItem('flora_history') || '[]'))

// Scanner Modal State
const scanStep = ref('upload') // upload, camera, scanning, result
const uploadedImageSrc = ref('')
const fileInput = ref(null)
const videoElement = ref(null)
const canvasElement = ref(null)
let cameraStream = null
const scanResult = ref(null)

// Island Detail State
const currentPage = ref(1)
const itemsPerPage = 8
const selectedPlantDetail = ref(null)

const basePath = import.meta.env.BASE_URL

const islands = computed(() => [
  {
    id: 'sumatra',
    name: 'Sumatra',
    icon: '🌋',
    image: basePath + 'islands/sumatra.png',
    positionClass: 'top-[16%] left-[6%]',
    sizeClass: 'w-[220px] md:w-[280px]',
    zoomData: { scale: 1.8, x: '20%', y: '10%' },
    animDelay: 0.2,
    isLocked: true
  },
  {
    id: 'kalimantan',
    name: 'Kalimantan',
    icon: '🌴',
    image: basePath + 'islands/kalimantan.png',
    positionClass: 'top-[14%] left-[28%]',
    sizeClass: 'w-[240px] md:w-[300px]',
    zoomData: { scale: 1.8, x: '5%', y: '15%' },
    animDelay: 0.8,
    isLocked: true
  },
  {
    id: 'sulawesi',
    name: 'Sulawesi',
    icon: '🌺',
    image: basePath + 'islands/sulawesi.png',
    positionClass: 'top-[28%] left-[50%]',
    sizeClass: 'w-[200px] md:w-[260px]',
    zoomData: { scale: 2, x: '-15%', y: '5%' },
    animDelay: 1.2,
    isLocked: true
  },
  {
    id: 'maluku',
    name: 'Maluku',
    icon: '🏝',
    image: basePath + 'islands/maluku.png',
    positionClass: 'top-[36%] left-[68%]',
    sizeClass: 'w-[150px] md:w-[190px]',
    zoomData: { scale: 2.2, x: '-25%', y: '0%' },
    animDelay: 0.5,
    isLocked: true
  },
  {
    id: 'papua',
    name: 'Papua',
    icon: '🏔',
    image: basePath + 'islands/papua.png',
    positionClass: 'top-[32%] left-[84%]',
    sizeClass: 'w-[240px] md:w-[300px]',
    zoomData: { scale: 1.8, x: '-35%', y: '10%' },
    animDelay: 1.5,
    isLocked: true
  },
  {
    id: 'jawa',
    name: 'Jawa',
    icon: '🌾',
    image: basePath + 'islands/jawa.png',
    positionClass: 'top-[60%] left-[20%]',
    sizeClass: 'w-[190px] md:w-[240px]',
    zoomData: { scale: 2.2, x: '15%', y: '-15%' },
    animDelay: 0.1,
    isLocked: false
  },
  {
    id: 'bali',
    name: 'Bali & Nusa Tenggara',
    icon: '🐢',
    image: basePath + 'islands/bali.png',
    positionClass: 'top-[70%] left-[42%]',
    sizeClass: 'w-[150px] md:w-[200px]',
    zoomData: { scale: 2.2, x: '-5%', y: '-20%' },
    animDelay: 0.6,
    isLocked: true
  }
])

// Mock descriptive text for plants
const plantDescriptions = {
  'Monstera Deliciosa': 'Tanaman hias dengan daun lebar berlubang yang sangat estetik. Sering ditemukan tumbuh di bawah naungan pohon besar di hutan hujan.',
  'Alocasia Amazonica': 'Memiliki daun berbentuk panah dengan warna hijau tua dan garis tulang daun yang kontras. Sangat eksotis.',
  'Sansevieria Trifasciata': 'Dikenal sebagai Lidah Mertua. Tanaman sukulen ini sangat tangguh dan luar biasa dalam menyaring racun di udara.',
  'Syngonium Podophyllum': 'Tanaman merambat yang tumbuh subur di iklim tropis. Daun mudanya berbentuk mata panah yang khas.',
  'Philodendron': 'Keluarga tanaman tropis dengan ratusan spesies. Sangat populer sebagai tanaman hias karena daya tahannya.',
  'Hoya (Wax Plant)': 'Tanaman merambat dengan bunga berbentuk bintang yang terlihat seperti terbuat dari lilin, mengeluarkan aroma harum di malam hari.',
  'Ficus': 'Spesies beringin yang kuat. Di alam liar, ia bisa tumbuh menjadi pohon raksasa yang menjadi rumah bagi banyak satwa.',
  'Epipremnum Aureum (Pothos)': 'Sirih gading adalah tanaman merambat abadi. Sangat adaptif dan mudah diperbanyak dengan stek batang.',
  'Dieffenbachia (Dumb Cane)': 'Tanaman cantik namun bergetah beracun. Daunnya dihiasi corak putih atau kuning yang menyebar dari tengah.',
  'Calathea (Prayer Plant)': 'Daunnya yang bercorak indah akan menutup ke atas pada malam hari layaknya tangan yang sedang berdoa.',
  'Caladium (Keladi)': 'Dikenal dari daunnya yang tipis namun memiliki warna-warni cerah seperti merah, pink, dan putih di tengahnya.',
  'Aglaonema (Chinese Evergreen)': 'Sri Rejeki adalah primadona tanaman hias di Indonesia. Warnanya bervariasi dari hijau hingga merah pekat.',
  'Anthurium': 'Memiliki seludang bunga (*spathe*) yang tebal, mengkilap, dan berwarna mencolok. Tumbuh subur di daerah lembap.',
  'Begonia': 'Spesies yang luar biasa beragam, dihargai karena bentuk dan corak daunnya yang asimetris dan unik.',
  'Peperomia': 'Tanaman mungil berdaun tebal. Habitat aslinya menempel pada batang pohon mati atau bebatuan berlumut.'
}

const plantIslandMap = {
  'Monstera Deliciosa': 'bali',
  'Alocasia Amazonica': 'kalimantan',
  'Sansevieria Trifasciata': 'jawa',
  'Syngonium Podophyllum': 'sulawesi',
  'Philodendron': 'sumatra',
  'Hoya (Wax Plant)': 'papua',
  'Ficus': 'maluku',
  'Epipremnum Aureum (Pothos)': 'jawa',
  'Dieffenbachia (Dumb Cane)': 'sumatra',
  'Calathea (Prayer Plant)': 'kalimantan',
  'Caladium (Keladi)': 'papua',
  'Aglaonema (Chinese Evergreen)': 'bali',
  'Anthurium': 'sulawesi',
  'Begonia': 'maluku',
  'Peperomia': 'kalimantan'
}

const islandPlants = computed(() => {
  if (!activeIsland.value) return []
  return floraHistory.value.filter(p => plantIslandMap[p.name] === activeIsland.value.id || (activeIsland.value.id === 'jawa' && !plantIslandMap[p.name]))
})

const totalPages = computed(() => Math.max(1, Math.ceil(islandPlants.value.length / itemsPerPage)))

const paginatedGridSlots = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  const plants = islandPlants.value.slice(start, end)
  
  // Fill up to itemsPerPage (8) slots
  const slots = [...plants]
  while (slots.length < itemsPerPage) {
    slots.push(null)
  }
  return slots
})

function getIslandPlantsCount(islandId) {
  return floraHistory.value.filter(plant => {
    const assignedIsland = plantIslandMap[plant.name] || 'jawa'
    return assignedIsland === islandId
  }).length
}

const mapTransformStyle = computed(() => {
  return {
    transform: `translate(${mapZoomData.value.x}, ${mapZoomData.value.y}) scale(${mapZoomData.value.scale})`
  }
})

function handleIslandHover(island) {
  hoveredIsland.value = island
  try { soundManager.playHover() } catch(e) {}
}

function selectIsland(island) {
  if (island.isLocked) return // Prevent clicking locked islands
  
  try { soundManager.playClick() } catch(e) {}
  isZooming.value = true
  activeIsland.value = island
  hoveredIsland.value = null
  currentPage.value = 1 // Reset pagination
  
  mapZoomData.value = island.zoomData
  
  setTimeout(() => {
    activeOverlay.value = 'island'
  }, 1000)
}

function openScanner() {
  try { soundManager.playClick() } catch(e) {}
  scanStep.value = 'upload'
  uploadedImageSrc.value = ''
  activeOverlay.value = 'scanner'
}

function closeOverlay() {
  activeOverlay.value = null
  selectedPlantDetail.value = null
  closeCameraStream()
  
  mapZoomData.value = { scale: 1, x: '0%', y: '0%' }
  
  setTimeout(() => {
    isZooming.value = false
    activeIsland.value = null
  }, 800)
}

function viewPlantDetail(plant) {
  try { soundManager.playClick() } catch(e) {}
  selectedPlantDetail.value = {
    ...plant,
    desc: plantDescriptions[plant.name] || 'Spesies menakjubkan dari kepulauan Nusantara yang belum memiliki deskripsi terperinci.'
  }
}

// WebRTC Camera Logic
async function openCamera() {
  try { soundManager.playClick() } catch(e) {}
  
  if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
    alert('Browser Anda tidak mendukung akses kamera secara langsung (Gunakan HTTPS atau localhost). Mengalihkan ke unggah file...');
    if (fileInput.value) fileInput.value.click();
    return;
  }

  scanStep.value = 'camera'
  
  try {
    // Gunakan parameter paling dasar untuk menghindari error pada driver webcam desktop tertentu
    cameraStream = await navigator.mediaDevices.getUserMedia({ video: true })
  } catch(err) {
    scanStep.value = 'upload'
    setTimeout(() => {
      let errorMessage = 'Gagal mengakses kamera. ';
      if (err.name === 'NotAllowedError') {
        errorMessage += 'Izin kamera ditolak oleh browser!\n\nCARA MEMPERBAIKI:\n1. Klik tulisan "Not secure" (atau ikon gembok/info) di sebelah KIRI alamat web (localhost:5173).\n2. Cari bagian "Camera" atau "Kamera".\n3. Ubah dari "Block" menjadi "Allow" (Izinkan).\n4. Refresh halaman ini.';
      } else if (err.name === 'NotFoundError') {
        errorMessage += 'Tidak ada perangkat webcam yang terdeteksi di komputer Anda.';
      } else if (err.name === 'NotReadableError' || err.name === 'TrackStartError') {
        errorMessage += 'Kamera sedang digunakan oleh aplikasi lain (seperti Zoom/Meet) atau terjadi error pada hardware.';
      } else {
        errorMessage += err.message || err.name;
      }
      
      alert(errorMessage + '\n\nMengalihkan ke mode unggah file...');
      if (fileInput.value) fileInput.value.click()
    }, 100)
    return
  }

  setTimeout(() => {
    if (videoElement.value && cameraStream) {
      videoElement.value.srcObject = cameraStream
    }
  }, 100)
}

function closeCameraStream() {
  if (cameraStream) {
    cameraStream.getTracks().forEach(track => track.stop())
    cameraStream = null
  }
}

function closeCamera() {
  try { soundManager.playClick() } catch(e) {}
  closeCameraStream()
  scanStep.value = 'upload'
}

function takePhoto() {
  try { soundManager.playClick() } catch(e) {}
  if (!videoElement.value || !canvasElement.value) return
  
  const video = videoElement.value
  const canvas = canvasElement.value
  canvas.width = video.videoWidth
  canvas.height = video.videoHeight
  canvas.getContext('2d').drawImage(video, 0, 0)
  
  uploadedImageSrc.value = canvas.toDataURL('image/jpeg')
  closeCameraStream()
  
  scanStep.value = 'scanning'
  simulateAnalysis()
}

// Mock Scanning Process
function startScan(event) {
  const file = event.target.files[0]
  if (!file) return

  const reader = new FileReader()
  reader.onload = (e) => {
    uploadedImageSrc.value = e.target.result
    scanStep.value = 'scanning'
    simulateAnalysis()
  }
  reader.readAsDataURL(file)
}

function simulateAnalysis() {
  // Simulate AI Processing
  setTimeout(() => {
    const allPlants = Object.keys(plantIslandMap)
    const randomPlant = allPlants[Math.floor(Math.random() * allPlants.length)]
    const islandId = plantIslandMap[randomPlant] || 'jawa'
    const islandObj = islands.value.find(i => i.id === islandId)
    
    scanResult.value = {
      id: Date.now(),
      name: randomPlant,
      confidence: Math.floor(Math.random() * 15) + 85,
      image: uploadedImageSrc.value,
      islandName: islandObj ? islandObj.name : 'Jawa',
      desc: plantDescriptions[randomPlant] || 'Spesies yang baru teridentifikasi.'
    }
    
    scanStep.value = 'result'
  }, 2500)
}

function playBirdSound() {
  try { soundManager.playBirdChirp() } catch(e) {}
}

function playCloudSound() {
  try { soundManager.playCloudSound() } catch(e) {}
}

function saveScanToHistory() {
  try { soundManager.playClick() } catch(e) {}
  floraHistory.value.unshift({
    id: scanResult.value.id,
    name: scanResult.value.name,
    confidence: scanResult.value.confidence,
    image: scanResult.value.image
  })
  localStorage.setItem('flora_history', JSON.stringify(floraHistory.value))
  closeOverlay()
}

let birdInterval = null;
onMounted(() => {
  // Play bird sound every 10 seconds
  birdInterval = setInterval(() => {
    // Only play if audio context is likely active (i.e. not zooming/busy)
    if (!activeOverlay.value && soundManager.audioCtx && soundManager.audioCtx.state === 'running') {
      playBirdSound();
    }
  }, 10000);
})

onUnmounted(() => {
  if (birdInterval) clearInterval(birdInterval);
})
</script>

<style scoped>
@keyframes scan-line {
  0% { transform: translateY(0); }
  50% { transform: translateY(160px); }
  100% { transform: translateY(0); }
}
.animate-scan-line {
  animation: scan-line 2s linear infinite;
}
</style>
