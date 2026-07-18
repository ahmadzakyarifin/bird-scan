<template>
  <div class="w-full h-full min-h-[500px] relative overflow-hidden rounded-3xl group" ref="containerRef">
    <!-- Dark/Light Mode aware background is handled by CSS here -->
    <div class="absolute inset-0 bg-gradient-to-t from-emerald-900/20 via-transparent to-transparent pointer-events-none transition-colors duration-500" :class="{'from-emerald-900/40': isDark}"></div>
    
    <div class="absolute inset-0 flex items-center justify-center pointer-events-none z-10" v-if="isLoading">
      <div class="px-4 py-2 bg-black/50 text-emerald-400 rounded-full backdrop-blur-sm text-xs font-bold animate-pulse">
        Memuat Model 3D...
      </div>
    </div>

    <!-- 3D Canvas -->
    <canvas ref="canvasRef" class="w-full h-full block touch-none cursor-grab active:cursor-grabbing"></canvas>

    <!-- Overlay Instructions -->
    <div class="absolute bottom-6 left-1/2 -translate-x-1/2 bg-white/5 backdrop-blur-md px-5 py-3 rounded-full text-xs font-bold text-gray-300 flex items-center gap-2 pointer-events-none opacity-50 group-hover:opacity-100 transition-opacity border border-white/10 shadow-lg z-20">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122" /></svg>
      Putar dari segala sisi, Tarik ke atas untuk melompat!
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount, watch } from 'vue'
import * as THREE from 'three'
import { OrbitControls } from 'three/addons/controls/OrbitControls.js'
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js'

const containerRef = ref(null)
const canvasRef = ref(null)
const isDark = ref(document.documentElement.classList.contains('dark'))
const isLoading = ref(true)

let scene, camera, renderer, controls
let plantGroup = new THREE.Group()
let animationId

// Physics State
let isDragging = false
let dragStartY = 0
let currentY = 0
let velocityY = 0
const gravity = 0.08
const bounceFactor = 0.6
const pointer = new THREE.Vector2()
const raycaster = new THREE.Raycaster()
let dragPlane = new THREE.Plane(new THREE.Vector3(0, 0, 1), 0)

onMounted(() => {
  initThree()
  loadModel()
  createEnvironment()
  animate()
  window.addEventListener('resize', onWindowResize)
  
  // Observe dark mode changes
  const observer = new MutationObserver(() => {
    isDark.value = document.documentElement.classList.contains('dark')
    updateTheme(isDark.value)
  })
  observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] })
})

onBeforeUnmount(() => {
  window.removeEventListener('resize', onWindowResize)
  if (animationId) cancelAnimationFrame(animationId)
  if (renderer) renderer.dispose()
})

function initThree() {
  scene = new THREE.Scene()
  // Transparent background for cinematic blending
  scene.background = null 
  
  // Fog matches the bg
  scene.fog = new THREE.FogExp2(0x050505, 0.03)

  camera = new THREE.PerspectiveCamera(45, containerRef.value.clientWidth / containerRef.value.clientHeight, 0.1, 100)
  camera.position.set(0, 4, 12)

  renderer = new THREE.WebGLRenderer({ 
    canvas: canvasRef.value, 
    antialias: true,
    alpha: true 
  })
  renderer.setSize(containerRef.value.clientWidth, containerRef.value.clientHeight)
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
  renderer.shadowMap.enabled = true
  renderer.shadowMap.type = THREE.PCFSoftShadowMap

  // Controls
  controls = new OrbitControls(camera, renderer.domElement)
  controls.enableDamping = true
  controls.dampingFactor = 0.05
  controls.enablePan = false
  controls.minDistance = 5
  controls.maxDistance = 20
  controls.maxPolarAngle = Math.PI / 2 + 0.1 // Allow looking slightly below

  // Lighting
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.6)
  scene.add(ambientLight)

  const dirLight = new THREE.DirectionalLight(0xffffff, 1.5)
  dirLight.position.set(5, 10, 7)
  dirLight.castShadow = true
  dirLight.shadow.mapSize.width = 1024
  dirLight.shadow.mapSize.height = 1024
  scene.add(dirLight)
  
  const fillLight = new THREE.DirectionalLight(0xaaddff, 0.5)
  fillLight.position.set(-5, 3, -5)
  scene.add(fillLight)

  // Drag Events
  canvasRef.value.addEventListener('pointerdown', onPointerDown)
  window.addEventListener('pointermove', onPointerMove)
  window.addEventListener('pointerup', onPointerUp)
}

