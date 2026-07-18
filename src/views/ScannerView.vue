<template>
  <div class="min-h-screen bg-white dark:bg-[#0a0a0a] transition-colors duration-300 flex flex-col font-sans text-gray-900 dark:text-gray-100">
    <!-- App Launch Splash -->
    <div
      v-if="isSplashVisible"
      class="fixed inset-0 z-50 flex flex-col items-center justify-center bg-emerald-700 text-white px-8 animate-splash-out" style="z-index: 70;"
    >
      <div class="relative mb-7">
        <div class="absolute inset-0 rounded-3xl bg-white/25 blur-xl animate-pulse"></div>
        <div class="relative w-24 h-24 rounded-3xl bg-white text-emerald-700 shadow-2xl flex items-center justify-center">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-14 w-14" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M12 21c-4.5-4.5-7-8.2-7-11.2A7 7 0 0112 3a7 7 0 017 6.8c0 3-2.5 6.7-7 11.2z" />
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M9.5 10.5c2.6 0 4.4-1.4 5-4 1.2 1.5 1.7 3.3 1.3 5.2-.5 2.4-2.4 4.3-5 4.7" />
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.8" d="M8 16c2.2-2.8 4.5-4.7 7-5.8" />
          </svg>
        </div>
      </div>

      <h1 class="text-3xl font-extrabold tracking-normal leading-tight">FloraScan</h1>
      <p class="text-sm text-emerald-50/90 font-medium mt-2 text-center">{{ $t('app.subtitle') }}</p>

      <div class="w-44 h-1.5 bg-white/25 rounded-full mt-8 overflow-hidden">
        <div class="h-full bg-white rounded-full animate-splash-progress"></div>
      </div>
    </div>
	    
    <!-- Top Navbar -->
    <header class="sticky top-0 z-40 h-16 bg-white dark:bg-[#0a0a0a] border-b border-gray-200 dark:border-gray-800 flex items-center justify-between px-4 md:px-8 shadow-sm">
      <!-- Logo & Title -->
      <div class="flex items-center gap-3">
        <router-link to="/" class="p-2 mr-1 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 transition flex items-center justify-center">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
          </svg>
        </router-link>
        <!-- Plant Icon Logo -->
        <div class="w-10 h-10 bg-emerald-100 dark:bg-emerald-900/40 rounded flex items-center justify-center text-emerald-600 dark:text-emerald-400 shadow-sm">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
        </div>
        <div class="min-w-0">
          <div class="flex flex-col justify-center">
            <h1 class="text-base md:text-xl font-bold tracking-tight leading-tight truncate">{{ $t('app.title') }}</h1>
            <p class="text-[10px] md:text-xs text-gray-500 dark:text-gray-400 font-medium mt-0.5 truncate">{{ $t('app.subtitle') }}</p>
          </div>
        </div>
      </div>

      <!-- Header Controls -->
      <div class="flex items-center gap-1.5 md:gap-3 shrink-0">
        <!-- Install PWA Button -->
        <button v-if="showInstallButton" @click="installApp" class="flex items-center gap-1.5 text-xs font-bold px-3 py-2 rounded bg-emerald-600 text-white hover:bg-emerald-700 transition shadow-sm h-9">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
          </svg>
          <span>{{ $t('pwa.install_button') }}</span>
        </button>
        
        <!-- Dataset Info Button -->
        <button @click="openDatasetModal" class="flex items-center gap-1.5 text-xs font-bold px-3 py-2 rounded bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-emerald-100 hover:text-emerald-700 dark:hover:bg-emerald-900/40 dark:hover:text-emerald-400 transition border border-gray-200 dark:border-gray-700 h-9">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <span class="hidden md:inline">Info Dataset</span>
        </button>
        
        <!-- Lang Toggle -->
        <button @click="toggleLang" class="flex items-center justify-center text-xs font-bold px-3 py-2 rounded bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700 transition border border-gray-200 dark:border-gray-700 h-9">
          {{ currentLang.toUpperCase() }}
        </button>
        
        <!-- Theme Toggle -->
        <button @click="toggleTheme" class="flex items-center justify-center px-3 py-2 rounded bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 hover:bg-gray-200 dark:hover:bg-gray-700 transition border border-gray-200 dark:border-gray-700 h-9">
          <svg v-if="isDark" xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-yellow-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
          </svg>
          <svg v-else xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-gray-700" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z" />
          </svg>
        </button>
      </div>
    </header>

    <!-- Main Content Area -->
    <main class="grow w-full max-w-5xl mx-auto p-4 md:p-8 flex flex-col gap-8">
      
      <!-- Stacked Layout: Camera & Result -->
      <div class="flex flex-col gap-8">
        
        <!-- TOP PANEL: Camera Section -->
        <section class="w-full flex flex-col gap-4">
          <div class="relative w-full aspect-video min-h-[350px] flex items-center justify-center bg-gray-100/50 dark:bg-gray-900/50 rounded-xl overflow-hidden shadow-sm border border-gray-200 dark:border-gray-800 group">
            
            <!-- Live Camera Video Element -->
            <video 
              ref="videoElement" 
              class="w-full h-full object-cover absolute inset-0 z-10" 
              :class="{'hidden': !isCameraActive || isCaptured}"
              autoplay 
              muted
              playsinline>
            </video>

            <!-- Captured Image Preview -->
            <img 
              v-if="isCaptured && capturedImage" 
              :src="capturedImage" 
              class="w-full h-full object-cover absolute inset-0 z-10" 
              alt="Captured" 
            />

            <!-- Overlay when Camera is OFF -->
            <div v-if="!isCameraActive && !isCaptured" class="text-center p-6 z-20 flex flex-col items-center animate-fade-in">
              <div class="w-20 h-20 bg-white dark:bg-gray-800 rounded-full flex items-center justify-center mb-4 shadow-sm border border-gray-100 dark:border-gray-700 text-emerald-500">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M15 13a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
              </div>
              <p class="text-sm text-gray-500 dark:text-gray-400 mb-6 max-w-xs">{{ $t('camera.instruction') }}</p>
              <div class="flex flex-col gap-3">
                <button @click="startCamera" class="px-6 py-2.5 bg-emerald-600 text-white hover:bg-emerald-700 rounded-lg font-semibold shadow-sm transition-colors flex items-center justify-center gap-2 w-[220px]">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 9a2 2 0 012-2h.93a2 2 0 001.664-.89l.812-1.22A2 2 0 0110.07 4h3.86a2 2 0 011.664.89l.812 1.22A2 2 0 0018.07 7H19a2 2 0 012 2v9a2 2 0 01-2 2H5a2 2 0 01-2-2V9z" />
                  </svg>
                  {{ $t('camera.start') }}
                </button>
                <input type="file" ref="fileInput" accept="image/jpeg, image/png, image/webp" class="hidden" @change="handleFileUpload" />
                <button @click="$refs.fileInput.click()" class="px-6 py-2.5 bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-300 border border-gray-200 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-700 rounded-lg font-semibold shadow-sm transition-colors flex items-center justify-center gap-2 w-[220px]">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" />
                  </svg>
                  Upload File
                </button>
              </div>
            </div>

            <!-- Loading Overlay (AI Style) -->
            <div v-if="isAnalyzing" class="absolute inset-0 bg-gray-900/90 flex flex-col items-center justify-center backdrop-blur-md z-30 overflow-hidden">
              <!-- Scanner Line -->
              <div class="absolute inset-0 w-full h-1 bg-emerald-400/60 shadow-[0_0_20px_rgba(52,211,153,0.8)] animate-scan-line blur-[1px]"></div>
              
              <!-- AI Spinner -->
              <div class="relative w-24 h-24 mb-6 flex items-center justify-center">
                <div class="absolute inset-0 border border-emerald-500/30 rounded-full animate-ping opacity-75"></div>
                <div class="absolute inset-2 border-2 border-t-emerald-400 border-r-emerald-500 border-b-transparent border-l-transparent rounded-full animate-spin" style="animation-duration: 1.5s;"></div>
                <div class="absolute inset-5 border-2 border-b-emerald-300 border-l-emerald-400 border-t-transparent border-r-transparent rounded-full animate-spin direction-reverse" style="animation-duration: 2s;"></div>
                <div class="w-3 h-3 bg-emerald-400 rounded-full shadow-[0_0_15px_rgba(52,211,153,1)] animate-pulse"></div>
              </div>
              
              <p class="text-emerald-400 font-bold tracking-[0.3em] uppercase text-xs animate-pulse drop-shadow-[0_0_8px_rgba(52,211,153,0.8)]">
                {{ $t('camera.analyzing') || 'ANALYZING...' }}
              </p>
            </div>
          </div>

          <!-- Camera Controls -->
          <div class="flex gap-3 justify-center" v-if="isCameraActive || isCaptured">
            <template v-if="isCameraActive && !isCaptured">
              <button @click="stopCamera" class="px-4 py-3 bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-200 border border-gray-200 dark:border-gray-700 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 font-semibold w-[160px] flex items-center justify-center text-sm transition">
                {{ $t('camera.stop') }}
              </button>
              <button @click="captureImage" class="px-4 py-3 bg-emerald-600 text-white hover:bg-emerald-700 rounded-lg font-semibold shadow-sm w-[160px] flex items-center justify-center text-sm transition">
                {{ $t('camera.capture') }}
              </button>
            </template>
            
            <template v-if="isCaptured && showResult">
              <button @click="retakePhoto" class="px-4 py-3 bg-white dark:bg-gray-800 text-gray-700 dark:text-gray-200 border border-gray-200 dark:border-gray-700 rounded-lg hover:bg-gray-50 dark:hover:bg-gray-700 font-semibold w-[160px] flex items-center justify-center text-sm transition">
                {{ $t('camera.retake') }}
              </button>
              <button @click="saveCurrentResultToHistory" class="px-4 py-3 bg-emerald-600 text-white hover:bg-emerald-700 rounded-lg font-semibold shadow-sm w-[160px] flex items-center justify-center text-sm transition">
                {{ $t('camera.save_history') }}
              </button>
            </template>
          </div>
          <div v-if="cameraError" class="mt-1 text-center">
            <p class="text-red-500 text-sm font-semibold">{{ cameraError }}</p>
            <p class="text-xs text-red-400 dark:text-red-300 mt-1 max-w-xl mx-auto leading-relaxed">
              {{ $t('camera.permission_hint') }}
            </p>
          </div>
        </section>

        <!-- BOTTOM PANEL: Results Section -->
        <section class="w-full flex flex-col" id="result-section">
          <div class="bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 rounded-xl p-8 grow flex flex-col shadow-sm">
            <h2 class="text-xs uppercase tracking-widest text-gray-400 dark:text-gray-500 font-bold mb-6 pb-3 border-b border-gray-100 dark:border-gray-800">
              {{ $t('result.title') }}
            </h2>
            
            <!-- Empty State -->
            <div v-if="!showResult" class="grow flex flex-col items-center justify-center text-center opacity-60">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-14 w-14 text-gray-300 dark:text-gray-700 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
              </svg>
              <p class="text-sm font-semibold text-gray-500 dark:text-gray-400">{{ $t('result.waiting') }}</p>
              <p class="text-xs text-gray-400 dark:text-gray-600 mt-2 max-w-[200px]">{{ $t('result.empty_desc') }}</p>
            </div>

            <!-- Result State -->
            <div v-if="showResult && currentResult" class="grow animate-fade-in flex flex-col">
              <div class="flex justify-between items-start mb-6">
                <div>
                  <h3 class="text-3xl md:text-4xl font-extrabold text-gray-900 dark:text-white tracking-tight mb-2">{{ currentResult.name }}</h3>
                  <p class="text-sm font-medium text-gray-500 dark:text-gray-400 flex items-center gap-2">
                    <span class="inline-block w-2 h-2 rounded-full bg-emerald-500"></span>
                    {{ $t('result.family') }}: {{ currentResult.family }}
                  </p>
                </div>
                <div class="text-right flex flex-col items-end shrink-0 ml-4">
                  <span class="inline-flex items-center justify-center px-3 py-1.5 bg-emerald-50 dark:bg-emerald-900/30 text-emerald-700 dark:text-emerald-400 text-sm font-bold rounded-md border border-emerald-200 dark:border-emerald-800/50">
                    {{ currentResult.confidence }}% MATCH
                  </span>
                  <p class="text-[9px] text-gray-400 dark:text-gray-500 mt-2 uppercase font-bold tracking-widest">{{ $t('result.confidence') }}</p>
                </div>
              </div>
              
              <div class="mt-auto grid grid-cols-1 md:grid-cols-2 gap-5">
                <div class="bg-white dark:bg-gray-900 p-5 rounded-xl border border-gray-200 dark:border-gray-800 md:col-span-2 shadow-sm flex flex-col justify-start">
                  <h4 class="text-xs font-bold text-gray-800 dark:text-gray-200 uppercase tracking-widest mb-3 flex items-center gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-emerald-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    {{ $t('result.description') }}
                  </h4>
                  <div class="flex flex-wrap gap-2 mb-3">
                    <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-400 text-[10px] font-bold uppercase tracking-wider border border-blue-100 dark:border-blue-800/30">
                      💧 {{ currentLang === 'id' ? currentResult.water_id : currentResult.water_en }}
                    </span>
                    <span class="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-md bg-amber-50 dark:bg-amber-900/20 text-amber-700 dark:text-amber-400 text-[10px] font-bold uppercase tracking-wider border border-amber-100 dark:border-amber-800/30">
                      ☀️ {{ currentLang === 'id' ? currentResult.sun_id : currentResult.sun_en }}
                    </span>
                  </div>
                  <p class="text-sm text-gray-600 dark:text-gray-300 leading-relaxed">
                    {{ currentLang === 'id' ? currentResult.description_id : currentResult.description_en }}
                  </p>
                </div>
                
                <div class="bg-white dark:bg-gray-900 p-5 rounded-xl border border-gray-200 dark:border-gray-800 shadow-sm flex flex-col justify-start">
                  <h4 class="text-xs font-bold text-emerald-600 dark:text-emerald-400 uppercase tracking-widest mb-3 flex items-center gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
                    </svg>
                    {{ currentLang === 'id' ? 'Panduan Perawatan' : 'Care Guide' }}
                  </h4>
                  <p class="text-sm text-gray-600 dark:text-gray-300 leading-relaxed font-medium">
                    {{ currentLang === 'id' ? currentResult.care_guide_id : currentResult.care_guide_en }}
                  </p>
                </div>

                <div class="bg-white dark:bg-gray-900 p-5 rounded-xl border border-gray-200 dark:border-gray-800 shadow-sm flex flex-col justify-start">
                  <h4 class="text-xs font-bold text-red-600 dark:text-red-400 uppercase tracking-widest mb-3 flex items-center gap-2">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                    </svg>
                    {{ currentLang === 'id' ? 'Peringatan Racun' : 'Toxicity' }}
                  </h4>
                  <p class="text-sm text-gray-600 dark:text-gray-300 leading-relaxed font-medium">
                    {{ currentLang === 'id' ? currentResult.toxicity_id : currentResult.toxicity_en }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </section>
      </div>

      <!-- History Data Table Section -->
      <section class="mt-8 animate-fade-in border-t border-gray-200 dark:border-gray-800 pt-8">
        
        <div class="flex flex-col sm:flex-row sm:items-center justify-between mb-6 gap-4">
          <h2 class="text-lg md:text-xl font-bold text-gray-900 dark:text-white flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 text-gray-400 shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16" />
            </svg>
            {{ $t('history.title') }}
          </h2>
          <div class="flex items-center gap-2 md:gap-3 self-end sm:self-auto">
            <button @click="exportToCSV" class="flex items-center gap-2 text-xs font-bold px-4 py-2 rounded-lg bg-emerald-600 text-white hover:bg-emerald-700 transition shadow-sm">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
              Export CSV
            </button>
            <span class="text-xs font-bold text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-800 px-3 py-1.5 rounded-md border border-gray-200 dark:border-gray-700 shadow-sm">{{ scanHistory.length }} {{ $t('history.total') }}</span>
          </div>
        </div>
        
        <div class="bg-white dark:bg-gray-900 border border-gray-200 dark:border-gray-800 rounded-xl shadow-sm overflow-hidden flex flex-col min-h-[420px]">
          
          <!-- Table Container -->
          <div class="overflow-x-auto grow flex flex-col w-full">
            <table class="w-full min-w-[550px] text-left border-collapse table-fixed" v-if="scanHistory.length > 0">
              <thead>
                <tr class="bg-gray-50 dark:bg-gray-950/50 text-[10px] uppercase tracking-widest text-gray-500 border-b border-gray-200 dark:border-gray-800">
                  <th class="py-4 px-6 font-bold w-[35%]">{{ $t('history.col_plant') }}</th>
                  <th class="py-4 px-6 font-bold w-[20%]">{{ $t('history.col_accuracy') }}</th>
                  <th class="py-4 px-6 font-bold w-[25%]">{{ $t('history.col_time') }}</th>
                  <th class="py-4 px-6 font-bold text-right w-[20%]">{{ $t('history.col_action') }}</th>
                </tr>
              </thead>
              <tbody>
                <!-- Data Rows (Padded to strictly 5) -->
                <tr v-for="(item, index) in paddedHistory" :key="item.id || ('empty-' + index)" class="border-b border-gray-100 dark:border-gray-800/50 h-[76px]" :class="{'hover:bg-gray-50 dark:hover:bg-gray-800/30 transition-colors': !item.isEmpty}">
                  <template v-if="!item.isEmpty">
                    <td class="py-3 px-6">
                      <div class="flex items-center gap-4">
                        <div class="w-12 h-12 rounded-lg overflow-hidden shrink-0 border border-gray-200 dark:border-gray-700 bg-gray-100 dark:bg-gray-800">
                          <img :src="item.image" class="w-full h-full object-cover" alt="Thumb" />
                        </div>
                        <div>
                          <p class="font-bold text-gray-900 dark:text-white">{{ item.name }}</p>
                          <p class="text-[10px] text-gray-500 uppercase tracking-wider mt-0.5">{{ item.family }}</p>
                        </div>
                      </div>
                    </td>
                    <td class="py-3 px-6">
                      <span class="text-sm font-bold text-emerald-600 dark:text-emerald-400">
                        {{ item.confidence }}%
                      </span>
                    </td>
                    <td class="py-3 px-6 text-sm text-gray-600 dark:text-gray-400 font-medium">
                      {{ item.date }}<br>
                      <span class="text-xs text-gray-400 dark:text-gray-500">{{ item.time }}</span>
                    </td>
                    <td class="py-3 px-6 text-right">
                      <div class="flex items-center justify-end gap-2">
                        <!-- View Details Button -->
                        <button @click="openModal(item)" class="p-2 text-gray-400 hover:text-emerald-600 hover:bg-emerald-50 dark:hover:text-emerald-400 dark:hover:bg-emerald-900/30 rounded-lg transition" :title="$t('history.btn_detail')">
                          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                          </svg>
                        </button>
                        <!-- Delete Button -->
                        <button @click="confirmDeleteHistory(item.id)" class="p-2 text-gray-400 hover:text-red-600 hover:bg-red-50 dark:hover:text-red-400 dark:hover:bg-red-900/30 rounded-lg transition" :title="$t('history.btn_delete')">
                          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                          </svg>
                        </button>
                      </div>
                    </td>
                  </template>
                  <template v-else>
                    <td class="py-3 px-6" colspan="4"></td>
                  </template>
                </tr>
              </tbody>
            </table>
            
            <!-- Centered Empty State -->
            <div v-if="scanHistory.length === 0" class="grow flex flex-col items-center justify-center text-gray-500 dark:text-gray-400 py-16">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-16 w-16 text-gray-300 dark:text-gray-700 mb-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
              </svg>
              <p class="font-bold text-lg text-gray-700 dark:text-gray-300">{{ $t('history.empty_title') }}</p>
              <p class="text-sm mt-1">{{ $t('history.empty_desc') }}</p>
            </div>
          </div>

          <!-- Pagination Footer -->
          <div v-show="scanHistory.length > 0" class="mt-auto border-t border-gray-200 dark:border-gray-800 px-4 md:px-6 py-4 flex flex-col sm:flex-row items-center justify-between gap-4 bg-gray-50 dark:bg-gray-900 shrink-0">
            <span class="text-sm text-gray-500 dark:text-gray-400">
              {{ $t('history.page') }} <span class="font-bold text-gray-900 dark:text-white">{{ currentPage }}</span> {{ $t('history.of') }} <span class="font-bold text-gray-900 dark:text-white">{{ totalPages }}</span>
            </span>
            <div class="flex items-center gap-2">
              <button 
                @click="prevPage" 
                :disabled="currentPage === 1"
                class="px-3 py-1.5 border border-gray-200 dark:border-gray-700 rounded-md text-sm font-medium text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 disabled:opacity-50 disabled:cursor-not-allowed transition w-[100px] flex justify-center"
              >
                {{ $t('history.prev') }}
              </button>
              <button 
                @click="nextPage" 
                :disabled="currentPage === totalPages"
                class="px-3 py-1.5 border border-gray-200 dark:border-gray-700 rounded-md text-sm font-medium text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 disabled:opacity-50 disabled:cursor-not-allowed transition w-[100px] flex justify-center"
              >
                {{ $t('history.next') }}
              </button>
            </div>
          </div>
        </div>
      </section>

    </main>
    
    <!-- Footer -->
    <footer class="mt-auto border-t border-gray-200 dark:border-gray-800/50 bg-white dark:bg-gray-900">
      <div class="max-w-7xl mx-auto px-6 py-5">
        <p class="text-[10px] md:text-xs uppercase tracking-widest text-gray-400 dark:text-gray-500 font-bold text-center">
          {{ $t('footer.edu_note') }}
        </p>
      </div>
    </footer>

    <!-- Hidden Canvas for capturing frames -->
    <canvas ref="canvasElement" class="hidden"></canvas>

    <!-- INSTALL APP MODAL -->
    <div v-if="isInstallModalOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div @click="closeInstallModal" class="absolute inset-0 bg-gray-900/60 dark:bg-black/70 backdrop-blur-sm transition-opacity"></div>

      <div class="relative bg-white dark:bg-gray-900 rounded-2xl shadow-2xl w-full max-w-sm overflow-hidden flex flex-col animate-fade-in border border-gray-200 dark:border-gray-800">
        <div class="flex items-center justify-between p-5 border-b border-gray-100 dark:border-gray-800">
          <h3 class="font-bold text-lg text-gray-900 dark:text-white flex items-center gap-2">
            <span class="w-8 h-8 bg-emerald-100 dark:bg-emerald-900/40 rounded flex items-center justify-center text-emerald-600 dark:text-emerald-400">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
            </span>
            {{ $t('pwa.modal_title') }}
          </h3>
          <button @click="closeInstallModal" class="p-1.5 text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 transition">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <div class="p-6">
          <p class="text-sm text-gray-600 dark:text-gray-300 leading-relaxed mb-5">
            {{ $t('pwa.modal_desc') }}
          </p>
          <ol class="space-y-3">
            <li v-for="(stepKey, index) in installStepKeys" :key="stepKey" class="flex gap-3 text-sm text-gray-700 dark:text-gray-300">
              <span class="shrink-0 w-6 h-6 rounded bg-emerald-100 dark:bg-emerald-900/40 text-emerald-700 dark:text-emerald-300 font-bold flex items-center justify-center text-xs">
                {{ index + 1 }}
              </span>
              <span>{{ $t(stepKey) }}</span>
            </li>
          </ol>
        </div>

        <div class="p-4 border-t border-gray-100 dark:border-gray-800 bg-gray-50 dark:bg-gray-950 text-right">
          <button @click="closeInstallModal" class="px-5 py-2 bg-emerald-600 text-white font-semibold rounded-lg hover:bg-emerald-700 transition">
            {{ $t('app.dataset_close') }}
          </button>
        </div>
      </div>
    </div>

    <!-- DETAIL MODAL (CRUD - Read & Update Notes) -->
    <div v-if="isModalOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4 sm:p-6">
      <!-- Backdrop -->
      <div @click="closeModal" class="absolute inset-0 bg-gray-900/60 dark:bg-black/70 backdrop-blur-sm transition-opacity"></div>
      
      <!-- Modal Content -->
      <div class="relative bg-white dark:bg-gray-900 rounded-2xl shadow-2xl w-full max-w-2xl max-h-[90vh] overflow-hidden flex flex-col animate-fade-in border border-gray-200 dark:border-gray-800">
        
        <!-- Modal Header -->
        <div class="flex items-center justify-between p-5 border-b border-gray-100 dark:border-gray-800">
          <h3 class="font-bold text-lg text-gray-900 dark:text-white">{{ $t('modal.title') }}</h3>
          <button @click="closeModal" class="p-1.5 text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 transition">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <!-- Modal Body (Scrollable) -->
        <div class="p-6 overflow-y-auto grow">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Full Image -->
            <div>
              <div class="w-full aspect-4/3 rounded-xl overflow-hidden border border-gray-200 dark:border-gray-700 bg-gray-100 dark:bg-gray-800">
                <img :src="selectedItem.image" class="w-full h-full object-cover" alt="Detail Image" />
              </div>
              <p class="text-xs text-gray-500 mt-3 text-center">{{ $t('modal.scanned_at') }} {{ selectedItem.date }} {{ selectedItem.time }}</p>
            </div>
            
            <!-- Analysis Details -->
            <div class="flex flex-col gap-5">
              <div>
                <p class="text-[10px] text-gray-500 uppercase tracking-widest font-bold mb-1">{{ $t('modal.result_title') }}</p>
                <h2 class="text-3xl font-extrabold text-gray-900 dark:text-white leading-tight mb-2">{{ selectedItem.name }}</h2>
                <p class="text-sm font-medium text-gray-500 dark:text-gray-400 flex items-center gap-2">
                  <span class="inline-block w-2 h-2 rounded-full bg-emerald-500"></span>
                  {{ $t('modal.family') }}: {{ selectedItem.family }}
                </p>
              </div>
              
              <div>
                <p class="text-[10px] text-gray-500 uppercase tracking-widest font-bold mb-1">{{ $t('modal.accuracy_title') }}</p>
                <span class="inline-flex items-center px-3 py-1.5 bg-emerald-50 dark:bg-emerald-900/30 text-emerald-700 dark:text-emerald-400 text-sm font-bold rounded-md border border-emerald-200 dark:border-emerald-800/50">
                  {{ selectedItem.confidence }}% Match
                </span>
              </div>
              
              <!-- Plant Description & Details -->
              <div class="mt-2 grid grid-cols-1 gap-4">
                <div class="p-5 bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 shadow-sm">
                  <h4 class="text-[10px] font-bold text-gray-800 dark:text-gray-200 uppercase tracking-widest mb-3 flex items-center gap-1.5">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5 text-emerald-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    {{ currentLang === 'id' ? 'Deskripsi Botani' : 'Botanical Description' }}
                  </h4>
                  <div class="flex flex-wrap gap-2 mb-3" v-if="selectedItem.water_id || selectedItem.water_en || selectedItem.sun_id || selectedItem.sun_en">
                    <span v-if="selectedItem.water_id || selectedItem.water_en" class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-md bg-blue-50 dark:bg-blue-900/20 text-blue-700 dark:text-blue-400 text-[9px] font-bold uppercase tracking-wider border border-blue-100 dark:border-blue-800/30">
                      💧 {{ currentLang === 'id' ? (selectedItem.water_id || selectedItem.water_en) : selectedItem.water_en }}
                    </span>
                    <span v-if="selectedItem.sun_id || selectedItem.sun_en" class="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-md bg-amber-50 dark:bg-amber-900/20 text-amber-700 dark:text-amber-400 text-[9px] font-bold uppercase tracking-wider border border-amber-100 dark:border-amber-800/30">
                      ☀️ {{ currentLang === 'id' ? (selectedItem.sun_id || selectedItem.sun_en) : selectedItem.sun_en }}
                    </span>
                  </div>
                  <p class="text-sm text-gray-600 dark:text-gray-300 leading-relaxed">
                    {{ currentLang === 'id' ? (selectedItem.description_id || selectedItem.description || 'Data tidak tersedia.') : (selectedItem.description_en || selectedItem.description || 'Data not available.') }}
                  </p>
                </div>
                
                <div class="p-5 bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 shadow-sm">
                  <h4 class="text-[10px] font-bold text-emerald-600 dark:text-emerald-400 uppercase tracking-widest mb-3 flex items-center gap-1.5">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 3v1m0 16v1m9-9h-1M4 12H3m15.364 6.364l-.707-.707M6.343 6.343l-.707-.707m12.728 0l-.707.707M6.343 17.657l-.707.707M16 12a4 4 0 11-8 0 4 4 0 018 0z" />
                    </svg>
                    {{ currentLang === 'id' ? 'Panduan Perawatan' : 'Care Guide' }}
                  </h4>
                  <p class="text-sm text-gray-600 dark:text-gray-300 leading-relaxed font-medium">
                    {{ currentLang === 'id' ? (selectedItem.care_guide_id || selectedItem.care_guide || 'Data tidak tersedia.') : (selectedItem.care_guide_en || selectedItem.care_guide || 'Data not available.') }}
                  </p>
                </div>

                <div class="p-5 bg-white dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 shadow-sm">
                  <h4 class="text-[10px] font-bold text-red-600 dark:text-red-400 uppercase tracking-widest mb-3 flex items-center gap-1.5">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-3.5 w-3.5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
                    </svg>
                    {{ currentLang === 'id' ? 'Peringatan Racun' : 'Toxicity' }}
                  </h4>
                  <p class="text-sm text-gray-600 dark:text-gray-300 leading-relaxed font-medium">
                    {{ currentLang === 'id' ? (selectedItem.toxicity_id || selectedItem.toxicity || 'Data tidak tersedia.') : (selectedItem.toxicity_en || selectedItem.toxicity || 'Data not available.') }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- DELETE CONFIRMATION MODAL -->
    <div v-if="isDeleteModalOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div @click="cancelDelete" class="absolute inset-0 bg-gray-900/60 dark:bg-black/70 backdrop-blur-sm transition-opacity"></div>
      
      <div class="relative bg-white dark:bg-gray-900 rounded-2xl shadow-2xl w-full max-w-sm overflow-hidden flex flex-col animate-fade-in border border-gray-200 dark:border-gray-800 p-6 text-center">
        <div class="mx-auto flex items-center justify-center h-12 w-12 rounded-full bg-red-100 dark:bg-red-900/30 mb-4">
          <svg class="h-6 w-6 text-red-600 dark:text-red-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
          </svg>
        </div>
        <h3 class="text-lg font-bold text-gray-900 dark:text-white mb-2">{{ $t('history.delete_title') }}</h3>
        <p class="text-sm text-gray-500 dark:text-gray-400 mb-6">{{ $t('history.delete_desc') }}</p>
        
        <div class="flex gap-3 w-full">
          <button @click="cancelDelete" class="w-full px-4 py-2.5 bg-gray-100 dark:bg-gray-800 text-gray-700 dark:text-gray-300 font-semibold rounded-lg hover:bg-gray-200 dark:hover:bg-gray-700 transition">
            {{ $t('history.cancel') }}
          </button>
          <button @click="executeDelete" class="w-full px-4 py-2.5 bg-red-600 text-white font-semibold rounded-lg hover:bg-red-700 transition shadow-sm">
            {{ $t('history.delete_confirm') }}
          </button>
        </div>
      </div>
    </div>

    <!-- DATASET INFO MODAL -->
    <div v-if="isDatasetModalOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div @click="closeDatasetModal" class="absolute inset-0 bg-gray-900/60 dark:bg-black/70 backdrop-blur-sm transition-opacity"></div>
      
      <div class="relative bg-white dark:bg-gray-900 rounded-2xl shadow-2xl w-full max-w-lg max-h-[80vh] flex flex-col animate-fade-in border border-gray-200 dark:border-gray-800 overflow-hidden">
        <div class="flex items-center justify-between p-5 border-b border-gray-100 dark:border-gray-800">
          <h3 class="font-bold text-lg text-gray-900 dark:text-white flex items-center gap-2">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-emerald-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 002-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
            </svg>
            {{ $t('app.dataset_title') }}
          </h3>
          <button @click="closeDatasetModal" class="p-1.5 text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 rounded-full hover:bg-gray-100 dark:hover:bg-gray-800 transition">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        
        <div class="p-6 overflow-y-auto grow">
          <p class="text-sm text-gray-600 dark:text-gray-300 mb-6 leading-relaxed">
            {{ $t('app.dataset_desc') }}
          </p>
          
          <div class="grid grid-cols-2 sm:grid-cols-3 gap-3">
            <div v-for="(plant, index) in datasetPlants" :key="index" class="bg-gray-50 dark:bg-gray-950 border border-gray-200 dark:border-gray-800 rounded-lg p-3 text-center">
              <span class="block text-sm font-bold text-gray-900 dark:text-white">{{ plant.name }}</span>
              <span class="block text-[10px] text-gray-500 uppercase tracking-wider mt-1">{{ plant.family }}</span>
            </div>
          </div>
        </div>
        
        <div class="p-4 border-t border-gray-100 dark:border-gray-800 bg-gray-50 dark:bg-gray-950 text-right">
          <button @click="closeDatasetModal" class="px-5 py-2 bg-emerald-600 text-white font-semibold rounded-lg hover:bg-emerald-700 transition">
            {{ $t('app.dataset_close') }}
          </button>
        </div>
      </div>
    </div>
    
  </div>
</template>

<script setup>
import { ref, computed, onMounted, onBeforeUnmount } from 'vue'
import { useI18n } from 'vue-i18n'
import plantsData from '../data/plants_info.json'

const { t, locale } = useI18n()
const MODEL_BASE_URL = 'https://teachablemachine.withgoogle.com/models/GMWNtuX0_/'

// Global Layout State
const isDark = ref(false)
const currentLang = ref(locale.value)
const isSplashVisible = ref(!sessionStorage.getItem('splashShown'))
let splashTimer = null

// Camera & Analysis State
const videoElement = ref(null)
const canvasElement = ref(null)
const fileInput = ref(null)
const isCameraActive = ref(false)
const isCaptured = ref(false)
const capturedImage = ref(null)
const isAnalyzing = ref(false)
const showResult = ref(false)
const cameraError = ref('')
let stream = null
let tmModel = null

// Current Analysis Result
const currentResult = ref(null)

// History State (CRUD)
const scanHistory = ref([])

// Pagination State
const currentPage = ref(1)
const itemsPerPage = 5

// Modal State
const isModalOpen = ref(false)
const selectedItem = ref(null)

// Delete Modal State
const isDeleteModalOpen = ref(false)
const itemToDelete = ref(null)

// Dataset Modal State
const isDatasetModalOpen = ref(false)
const datasetPlants = computed(() => Object.values(plantsData))

// PWA Install State
const deferredPrompt = ref(null)
const isInstallModalOpen = ref(false)
const isAppInstalled = ref(false)
let beforeInstallPromptHandler = null
let appInstalledHandler = null

const isStandaloneApp = () => {
  return window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone === true
}

const showInstallButton = computed(() => !isAppInstalled.value)

const installStepKeys = computed(() => {
  const userAgent = window.navigator.userAgent.toLowerCase()

  if (/iphone|ipad|ipod/.test(userAgent)) {
    return ['pwa.ios_step1', 'pwa.ios_step2', 'pwa.ios_step3']
  }

  if (/android/.test(userAgent)) {
    return ['pwa.android_step1', 'pwa.android_step2', 'pwa.android_step3']
  }

  return ['pwa.desktop_step1', 'pwa.desktop_step2', 'pwa.desktop_step3']
})

const installApp = async () => {
  if (!deferredPrompt.value) {
    isInstallModalOpen.value = true
    return
  }

  deferredPrompt.value.prompt()
  const { outcome } = await deferredPrompt.value.userChoice
  if (outcome === 'accepted') {
    isAppInstalled.value = true
  }
  deferredPrompt.value = null
}

const closeInstallModal = () => {
  isInstallModalOpen.value = false
}

// Initialization
onMounted(() => {
  isDark.value = document.body.classList.contains('dark')
  isAppInstalled.value = isStandaloneApp()
  if (isSplashVisible.value) {
    splashTimer = window.setTimeout(() => {
      isSplashVisible.value = false
      sessionStorage.setItem('splashShown', 'true')
    }, 1500)
  }
  
  // Load history from local storage
  const savedHistory = localStorage.getItem('flora_history')
  if (savedHistory) {
    scanHistory.value = JSON.parse(savedHistory)
  }
  
  // PWA Prompt Listener
  beforeInstallPromptHandler = (e) => {
    e.preventDefault()
    deferredPrompt.value = e
  }
  window.addEventListener('beforeinstallprompt', beforeInstallPromptHandler)

  appInstalledHandler = () => {
    deferredPrompt.value = null
    isAppInstalled.value = true
    isInstallModalOpen.value = false
  }
  window.addEventListener('appinstalled', appInstalledHandler)
})

onBeforeUnmount(() => {
  if (splashTimer) {
    window.clearTimeout(splashTimer)
  }
  if (beforeInstallPromptHandler) {
    window.removeEventListener('beforeinstallprompt', beforeInstallPromptHandler)
  }
  if (appInstalledHandler) {
    window.removeEventListener('appinstalled', appInstalledHandler)
  }
  stopCamera()
})

// UI Handlers
const toggleTheme = () => {
  isDark.value = !isDark.value
  if (isDark.value) {
    document.body.classList.add('dark')
    localStorage.setItem('theme', 'dark')
  } else {
    document.body.classList.remove('dark')
    localStorage.setItem('theme', 'light')
  }
}

const toggleLang = () => {
  const newLang = currentLang.value === 'id' ? 'en' : 'id'
  currentLang.value = newLang
  locale.value = newLang
  localStorage.setItem('flora_lang', newLang)
}

// ==============================
// CAMERA LOGIC
// ==============================
const startCamera = async () => {
  cameraError.value = ''
  try {
    if (!navigator.mediaDevices?.getUserMedia) {
      cameraError.value = t('camera.unsupported')
      return
    }

    stream = await navigator.mediaDevices.getUserMedia({ 
      video: { facingMode: 'environment' }
    })
    
    if (videoElement.value) {
      videoElement.value.srcObject = stream
      videoElement.value.play().catch(e => console.error("Play error:", e))
      isCameraActive.value = true
      isCaptured.value = false
      showResult.value = false
    }
  } catch (err) {
    console.error("Error accessing camera: ", err)
    if (err?.name === 'NotFoundError' || err?.name === 'DevicesNotFoundError') {
      cameraError.value = t('camera.no_device')
      return
    }

    cameraError.value = t('camera.permission_denied')
  }
}

const stopCamera = () => {
  if (stream) {
    stream.getTracks().forEach(track => track.stop())
    stream = null
  }
  isCameraActive.value = false
}

const captureImage = () => {
  if (!videoElement.value || !canvasElement.value) return
  
  const video = videoElement.value
  const canvas = canvasElement.value
  
  canvas.width = video.videoWidth
  canvas.height = video.videoHeight
  
  const ctx = canvas.getContext('2d')
  ctx.drawImage(video, 0, 0, canvas.width, canvas.height)
  
  capturedImage.value = canvas.toDataURL('image/jpeg', 0.9)
  
  isCaptured.value = true
  stopCamera()
  
  analyzeImage()
}

const retakePhoto = () => {
  isCaptured.value = false
  capturedImage.value = null
  showResult.value = false
  currentResult.value = null
  startCamera()
}

const loadTeachableMachineModel = async () => {
  if (!tmModel) {
    // Use tmImage loaded from CDN (index.html script tags)
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

const normalizeLabel = (label) => {
  return label.trim().toLowerCase().replace(/[^a-z0-9]+/g, '_').replace(/^_|_$/g, '')
}

const plantKeyByLabel = {
  syngonium: 'syngonium',
  sansevieria: 'sansevieria',
  philodendron: 'philodendron',
  monstera: 'monstera',
  hoya: 'hoya',
  ficus: 'ficus',
  epipremnum: 'epipremnum',
  dieffenbachia: 'dieffenbachia',
  calathea: 'calathea',
  caladium: 'caladium',
  aglaonema: 'aglaonema',
  anthurium: 'anthurium',
  begonia: 'begonia',
  peperomia: 'peperomia',
  alocasia: 'alocasia'
}

const titleFromLabel = (label) => {
  return label.trim().replace(/_/g, ' ')
}

const fallbackPlantInfo = (label) => {
  const cleanLabel = titleFromLabel(label)
  const isNotPlant = normalizeLabel(label) === 'not_plant'
  const isOtherPlant = normalizeLabel(label) === 'tanaman_lain'
  const name = isNotPlant
    ? (currentLang.value === 'id' ? 'Bukan Tanaman' : 'Not a Plant')
    : cleanLabel

  return {
    name,
    family: isOtherPlant ? 'Tanaman lain' : '-',
    water_id: 'Data belum tersedia',
    water_en: 'Data not available',
    sun_id: 'Data belum tersedia',
    sun_en: 'Data not available',
    description_id: isNotPlant
      ? 'Gambar tidak terdeteksi sebagai tanaman dari dataset FloraScan.'
      : `Model mengenali gambar sebagai ${cleanLabel}, tetapi detail botani untuk label ini belum tersedia di database FloraScan.`,
    description_en: isNotPlant
      ? 'The image was not detected as a plant from the FloraScan dataset.'
      : `The model recognized this image as ${cleanLabel}, but botanical details for this label are not available in the FloraScan database yet.`,
    care_guide_id: 'Belum ada panduan perawatan untuk label ini.',
    care_guide_en: 'No care guide is available for this label yet.',
    toxicity_id: 'Data toksisitas belum tersedia.',
    toxicity_en: 'Toxicity data is not available yet.'
  }
}

const buildAnalysisResult = (plant, confidence) => {
  const now = new Date()

  return {
    id: Date.now().toString(),
    name: plant.name,
    family: plant.family,
    water_en: plant.water_en,
    water_id: plant.water_id,
    sun_en: plant.sun_en,
    sun_id: plant.sun_id,
    description_en: plant.description_en,
    description_id: plant.description_id,
    care_guide_en: plant.care_guide_en,
    care_guide_id: plant.care_guide_id,
    toxicity_en: plant.toxicity_en,
    toxicity_id: plant.toxicity_id,
    confidence,
    image: capturedImage.value,
    date: now.toLocaleDateString('id-ID', { day: 'numeric', month: 'short', year: 'numeric' }),
    time: now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
    note: ''
  }
}

const analyzeImage = async () => {
  isAnalyzing.value = true
  showResult.value = false

  try {
    const model = await loadTeachableMachineModel()
    const image = await imageFromDataUrl(capturedImage.value)
    const predictions = await model.predict(image)
    const bestPrediction = predictions.reduce((best, item) => {
      return item.probability > best.probability ? item : best
    }, predictions[0])
    const label = bestPrediction.className
    const plantKey = plantKeyByLabel[normalizeLabel(label)]
    const plant = plantKey ? plantsData[plantKey] : fallbackPlantInfo(label)
    const confidence = (bestPrediction.probability * 100).toFixed(1)

    currentResult.value = buildAnalysisResult(plant, confidence)
    showResult.value = true
  } catch (err) {
    console.error("Error analyzing image: ", err)
    cameraError.value = t('camera.analysis_failed')
  } finally {
    isAnalyzing.value = false
  }
}

const emit = defineEmits(['close', 'scan-success'])

const saveCurrentResultToHistory = () => {
  if (currentResult.value) {
    addToHistory({...currentResult.value})
    
    // Emit event so LandingView can catch it and add to island
    emit('scan-success', currentResult.value)
    
    // Hide current result to force taking a new photo
    showResult.value = false
    isCaptured.value = false
    currentResult.value = null
    startCamera()
  }
}

const handleFileUpload = (event) => {
  const file = event.target.files[0]
  if (!file) return
  
  const reader = new FileReader()
  reader.onload = (e) => {
    capturedImage.value = e.target.result
    isCaptured.value = true
    isCameraActive.value = false // Ensure camera is hidden
    
    // Reset input so the same file can be selected again
    if (fileInput.value) fileInput.value.value = ''
    
    analyzeImage()
  }
  reader.readAsDataURL(file)
}

// ==============================
// CRUD & PAGINATION LOGIC
// ==============================

// Create
const addToHistory = (item) => {
  scanHistory.value.unshift(item)
  // Ensure we go back to page 1 to see the new item
  currentPage.value = 1
  saveHistoryToLocal()
}

// Read (Pagination Computed)
const totalPages = computed(() => {
  return Math.max(1, Math.ceil(scanHistory.value.length / itemsPerPage))
})

const paginatedHistory = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage
  const end = start + itemsPerPage
  return scanHistory.value.slice(start, end)
})

const paddedHistory = computed(() => {
  const items = [...paginatedHistory.value]
  if (scanHistory.value.length === 0) return items // If empty, let empty state show
  while(items.length < itemsPerPage) {
    items.push({ isEmpty: true })
  }
  return items
})

const prevPage = () => {
  if (currentPage.value > 1) currentPage.value--
}

const nextPage = () => {
  if (currentPage.value < totalPages.value) currentPage.value++
}

// Read (Modal Detail)
const openModal = (item) => {
  selectedItem.value = item
  isModalOpen.value = true
  document.body.style.overflow = 'hidden' // Prevent bg scroll
}

const closeModal = () => {
  isModalOpen.value = false
  selectedItem.value = null
  document.body.style.overflow = 'auto'
}

// Delete Flow
const confirmDeleteHistory = (id) => {
  itemToDelete.value = id
  isDeleteModalOpen.value = true
}

const executeDelete = () => {
  if (itemToDelete.value) {
    scanHistory.value = scanHistory.value.filter(item => item.id !== itemToDelete.value)
    
    if (paginatedHistory.value.length === 0 && currentPage.value > 1) {
      currentPage.value--
    }
    
    saveHistoryToLocal()
    itemToDelete.value = null
    isDeleteModalOpen.value = false
  }
}

const cancelDelete = () => {
  itemToDelete.value = null
  isDeleteModalOpen.value = false
}

// Dataset Info Modal
const openDatasetModal = () => {
  isDatasetModalOpen.value = true
  document.body.style.overflow = 'hidden'
}

const closeDatasetModal = () => {
  isDatasetModalOpen.value = false
  document.body.style.overflow = 'auto'
}

// Persistence
const saveHistoryToLocal = () => {
  localStorage.setItem('flora_history', JSON.stringify(scanHistory.value))
}

// Export Logic
const exportToCSV = () => {
  if (scanHistory.value.length === 0) return
  
  const headers = currentLang.value === 'id' 
    ? ['ID', 'Nama Tanaman', 'Famili', 'Tingkat Akurasi (%)', 'Tanggal', 'Waktu', 'Deskripsi']
    : ['ID', 'Name', 'Family', 'Confidence (%)', 'Date', 'Time', 'Description']
  const rows = scanHistory.value.map(item => {
    const descId = item.description_id || item.description || ''
    const descEn = item.description_en || item.description || ''
    const desc = currentLang.value === 'id' ? descId : descEn
    return [
      item.id,
      `"${item.name || ''}"`,
      `"${item.family || ''}"`,
      item.confidence || '',
      `"${item.date || ''}"`,
      `"${item.time || ''}"`,
      `"${desc.replace(/"/g, '""')}"`
    ]
  })
  
  const csvContent = [
    headers.join(','),
    ...rows.map(row => row.join(','))
  ].join('\n')
  
  const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' })
  const url = URL.createObjectURL(blob)
  const link = document.createElement('a')
  link.setAttribute('href', url)
  link.setAttribute('download', `florascan_history_${new Date().getTime()}.csv`)
  document.body.appendChild(link)
  link.click()
  document.body.removeChild(link)
}

</script>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.3s ease-out forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes scanLine {
  0% { transform: translateY(-100%); }
  50% { transform: translateY(200%); }
  100% { transform: translateY(-100%); }
}
@keyframes splashProgress {
  from { width: 0%; }
  to { width: 100%; }
}
@keyframes splashOut {
  0%, 72% {
    opacity: 1;
    transform: scale(1);
  }
  100% {
    opacity: 0;
    transform: scale(1.02);
  }
}
.animate-scan-line {
  animation: scanLine 3s ease-in-out infinite;
}
.animate-splash-progress {
  animation: splashProgress 1.35s ease-out forwards;
}
.animate-splash-out {
  animation: splashOut 1.5s ease forwards;
}
.direction-reverse {
  animation-direction: reverse;
}
</style>
