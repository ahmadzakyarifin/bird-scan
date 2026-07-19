import re
import os

with open('src/views/LandingView.vue', 'r') as f:
    content = f.read()

# 1. Add @mousemove to the root div
content = content.replace(
    '<div class="relative w-full h-screen bg-gradient-to-b from-sky-200 via-sky-100 to-[#f8fafc] overflow-hidden font-sans selection:bg-emerald-500/30">',
    '<div class="relative w-full h-screen bg-gradient-to-b from-sky-200 via-sky-100 to-[#f8fafc] overflow-hidden font-sans selection:bg-emerald-500/30" @mousemove="onMouseMove">'
)

# 2. Add translateZ to islands
style_target = """          :style="{ 
            animationDelay: island.animDelay + 's', 
            zIndex: (isDragging && draggingIsland?.id === island.id) ? 30 : (hoveredIsland?.id === island.id ? 20 : 10),
            left: (islandPos[island.id]?.x !== undefined ? islandPos[island.id].x : island.defaultX) + '%',
            top: (islandPos[island.id]?.y !== undefined ? islandPos[island.id].y : island.defaultY) + '%'
          }""""
style_new = """          :style="{ 
            animationDelay: island.animDelay + 's', 
            zIndex: (isDragging && draggingIsland?.id === island.id) ? 30 : (hoveredIsland?.id === island.id ? 20 : 10),
            left: (islandPos[island.id]?.x !== undefined ? islandPos[island.id].x : island.defaultX) + '%',
            top: (islandPos[island.id]?.y !== undefined ? islandPos[island.id].y : island.defaultY) + '%',
            transform: hoveredIsland?.id === island.id ? 'translateZ(60px) scale(1.05)' : 'translateZ(20px)'
          }""""
content = content.replace(style_target, style_new)

# Make wrapper preserve-3d
wrapper_old = """      <!-- The Archipelago Wrapper -->
      <div class="relative w-[1500px] h-[800px] max-w-full max-h-full scale-50 md:scale-75 lg:scale-100 mt-10">"""
wrapper_new = """      <!-- The Archipelago Wrapper -->
      <div class="relative w-[1500px] h-[800px] max-w-full max-h-full scale-50 md:scale-75 lg:scale-100 mt-10" style="transform-style: preserve-3d;">"""
content = content.replace(wrapper_old, wrapper_new)

# 3. Import useRouter
if "import { useRouter } from 'vue-router'" not in content:
    content = content.replace("import { soundManager } from '../utils/SoundManager'", "import { soundManager } from '../utils/SoundManager'\nimport { useRouter } from 'vue-router'")

if "const router = useRouter()" not in content:
    content = content.replace("const isZooming = ref(false)", "const router = useRouter()\nconst isZooming = ref(false)")

# 4. Modify mapTransformStyle and add onMouseMove
map_style_old = """const mapTransformStyle = computed(() => {
  return {
    transform: `translate(${mapZoomData.value.x}, ${mapZoomData.value.y}) scale(${mapZoomData.value.scale})`
  }
})"""
map_style_new = """const tiltX = ref(0)
const tiltY = ref(0)

function onMouseMove(e) {
  if (isDragging.value || isZooming.value || activeOverlay.value) {
    tiltX.value = 0
    tiltY.value = 0
    return
  }
  const x = (e.clientX / window.innerWidth) - 0.5
  const y = (e.clientY / window.innerHeight) - 0.5
  tiltX.value = -y * 30
  tiltY.value = x * 30
}

const mapTransformStyle = computed(() => {
  if (isZooming.value || activeOverlay.value) {
    return {
      transform: `translate(${mapZoomData.value.x}, ${mapZoomData.value.y}) scale(${mapZoomData.value.scale})`,
      transition: 'transform 1s ease-in-out'
    }
  }
  return {
    transform: `translate(${mapZoomData.value.x}, ${mapZoomData.value.y}) scale(${mapZoomData.value.scale}) perspective(1200px) rotateX(${tiltX.value}deg) rotateY(${tiltY.value}deg)`,
    transformStyle: 'preserve-3d',
    transition: 'transform 0.1s linear' // Fast transition for smooth mouse follow
  }
})"""
content = content.replace(map_style_old, map_style_new)

# 5. Modify selectIsland to use router.push
select_old = """function selectIsland(event, island) {
  if (isDragging.value) return; // Prevent click when dragging

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
}"""
select_new = """function selectIsland(event, island) {
  if (isDragging.value) return; // Prevent click when dragging

  if (island.isLocked) return // Prevent clicking locked islands
  
  try { soundManager.playClick() } catch(e) {}
  
  // Navigate to WorldView directly with the island ID as a query param
  router.push({ path: '/world', query: { island: island.id } })
}"""
content = content.replace(select_old, select_new)

with open('src/views/LandingView.vue', 'w') as f:
    f.write(content)

print("Done patching LandingView.vue")