function loadModel() {
  scene.add(plantGroup)
  const loader = new GLTFLoader()
  
  // Try loading a custom GLB if the user placed it in public/
  loader.load('/plant.glb', (gltf) => {
    isLoading.value = false
    const model = gltf.scene
    
    // Auto-scale and center the model
    const box = new THREE.Box3().setFromObject(model)
    const size = box.getSize(new THREE.Vector3()).length()
    const center = box.getCenter(new THREE.Vector3())
    
    model.position.x += (model.position.x - center.x)
    model.position.y += (model.position.y - center.y) + (box.max.y - box.min.y)/2 // sit on ground
    model.position.z += (model.position.z - center.z)
    
    const scale = 5 / size
    model.scale.setScalar(scale)
    
    model.traverse((child) => {
      if (child.isMesh) {
        child.castShadow = true
        child.receiveShadow = true
      }
    })
    
    plantGroup.add(model)
  }, undefined, (error) => {
    // Fallback if no plant.glb exists: create a procedural plant
    console.log("No custom /plant.glb found. Showing fallback procedural plant.")
    isLoading.value = false
    createProceduralFallback()
  })
}

function createProceduralFallback() {
  // Pot
  const potGeo = new THREE.CylinderGeometry(1.2, 0.9, 1.5, 32)
  const potMat = new THREE.MeshStandardMaterial({ 
    color: 0x222222, 
    roughness: 0.2, 
    metalness: 0.8 
  })
  const pot = new THREE.Mesh(potGeo, potMat)
  pot.position.y = 0.75
  pot.castShadow = true
  pot.receiveShadow = true
  plantGroup.add(pot)

  // Leaves
  const leafGeo = new THREE.ConeGeometry(0.8, 3, 4)
  leafGeo.translate(0, 1.5, 0) // move origin to bottom
  const leafMat = new THREE.MeshStandardMaterial({ 
    color: 0x10b981, 
    roughness: 0.4 
  })
  
  for(let i=0; i<5; i++) {
    const leaf = new THREE.Mesh(leafGeo, leafMat)
    leaf.position.y = 1.4
    leaf.rotation.x = Math.random() * 0.5 + 0.2
    leaf.rotation.y = (i / 5) * Math.PI * 2
    leaf.rotation.z = (Math.random() - 0.5) * 0.2
    leaf.castShadow = true
    plantGroup.add(leaf)
  }
}

function createEnvironment() {
  // Ground
  const grid = new THREE.GridHelper(20, 20, 0x10b981, 0x333333)
  grid.material.opacity = 0.2
  grid.material.transparent = true
  scene.add(grid)
  
  const groundGeo = new THREE.PlaneGeometry(50, 50)
  const groundMat = new THREE.MeshStandardMaterial({ 
    color: 0x050505,
    roughness: 0.1,
    metalness: 0.5
  })
  const ground = new THREE.Mesh(groundGeo, groundMat)
  ground.rotation.x = -Math.PI / 2
  ground.position.y = 0
  ground.receiveShadow = true
  scene.add(ground)
  
  // Floating Particles
  const partGeo = new THREE.BufferGeometry()
  const partCount = 50
  const posArray = new Float32Array(partCount * 3)
  for(let i=0; i<partCount*3; i++) {
    posArray[i] = (Math.random() - 0.5) * 15
    if(i%3 === 1) posArray[i] = Math.random() * 10 // Y always positive
  }
  partGeo.setAttribute('position', new THREE.BufferAttribute(posArray, 3))
  const partMat = new THREE.PointsMaterial({
    size: 0.05,
    color: 0x34d399,
    transparent: true,
    opacity: 0.6,
    blending: THREE.AdditiveBlending
  })
  const particles = new THREE.Points(partGeo, partMat)
  scene.add(particles)
}

