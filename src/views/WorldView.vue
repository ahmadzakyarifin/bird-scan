<template>
  <div class="relative w-full h-screen overflow-hidden bg-sky-100">
    <!-- UI Overlay (Appears when camera is at a specific location) -->
    <div 
      v-if="currentLocation" 
      class="absolute top-0 left-0 w-full h-full pointer-events-none z-10 flex flex-col justify-center p-4 md:p-8"
    >
      <!-- Dynamic Overlay Based on Location -->
      <AILabOverlay 
        v-if="currentLocation.id === 'lab'" 
        @close="resetCamera" 
      />
      
      <AviaryOverlay 
        v-else-if="currentLocation.id === 'garden'" 
        :island-id="islandId"
        @close="resetCamera" 
      />
      
      <!-- Generic Overlay for others -->
      <div v-else class="pointer-events-auto bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-2xl max-w-md w-full border border-white/50 mb-8 mx-auto mt-auto transform transition-all duration-500 translate-y-0 opacity-100">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-2xl font-bold text-emerald-900">{{ currentLocation.name }}</h2>
          <button @click="resetCamera" class="w-8 h-8 rounded-full bg-gray-200 hover:bg-gray-300 flex items-center justify-center text-gray-700 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" /></svg>
          </button>
        </div>
        <p class="text-gray-600 mb-6">{{ currentLocation.description }}</p>
        <button class="w-full py-3 bg-emerald-500 hover:bg-emerald-600 text-white rounded-xl font-semibold shadow-lg shadow-emerald-500/30 transition-all active:scale-95">
          {{ currentLocation.actionText }}
        </button>
      </div>
    </div>

    <!-- Back button to map -->
    <button 
      v-if="!currentLocation"
      @click="$router.push('/')" 
      class="absolute top-6 left-6 z-10 px-4 py-2 bg-white/80 backdrop-blur-md rounded-xl text-emerald-800 font-bold shadow-lg flex items-center gap-2 hover:bg-white transition-colors"
    >
      <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" /></svg>
      Kembali ke Peta
    </button>

    <!-- Overlay Instruction -->
    <div v-if="!currentLocation" class="absolute bottom-8 left-1/2 -translate-x-1/2 z-10 flex flex-col items-center pointer-events-none">
      <div class="px-6 py-2 bg-emerald-900/80 backdrop-blur-md text-emerald-100 rounded-full text-xs font-bold uppercase tracking-widest mb-3 border border-emerald-500/30">
        📍 Eksplorasi: {{ islandName }}
      </div>
      <div class="px-6 py-3 bg-black/60 backdrop-blur-sm text-white rounded-full text-sm font-medium animate-pulse border border-white/10 shadow-lg">
        Pilih bangunan Aviary (warna kuning) untuk melihat histori burung
      </div>
    </div>

    <!-- 3D Scene -->
    <TresCanvas clear-color="#87CEEB" window-size>
      <TresPerspectiveCamera 
        ref="cameraRef"
        :position="[0, 10, 15]" 
        :look-at="[0, 0, 0]" 
      />
      
      <!-- Controls -->
      <OrbitControls 
        v-if="!currentLocation"
        :enable-damping="true"
        :damping-factor="0.05"
        :min-distance="5"
        :max-distance="30"
        :max-polar-angle="Math.PI / 2.1"
      />

      <!-- Lighting -->
      <TresAmbientLight :intensity="0.5" />
      <TresDirectionalLight 
        :position="[5, 10, 5]" 
        :intensity="1" 
        cast-shadow
      />

      <!-- Island Base (Procedural Placeholder) -->
      <TresMesh :position="[0, -0.5, 0]" receive-shadow>
        <TresCylinderGeometry :args="[12, 11, 1, 32]" />
        <TresMeshStandardMaterial color="#2d4c1e" />
      </TresMesh>

      <!-- Water Base -->
      <TresMesh :position="[0, -1, 0]">
        <TresPlaneGeometry :args="[100, 100]" />
        <TresMeshStandardMaterial color="#4da6ff" />
      </TresMesh>

      <!-- Buildings -->
      
      <!-- Tree of Life (Using actual 3D model) -->
      <Building
        :position="[0, -0.5, -2]"
        modelPath="/plant.glb"
        :hitboxArgs="[3, 5, 3]"
        @click="() => moveToBuilding('tree')"
      >
        <TresMesh cast-shadow>
          <TresCylinderGeometry :args="[1, 1.5, 4, 16]" />
          <TresMeshStandardMaterial color="#34d399" />
        </TresMesh>
      </Building>

      <!-- AI Lab -->
      <Building
        :position="[-5, 1, 3]"
        :hitboxArgs="[2.5, 2.5, 2.5]"
        @click="() => moveToBuilding('lab')"
      >
        <TresMesh cast-shadow>
          <TresBoxGeometry :args="[2, 2, 2]" />
          <TresMeshStandardMaterial color="#60a5fa" />
        </TresMesh>
      </Building>

      <!-- Botanical Garden -->
      <Building
        :position="[4, 0.5, 4]"
        :hitboxArgs="[3.5, 2, 3.5]"
        @click="() => moveToBuilding('garden')"
      >
        <TresMesh cast-shadow>
          <TresBoxGeometry :args="[3, 1, 3]" />
          <TresMeshStandardMaterial color="#fcd34d" />
        </TresMesh>
      </Building>
      
      <!-- Observatory -->
      <Building
        :position="[-4, 2, -5]"
        :hitboxArgs="[2, 5, 2]"
        @click="() => moveToBuilding('observatory')"
      >
        <TresMesh cast-shadow>
          <TresCylinderGeometry :args="[1, 1, 4, 16]" />
          <TresMeshStandardMaterial color="#f3f4f6" />
        </TresMesh>
      </Building>

      <!-- Museum -->
      <Building
        :position="[5, 1.5, -3]"
        :hitboxArgs="[2.5, 4, 2.5]"
        @click="() => moveToBuilding('museum')"
      >
        <TresMesh cast-shadow>
          <TresBoxGeometry :args="[2, 3, 2]" />
          <TresMeshStandardMaterial color="#c084fc" />
        </TresMesh>
      </Building>

    </TresCanvas>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import { TresCanvas } from '@tresjs/core'
