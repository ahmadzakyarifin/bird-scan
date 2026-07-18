<template>
  <div class="relative w-full h-full min-h-[500px] overflow-hidden rounded-3xl group flex items-end justify-center perspective-[1200px]" ref="containerRef">
    <!-- Background Glow -->
    <div class="absolute inset-0 bg-gradient-to-t from-emerald-900/30 via-transparent to-transparent opacity-50 pointer-events-none"></div>
    <div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[400px] h-[400px] bg-emerald-500/20 blur-[120px] rounded-full pointer-events-none mix-blend-screen"></div>

    <!-- The Plant Image Container -->
    <div 
      ref="plantContainer"
      class="relative z-10 w-full max-w-[500px] cursor-grab active:cursor-grabbing will-change-transform transform-gpu flex justify-center pb-10"
      @pointerdown="onPointerDown"
      style="transform-style: preserve-3d;"
    >
      <img 
        src="/futuristic_plant_cropped.png" 
        alt="Futuristic Plant" 
        class="w-full h-auto object-contain pointer-events-none drop-shadow-[0_25px_35px_rgba(5,150,105,0.4)]"
      />
    </div>

    <!-- Overlay Instructions -->
    <div class="absolute bottom-6 left-1/2 -translate-x-1/2 bg-white/5 backdrop-blur-md px-5 py-3 rounded-full text-xs font-bold text-gray-300 flex items-center gap-2 pointer-events-none opacity-50 group-hover:opacity-100 transition-opacity border border-white/10 shadow-lg z-20">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 15l-2 5L9 9l11 4-5 2zm0 0l5 5M7.188 2.239l.777 2.897M5.136 7.965l-2.898-.777M13.95 4.05l-2.122 2.122m-5.657 5.656l-2.12 2.122" /></svg>
      Geser untuk putar, Tarik ke atas untuk melompat!
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const containerRef = ref(null)
const plantContainer = ref(null)

let isDragging = false
let startY = 0
let startX = 0
let currentY = 0
let currentRotationY = 0
let targetRotationY = 0
let velocityY = 0
const gravity = 1.2
const bounceFactor = 0.6
let lastMouseY = 0
let animationId = null
let idleTime = 0

onMounted(() => {
  window.addEventListener('pointermove', onPointerMove)
  window.addEventListener('pointerup', onPointerUp)
  window.addEventListener('touchmove', onTouchMove, { passive: false })
  window.addEventListener('touchend', onPointerUp)
  
  // Start animation loop
  animate()
})

onBeforeUnmount(() => {
  window.removeEventListener('pointermove', onPointerMove)
  window.removeEventListener('pointerup', onPointerUp)
  window.removeEventListener('touchmove', onTouchMove)
  window.removeEventListener('touchend', onPointerUp)
  if (animationId) cancelAnimationFrame(animationId)
})

function onPointerDown(event) {
  isDragging = true
  startY = event.clientY - currentY
  startX = event.clientX - targetRotationY
  velocityY = 0
  lastMouseY = event.clientY
}

function handleDragMove(clientX, clientY) {
  if (!isDragging) return
  
  // Vertical drag (Pull to jump)
  const newY = clientY - startY
  // Allow pulling up (negative Y) but restrict going below ground (positive Y > 0)
  currentY = Math.min(newY, 0)
  
  // Horizontal drag (Rotate)
  const newX = clientX - startX
  targetRotationY = newX * 0.5 // Scale rotation sensitivity
  
  velocityY = clientY - lastMouseY
  lastMouseY = clientY
}

function onPointerMove(event) {
  handleDragMove(event.clientX, event.clientY)
}

function onTouchMove(event) {
  if (isDragging) {
    event.preventDefault()
    handleDragMove(event.touches[0].clientX, event.touches[0].clientY)
  }
}

function onPointerUp() {
  if (isDragging) {
    isDragging = false
    
    // If flicked up, give momentum, else if just clicked give a jump
    if (velocityY < -2) {
      // momentum is kept
    } else if (currentY < -10) {
      // Just let gravity take it
      velocityY = 0
    } else {
      // Just clicked, make it jump!
      velocityY = -35
    }
  }
}

function animate() {
  animationId = requestAnimationFrame(animate)
  
  if (!isDragging) {
    velocityY += gravity
    currentY += velocityY
    
    // Floor collision
    if (currentY >= 0) {
      currentY = 0
      if (velocityY > 3) {
        velocityY = -velocityY * bounceFactor
      } else {
        velocityY = 0
      }
    }
    
    // Idle Animation
    if (Math.abs(velocityY) < 0.5 && currentY === 0) {
      idleTime += 0.03
      // Pronounced float up and down
      const floatY = Math.sin(idleTime) * 15
      // Sway rotation
      targetRotationY = Math.sin(idleTime * 0.5) * 10
      // Continuous gentle spin/tilt
      const swayZ = Math.sin(idleTime * 0.8) * 2
      
      // Smoothly interpolate rotation to target
      currentRotationY += (targetRotationY - currentRotationY) * 0.1
      
      applyTransform(currentY + floatY, currentRotationY, swayZ)
    } else {
      // While jumping/falling, smoothly return to 0 rotation
      targetRotationY = 0
      currentRotationY += (targetRotationY - currentRotationY) * 0.05
      applyTransform(currentY, currentRotationY, 0)
    }
  } else {
    // While dragging, apply target rotation instantly
    currentRotationY += (targetRotationY - currentRotationY) * 0.2
    applyTransform(currentY, currentRotationY, 0)
  }
}

function applyTransform(y, rotateY, rotateZ) {
  if (plantContainer.value) {
    // Add tilt based on velocity for squash/stretch feel
    let rotateX = isDragging ? (currentY / -5) : velocityY * 0.5
    // Limit rotateX
    rotateX = Math.max(-15, Math.min(15, rotateX))
    
    plantContainer.value.style.transform = `translateY(${y}px) rotateY(${rotateY}deg) rotateZ(${rotateZ}deg) rotateX(${rotateX}deg)`
  }
}
</script>
