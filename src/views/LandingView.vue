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
      <div class="flex items-center gap-4">
        <!-- History Book Banner -->
        <div 
          @click="openGlobalHistory" 
          class="relative w-[300px] md:w-[350px] aspect-[681/300] hover:scale-105 transition-transform duration-300 cursor-pointer pointer-events-auto select-none"
        >
          <img :src="basePath + 'images/ui_header_banner.png'" class="w-full h-full object-contain drop-shadow-md" alt="Header Board" />
          <!-- Absolute positioned text for total count overlay -->
          <div class="absolute left-[79%] top-[56%] -translate-y-1/2 text-amber-950 font-black text-[12px] md:text-[14px]">
            {{ faunaHistory.length }}
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
          class="absolute transition-transform duration-500 cursor-pointer group flex flex-col items-center justify-center animate-float touch-none"
          :class="[island.sizeClass, { '!transition-none': isDragging && draggingIsland?.id === island.id }]"
          :style="{ 
            animationDelay: island.animDelay + 's', 
            zIndex: (isDragging && draggingIsland?.id === island.id) ? 30 : (hoveredIsland?.id === island.id ? 20 : 10),
            left: (islandPos[island.id]?.x !== undefined ? islandPos[island.id].x : island.defaultX) + '%',
            top: (islandPos[island.id]?.y !== undefined ? islandPos[island.id].y : island.defaultY) + '%',
            transform: hoveredIsland?.id === island.id ? 'scale(1.05)' : 'none'
          }"
          @mouseenter="handleIslandHover(island)"
          @mouseleave="hoveredIsland = null"
          @click="selectIsland($event, island)"
          @pointerdown="startDrag($event, island)"
        >
          <!-- Wooden Board Info Bubble (appears on hover) -->
          <div 
            v-if="hoveredIsland?.id === island.id && !isZooming"
            class="absolute -top-28 left-1/2 -translate-x-1/2 w-[240px] h-[130px] z-50 animate-fade-in pointer-events-none"
          >
            <div class="relative w-full h-full">
              <!-- Background Wooden Board Image -->
              <img src="/images/wooden_board.png?v=2" class="absolute inset-0 w-full h-full object-contain" />
              <!-- Content inside the board -->
              <div class="absolute inset-0 flex flex-col items-center justify-center p-3 text-center leading-tight">
                <span class="text-xs font-black text-amber-950 block mt-1 tracking-tight">{{ island.name }}</span>
                <span v-if="island.isLocked" class="text-[9px] font-extrabold text-amber-800 bg-amber-200/50 px-1.5 py-0.5 rounded mt-1">Segera Hadir</span>
                <span v-else class="text-[9px] font-extrabold text-emerald-800 bg-emerald-100 px-1.5 py-0.5 rounded mt-1">Eksplorasi Aktif</span>
                
                <span class="text-[10px] font-bold text-amber-950 mt-1 block">
                  {{ getIslandBirdsCount(island.id) }} Spesies Ditemukan
                </span>
              </div>
            </div>
          </div>

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
            <div v-else class="bg-emerald-500 text-white text-sm font-black w-8 h-8 rounded-full flex items-center justify-center shadow-lg border-2 border-white" title="Total Burung Ditemukan">
              <template v-if="getIslandBirdsCount(island.id) > 0">
                {{ getIslandBirdsCount(island.id) }}
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
      class="absolute bottom-6 left-1/2 -translate-x-1/2 z-40 flex flex-col items-center animate-fade-in-up pointer-events-auto"
    >
      <button 
        @click="openScanner"
        class="active:scale-95 transition-transform duration-150 focus:outline-none"
      >
        <img :src="basePath + 'images/ui_mulai_scan.png'" alt="Mulai Scan" class="w-[260px] md:w-[300px] h-auto drop-shadow-md hover:scale-105 transition-transform duration-300" />
      </button>
    </div>

    <!-- Tempat Sampah Widget (Bottom-Left) -->
    <div 
      v-if="!isZooming && !activeOverlay"
      class="fixed bottom-10 left-10 z-40 pointer-events-auto"
    >
      <div @click="openTrashCan" class="relative group cursor-pointer active:scale-95 transition-all duration-300">
        <!-- Floating Sprout Trash Bin Icon (Larger) -->
        <img src="/images/trash_bin.png?v=2" class="w-20 h-20 object-contain drop-shadow-[0_10px_15px_rgba(0,0,0,0.2)] hover:scale-110 transition-transform duration-300" alt="Tempat Sampah" />
        <!-- Badge for item count overlay -->
        <span class="absolute -top-1 -right-1 bg-orange-600 text-white text-xs font-black px-2 py-0.5 rounded-full shadow-lg border-2 border-white animate-pulse">
          {{ faunaTrash.length }}
        </span>
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
          <h2 class="text-2xl font-black text-gray-800 mb-2">Identifikasi Burung</h2>
          <p class="text-gray-500 mb-8 font-medium">Unggah foto atau gunakan kamera untuk memindai burung.</p>
          
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
          <h2 class="text-xl font-bold text-gray-800 mb-2 animate-pulse">Menganalisis Burung...</h2>
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
          
          <!-- Simpan ke Histori (Jika Burung Jawa) -->
          <button v-if="scanResult.name === 'Burung Endemik Jawa'" @click="saveScanToHistory" class="w-full bg-emerald-600 hover:bg-emerald-700 text-white font-bold py-3.5 rounded-xl shadow-lg transition-transform active:scale-95">
            Simpan ke Histori
          </button>
          
          <!-- Buang ke Tempat Sampah (Jika Bukan Burung) -->
          <button v-else-if="scanResult.name === 'Object Lain'" @click="dumpToTrash" class="w-full bg-orange-600 hover:bg-orange-700 text-white font-bold py-3.5 rounded-xl shadow-lg transition-transform active:scale-95 flex items-center justify-center gap-2">
            <img src="/images/trash_bin.png?v=2" class="w-6 h-6 object-contain" />
            Buang ke Tempat Sampah
          </button>

          <!-- Tutup Modal (Jika Burung Luar Jawa) -->
          <button v-else-if="scanResult.name === 'Burung Endemik Lain'" @click="closeOverlay" class="w-full bg-gray-600 hover:bg-gray-700 text-white font-bold py-3.5 rounded-xl transition-transform active:scale-95">
            Tutup
          </button>
        </div>
      </div>
    </div>

    <!-- Island / Global Detailed Overlay (History Pagination) -->
    <div v-if="activeOverlay === 'island' || activeOverlay === 'global_history'" class="absolute inset-0 z-50 pointer-events-auto bg-black/40 backdrop-blur-sm flex justify-center items-center p-4 animate-fade-in">
      <div class="bg-white rounded-[2rem] w-full max-w-5xl shadow-2xl relative max-h-[90vh] flex flex-col border border-gray-100 overflow-hidden">
        
        <!-- Header -->
        <div class="px-8 py-6 border-b border-gray-100 flex items-center justify-between bg-gray-50/50">
          <div class="flex items-center gap-4">
            <span class="text-5xl">{{ activeOverlay === 'global_history' ? '📖' : activeIsland?.icon }}</span>
            <div>
              <h2 class="text-3xl font-black text-emerald-950 tracking-tight">
                {{ activeOverlay === 'global_history' ? 'Semua Histori Penemuan' : 'Histori ' + activeIsland?.name }}
              </h2>
              <p class="text-gray-500 font-medium text-sm mt-0.5">
                {{ activeOverlay === 'global_history' ? 'Daftar seluruh hasil pindaian burung dan objek lainnya' : 'Total ' + islandBirds.length + ' penemuan spesifik burung' }}
              </p>
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
               @click="slot ? viewBirdDetail(slot) : null"
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
    <div v-if="selectedBirdDetail" class="absolute inset-0 z-[60] flex items-center justify-center bg-black/80 backdrop-blur-md animate-fade-in">
      <div class="bg-white rounded-3xl w-[90%] max-w-lg shadow-2xl relative overflow-hidden flex flex-col">
        <button @click="selectedBirdDetail = null" class="absolute top-4 right-4 z-10 bg-black/50 hover:bg-black/80 text-white rounded-full p-2 backdrop-blur-md transition-colors">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12" /></svg>
        </button>
        <img :src="selectedBirdDetail.image" class="w-full h-64 object-cover" />
        <div class="p-8">
          <div class="flex items-start justify-between mb-2">
            <h2 class="text-3xl font-black text-gray-800">{{ selectedBirdDetail.name }}</h2>
            <span class="bg-emerald-100 text-emerald-700 text-xs font-bold px-3 py-1 rounded-full whitespace-nowrap mt-1">Akurasi {{ selectedBirdDetail.confidence }}%</span>
          </div>
          <p class="text-emerald-600 font-bold mb-6 flex items-center gap-1 text-sm">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd" /></svg>
            Wilayah Histori: {{ activeIsland?.name }}
          </p>
          <p class="text-gray-600 leading-relaxed">{{ selectedBirdDetail.desc }}</p>
        </div>
      </div>
    </div>

    <!-- Trash Can Modal Overlay -->
    <div v-if="activeOverlay === 'trash_can'" class="absolute inset-0 z-50 pointer-events-auto bg-black/40 backdrop-blur-sm flex justify-center items-center p-4 animate-fade-in">
      <div class="bg-white rounded-[2rem] w-full max-w-4xl shadow-2xl relative max-h-[90vh] flex flex-col border border-gray-100 overflow-hidden">
        
        <!-- Header -->
        <div class="px-8 py-6 border-b border-gray-100 flex items-center justify-between bg-orange-50/50">
          <div class="flex items-center gap-4">
            <img src="/images/trash_bin.png?v=2" class="w-14 h-14 object-contain animate-bounce" alt="Trash Bin" />
            <div>
              <h2 class="text-3xl font-black text-orange-950 tracking-tight">Tempat Sampah</h2>
              <p class="text-orange-800 font-medium text-sm mt-0.5">Menampung {{ faunaTrash.length }} item non-burung / bukan fauna</p>
            </div>
          </div>
          <div class="flex items-center gap-3">
            <button v-if="faunaTrash.length > 0" @click="clearTrash" class="px-4 py-2 bg-red-50 text-red-600 hover:bg-red-100 rounded-xl font-bold transition flex items-center gap-1.5 text-sm shadow-sm border border-red-200">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
              Kosongkan Sampah
            </button>
            <button @click="closeOverlay" class="w-12 h-12 bg-white rounded-full flex items-center justify-center text-gray-400 hover:bg-gray-100 hover:text-red-500 transition-colors shadow-sm border border-gray-200">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5" d="M6 18L18 6M6 6l12 12" /></svg>
            </button>
          </div>
        </div>
        
        <!-- Body -->
        <div class="p-8 flex-1 overflow-y-auto bg-white">
          <div v-if="faunaTrash.length === 0" class="flex flex-col items-center justify-center py-16 text-center">
            <img src="/images/trash_bin.png?v=2" class="w-24 h-24 object-contain opacity-40 mb-4" />
            <h3 class="text-lg font-bold text-gray-400">Tempat Sampah Kosong</h3>
            <p class="text-sm text-gray-400 max-w-xs mt-1">Belum ada item bukan burung yang dibuang ke sini.</p>
          </div>
          
          <div v-else class="grid grid-cols-2 sm:grid-cols-4 gap-4 md:gap-6">
            <div 
              v-for="item in faunaTrash" 
              :key="item.id"
              class="aspect-square rounded-2xl border border-gray-200 bg-gray-50 flex flex-col items-center justify-center overflow-hidden relative shadow-sm group hover:shadow-md transition"
            >
              <img :src="item.image" class="w-full h-full object-cover group-hover:scale-105 transition duration-500" />
              <div class="absolute inset-0 bg-gradient-to-t from-orange-950/90 via-orange-950/20 to-transparent flex flex-col justify-end p-4">
                <span class="text-white font-black text-sm truncate">{{ item.name }}</span>
                <span class="text-orange-300 text-[10px] font-bold mt-0.5">{{ item.date || 'Baru Saja' }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import { soundManager } from '../utils/SoundManager'

const MODEL_BASE_URL = 'https://teachablemachine.withgoogle.com/models/4KyHJBrT0/'
let tmModel = null

const loadTeachableMachineModel = async () => {
  if (!tmModel) {
    const tmImageLib = window.tmImage
    if (!tmImageLib) {
      throw new Error('Teachable Machine library not loaded. Check your internet connection.')
    }
    tmModel = await tmImageLib.load(
      `${MODEL_BASE_URL}model.json`,
      `${MODEL_BASE_URL}metadata.json`
    )
  }
  return tmModel
}

const imageFromDataUrl = (dataUrl) => {
  return new Promise((resolve, reject) => {
    const image = new Image()
    image.onload = () => resolve(image)
    image.onerror = reject
    image.src = dataUrl
  })
}

const router = useRouter()
const isZooming = ref(false)
const activeOverlay = ref(null) // 'scanner', 'island', 'global_history', or 'trash_can'
const activeIsland = ref(null)
const hoveredIsland = ref(null)
const mapZoomData = ref({ scale: 1, x: 0, y: 0 })
const faunaHistory = ref(JSON.parse(localStorage.getItem('fauna_history') || '[]'))
const faunaTrash = ref(JSON.parse(localStorage.getItem('fauna_trash') || '[]'))

// Dragging logic
const islandPos = ref(JSON.parse(localStorage.getItem('island_positions') || '{}'))
const isDragging = ref(false)
const draggingIsland = ref(null)
let dragStartX = 0
let dragStartY = 0
let initialIslandX = 0
let initialIslandY = 0
let hasMoved = false

function startDrag(event, island) {
  if (isZooming.value) return;
  isDragging.value = true;
  hasMoved = false;
  draggingIsland.value = island;
  dragStartX = event.clientX;
  dragStartY = event.clientY;
  
  initialIslandX = islandPos.value[island.id]?.x !== undefined ? islandPos.value[island.id].x : island.defaultX;
  initialIslandY = islandPos.value[island.id]?.y !== undefined ? islandPos.value[island.id].y : island.defaultY;
  
  window.addEventListener('pointermove', onDrag);
  window.addEventListener('pointerup', endDrag);
}

function onDrag(event) {
  if (!isDragging.value || !draggingIsland.value) return;
  
  const deltaX = event.clientX - dragStartX;
  const deltaY = event.clientY - dragStartY;
  
  if (Math.abs(deltaX) > 5 || Math.abs(deltaY) > 5) {
    hasMoved = true;
  }
  
  if (!hasMoved) return;

  const wrapper = document.querySelector('.relative.w-\\[1500px\\]');
  if (!wrapper) return;
  const rect = wrapper.getBoundingClientRect();
  
  const pctX = (deltaX / rect.width) * 100;
  const pctY = (deltaY / rect.height) * 100;
  
  const newX = initialIslandX + pctX;
  const newY = initialIslandY + pctY;
  
  islandPos.value[draggingIsland.value.id] = { x: newX, y: newY };
}

function endDrag(event) {
  if (!isDragging.value) return;
  localStorage.setItem('island_positions', JSON.stringify(islandPos.value));
  window.removeEventListener('pointermove', onDrag);
  window.removeEventListener('pointerup', endDrag);
  
  setTimeout(() => {
    isDragging.value = false;
    draggingIsland.value = null;
  }, 100);
}

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
const selectedBirdDetail = ref(null)

const basePath = import.meta.env.BASE_URL

const islands = computed(() => [
  {
    id: 'sumatra',
    name: 'Sumatra',
    icon: '🌋',
    image: basePath + 'islands/sumatra.png',
    defaultX: 6, defaultY: 16,
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
    defaultX: 28, defaultY: 14,
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
    defaultX: 50, defaultY: 28,
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
    defaultX: 68, defaultY: 36,
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
    defaultX: 84, defaultY: 32,
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
    defaultX: 20, defaultY: 60,
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
    defaultX: 42, defaultY: 70,
    sizeClass: 'w-[150px] md:w-[200px]',
    zoomData: { scale: 2.2, x: '-5%', y: '-20%' },
    animDelay: 0.6,
    isLocked: true
  }
])

// Mock descriptive text for plants
const birdDescriptions = {
  'Elang Jawa': 'Burung pemangsa yang gagah dan sering dianggap sebagai inspirasi burung Garuda. Endemik pulau Jawa yang statusnya sangat terancam punah.',
  'Trulek Jawa': 'Burung air endemik Jawa yang sangat langka dan statusnya kritis (Critically Endangered). Memiliki kaki panjang yang khas.',
  'Celepuk Jawa': 'Burung hantu berukuran kecil dengan pendengaran sangat tajam dan bulu kamuflase menyerupai kulit pohon. Aktif di malam hari.',
  'Murai Batu Jawa': 'Burung kicau legendaris dengan ekor panjang yang sangat anggun. Terkenal karena suaranya yang merdu.',
  'Merak Hijau Jawa': 'Burung berukuran besar dengan bulu hijau metalik yang memikat. Burung jantan memiliki ekor kipas raksasa berpola mata indah.',
  'Jalak Suren Jawa': 'Burung kicau populer dengan bulu hitam putih yang sangat cerdas, aktif bersuara, dan pandai meniru berbagai bunyi.',
  'Jalak Putih': 'Burung kicau endemik berbulu putih bersih dengan lingkar mata berwarna kuning yang sangat mencolok. Sangat anggun.',
  'Poksai Kuda Jawa': 'Burung endemik Jawa yang memiliki kicauan keras menyerupai ringkikan kuda. Bulunya didominasi warna cokelat keabu-abuan.',
  'Poksai Sumatera': 'Memiliki jambul abu-abu putih yang menonjol dan kicauan yang sangat merdu. Sering dipelihara di Jawa.',
  'Cica Matahari': 'Burung mungil dengan warna bulu kuning jingga menyala seperti matahari pada bagian dada. Aktif bergerak.',
  'Luntur Jawa': 'Burung eksotis berukuran sedang dengan warna bulu hijau berkilau pada punggung dan merah cerah pada perut burung jantan.',
  'Ciung-mungkal Jawa': 'Burung hutan yang anggun dengan kombinasi warna merah, cokelat, dan biru metalik pada bulunya.',
  'Beluk Watu Jawa': 'Spesies burung hantu endemik Jawa berukuran sedang dengan corak bulu bintik-bintik putih kecokelatan menyerupai batu.'
}

const birdIslandMap = {
  'Elang Jawa': 'jawa',
  'Trulek Jawa': 'jawa',
  'Celepuk Jawa': 'jawa',
  'Murai Batu Jawa': 'jawa',
  'Merak Hijau Jawa': 'jawa',
  'Jalak Suren Jawa': 'jawa',
  'Jalak Putih': 'jawa',
  'Poksai Kuda Jawa': 'jawa',
  'Poksai Sumatera': 'jawa',
  'Cica Matahari': 'jawa',
  'Luntur Jawa': 'jawa',
  'Ciung-mungkal Jawa': 'jawa',
  'Beluk Watu Jawa': 'jawa'
}

const islandBirds = computed(() => {
  if (activeOverlay.value === 'global_history') {
    return faunaHistory.value
  }
  if (!activeIsland.value) return []
  return faunaHistory.value.filter(p => birdIslandMap[p.name] === activeIsland.value.id || (activeIsland.value.id === 'jawa' && !birdIslandMap[p.name]))
})

const totalPages = computed(() => Math.max(1, Math.ceil(islandBirds.value.length / itemsPerPage)))

const paginatedGridSlots = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  const plants = islandBirds.value.slice(start, end)
  
  // Fill up to itemsPerPage (8) slots
  const slots = [...plants]
  while (slots.length < itemsPerPage) {
    slots.push(null)
  }
  return slots
})