import { OrbitControls } from '@tresjs/cientos'
import gsap from 'gsap'

import AILabOverlay from '../components/AILabOverlay.vue'
import AviaryOverlay from '../components/AviaryOverlay.vue'
import Building from '../components/world/Building.vue'

const route = useRoute()
const islandId = ref(route.query.island || null)

const islandNames = {
  sumatra: 'Pulau Sumatra',
  jawa: 'Pulau Jawa',
  kalimantan: 'Pulau Kalimantan',
  sulawesi: 'Pulau Sulawesi',
  papua: 'Pulau Papua'
}
const islandName = computed(() => islandId.value ? islandNames[islandId.value] || 'Kepulauan Nusantara' : 'Kepulauan Nusantara')

const cameraRef = ref(null)
const currentLocation = ref(null)

const locations = {
  tree: {
    id: 'tree',
    name: "Tree of Life",
    description: "Pohon kehidupan ini tumbuh seiring dengan jumlah spesies burung yang berhasil Anda identifikasi. Semakin banyak pengetahuan, semakin rindang pohon ini.",
    actionText: "Lihat Progress",
    camPos: [0, 5, 4],
    lookAt: [0, 2, -2]
  },
  lab: {
    id: 'lab',
    name: "AI Laboratory",
    description: "Pusat penelitian canggih tempat AI menganalisis burung yang Anda temukan di alam liar.",
    actionText: "Upload & Scan Foto",
    camPos: [-5, 3, 7],
    lookAt: [-5, 1, 3]
  },
  garden: {
    id: 'garden',
    name: "Aviary Konservasi",
    description: "Koleksi digital dari semua burung yang telah Anda temukan di pulau ini. Aviary ini adalah bukti perjalanan ekspedisi Anda.",
    actionText: "Lihat Koleksi Burung",
    camPos: [4, 3, 8],
    lookAt: [4, 0.5, 4]
  },
  observatory: {
    id: 'observatory',
    name: "Observatory",
    description: "Menara pantau untuk melihat peta persebaran avifauna di seluruh penjuru kepulauan Nusantara.",
    actionText: "Buka Peta Indonesia",
    camPos: [-4, 5, -1],
    lookAt: [-4, 2, -5]
  },
  museum: {
    id: 'museum',
    name: "Museum Fauna",
    description: "Ensiklopedia interaktif yang menyimpan data lengkap tentang setiap spesies burung yang teridentifikasi.",
    actionText: "Buka Ensiklopedia",
    camPos: [5, 4, 1],
    lookAt: [5, 1.5, -3]
  }
}

// Default camera state
const defaultCamPos = [0, 10, 15]
const defaultLookAt = [0, 0, 0]

function moveToBuilding(id) {
  const loc = locations[id]
  if (!loc || !cameraRef.value) return
  
  currentLocation.value = loc
  
  // We need to animate both position and the camera's lookAt target
  const camera = cameraRef.value
  
  gsap.to(camera.position, {
    x: loc.camPos[0],
    y: loc.camPos[1],
    z: loc.camPos[2],
    duration: 1.5,
    ease: "power2.inOut",
    onUpdate: () => {
      camera.lookAt(loc.lookAt[0], loc.lookAt[1], loc.lookAt[2])
    }
  })
}

function resetCamera() {
  currentLocation.value = null
  const camera = cameraRef.value
  
  gsap.to(camera.position, {
    x: defaultCamPos[0],
    y: defaultCamPos[1],
    z: defaultCamPos[2],
    duration: 1.5,
    ease: "power2.inOut",
    onUpdate: () => {
      camera.lookAt(defaultLookAt[0], defaultLookAt[1], defaultLookAt[2])
    }
  })
}
</script>