function updateTheme(dark) {
  scene.fog.color.setHex(dark ? 0x050505 : 0xf9fafb)
  // Ensure ground matches theme
  scene.children.forEach(c => {
    if(c.isMesh && c.geometry.type === 'PlaneGeometry') {
      c.material.color.setHex(dark ? 0x050505 : 0xffffff)
    }
  })
}

// Interactive Physics
function onPointerDown(event) {
  const rect = canvasRef.value.getBoundingClientRect()
  pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1
  pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1

  raycaster.setFromCamera(pointer, camera)
  const intersects = raycaster.intersectObject(plantGroup, true)

  if (intersects.length > 0) {
    isDragging = true
    controls.enabled = false // disable orbit while dragging
    
    // Calculate intersection with drag plane
    dragPlane.setFromNormalAndCoplanarPoint(camera.getWorldDirection(new THREE.Vector3()), plantGroup.position)
    raycaster.ray.intersectPlane(dragPlane, pointer)
    dragStartY = pointer.y - currentY
    velocityY = 0
  }
}

function onPointerMove(event) {
  if (!isDragging) return
  
  const rect = canvasRef.value.getBoundingClientRect()
  pointer.x = ((event.clientX - rect.left) / rect.width) * 2 - 1
  pointer.y = -((event.clientY - rect.top) / rect.height) * 2 + 1

  raycaster.setFromCamera(pointer, camera)
  const intersectPoint = new THREE.Vector3()
  raycaster.ray.intersectPlane(dragPlane, intersectPoint)
  
  const newY = intersectPoint.y - dragStartY
  currentY = Math.max(0, newY) // Don't allow dragging below ground
  
  // Estimate velocity based on movement
  velocityY = (currentY - plantGroup.position.y) * 0.5
}

function onPointerUp() {
  if (isDragging) {
    isDragging = false
    controls.enabled = true
    // If just clicked (no movement), give it a jump
    if (currentY < 0.1 && Math.abs(velocityY) < 0.1) {
      velocityY = 1.5
    }
  }
}

function animate() {
  animationId = requestAnimationFrame(animate)
  controls.update()
  
  if (!isDragging) {
    velocityY -= gravity
    currentY += velocityY
    
    if (currentY <= 0) {
      currentY = 0
      if (velocityY < -0.2) {
        velocityY = -velocityY * bounceFactor
        // Squash effect
        plantGroup.scale.y = 0.7
        plantGroup.scale.x = 1.15
        plantGroup.scale.z = 1.15
      } else {
        velocityY = 0
      }
    }
  }
  
  // Smoothly recover scale from squash
  plantGroup.scale.lerp(new THREE.Vector3(1,1,1), 0.15)
  plantGroup.position.y = currentY
  
  // Subtle idle breathing animation when resting
  if (!isDragging && currentY === 0 && Math.abs(velocityY) < 0.1) {
    const time = Date.now() * 0.002
    plantGroup.scale.y = 1 + Math.sin(time) * 0.02
    plantGroup.scale.x = 1 - Math.sin(time) * 0.01
    plantGroup.scale.z = 1 - Math.sin(time) * 0.01
  }

  // Rotate particles
  scene.children.forEach(c => {
    if(c.isPoints) c.rotation.y += 0.001
  })

  renderer.render(scene, camera)
}

function onWindowResize() {
  if (!containerRef.value || !camera || !renderer) return
  camera.aspect = containerRef.value.clientWidth / containerRef.value.clientHeight
  camera.updateProjectionMatrix()
  renderer.setSize(containerRef.value.clientWidth, containerRef.value.clientHeight)
}
</script>