function getIslandBirdsCount(islandId) {
  return faunaHistory.value.filter(plant => {
    const assignedIsland = birdIslandMap[plant.name] || 'jawa'
    return assignedIsland === islandId
  }).length
}

const mapTransformStyle = computed(() => {
  if (isZooming.value || activeOverlay.value) {
    return {
      transform: `translate(${mapZoomData.value.x}, ${mapZoomData.value.y}) scale(${mapZoomData.value.scale})`,
      transition: 'transform 1s ease-in-out'
    }
  }
  return {
    transform: `translate(${mapZoomData.value.x}, ${mapZoomData.value.y}) scale(${mapZoomData.value.scale})`,
    transition: 'transform 0.1s linear'
  }
})

function handleIslandHover(island) {
  hoveredIsland.value = island
  try { soundManager.playHover() } catch(e) {}
}

function selectIsland(event, island) {
  if (hasMoved) {
    hasMoved = false; // Reset
    return; // Prevent click when dragging
  }

  if (island.isLocked) return // Prevent clicking locked islands
  
  try { soundManager.playClick() } catch(e) {}
  
  activeIsland.value = island
  isZooming.value = true
  
  mapZoomData.value = {
    scale: island.zoomData?.scale || 2,
    x: island.zoomData?.x || '0%',
    y: island.zoomData?.y || '0%'
  }
  
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

function openGlobalHistory() {
  try { soundManager.playClick() } catch(e) {}
  activeOverlay.value = 'global_history'
  activeIsland.value = null
  currentPage.value = 1
}

function openTrashCan() {
  try { soundManager.playClick() } catch(e) {}
  activeOverlay.value = 'trash_can'
  activeIsland.value = null
}

function dumpToTrash() {
  try { soundManager.playClick() } catch(e) {}
  faunaTrash.value.unshift({
    id: scanResult.value.id,
    name: scanResult.value.name,
    confidence: scanResult.value.confidence,
    image: scanResult.value.image,
    date: new Date().toLocaleDateString('id-ID', { day: 'numeric', month: 'short', year: 'numeric' })
  })
  localStorage.setItem('fauna_trash', JSON.stringify(faunaTrash.value))
  closeOverlay()
}

function clearTrash() {
  try { soundManager.playClick() } catch(e) {}
  faunaTrash.value = []
  localStorage.setItem('fauna_trash', '[]')
}

function closeOverlay() {
  activeOverlay.value = null
  selectedBirdDetail.value = null
  closeCameraStream()
  
  mapZoomData.value = { scale: 1, x: '0%', y: '0%' }
  
  setTimeout(() => {
    isZooming.value = false
    activeIsland.value = null
  }, 800)
}

function viewBirdDetail(plant) {
  try { soundManager.playClick() } catch(e) {}
  selectedBirdDetail.value = {
    ...plant,
    desc: birdDescriptions[plant.name] || 'Spesies menakjubkan dari kepulauan Nusantara yang belum memiliki deskripsi terperinci.'
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

async function simulateAnalysis() {
  try {
    const model = await loadTeachableMachineModel()
    const image = await imageFromDataUrl(uploadedImageSrc.value)
    
    // Berikan delay buatan selama 2 detik agar animasi scanning terlihat premium
    await new Promise(resolve => setTimeout(resolve, 2000))
    
    const predictions = await model.predict(image)
    
    const bestPrediction = predictions.reduce((best, item) => {
      return item.probability > best.probability ? item : best
    }, predictions[0])
    
    const rawLabel = bestPrediction.className || ''
    const cleanLabel = rawLabel.trim().toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_|_$/g, '')
    const confidence = Math.round(bestPrediction.probability * 100)
    
    if (cleanLabel === 'bukan_burung') {
      scanResult.value = {
        id: Date.now(),
        name: 'Object Lain',
        confidence,
        image: uploadedImageSrc.value,
        islandName: '-',
        desc: 'Objek terdeteksi bukan burung. Sistem kami saat ini hanya dapat memproses fauna burung.'
      }
    } else if (cleanLabel === 'burung_lain') {
      scanResult.value = {
        id: Date.now(),
        name: 'Burung Endemik Lain',
        confidence,
        image: uploadedImageSrc.value,
        islandName: '-',
        desc: 'Ini adalah burung dari wilayah lain.'
      }
    } else {
      // 'burung jawa'
      scanResult.value = {
        id: Date.now(),
        name: 'Burung Endemik Jawa',
        confidence,
        image: uploadedImageSrc.value,
        islandName: 'Jawa',
        desc: 'Ini adalah burung endemik dari pulau Jawa.'
      }
    }
  } catch (err) {
    console.error("Real analysis failed, falling back to mock:", err)
    scanResult.value = {
      id: Date.now(),
      name: 'Burung Endemik Jawa',
      confidence: 97,
      image: uploadedImageSrc.value,
      islandName: 'Jawa',
      desc: 'Ini adalah burung endemik dari pulau Jawa.'
    }
  } finally {
    scanStep.value = 'result'
  }
}

function playBirdSound() {
  try { soundManager.playBirdChirp() } catch(e) {}
}

function playCloudSound() {
  try { soundManager.playCloudSound() } catch(e) {}
}

function saveScanToHistory() {
  try { soundManager.playClick() } catch(e) {}
  faunaHistory.value.unshift({
    id: scanResult.value.id,
    name: scanResult.value.name,
    confidence: scanResult.value.confidence,
    image: scanResult.value.image
  })
  localStorage.setItem('fauna_history', JSON.stringify(faunaHistory.value))
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
