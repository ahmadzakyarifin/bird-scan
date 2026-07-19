import re
import json

with open('src/views/LandingView.vue', 'r') as f:
    content = f.read()

# Replace texts
content = content.replace('FloraNusantara', 'FaunaNusantara.ai')
content = content.replace('Buku Histori Flora', 'Buku Histori Avifauna')
content = content.replace('floraHistory', 'faunaHistory')
content = content.replace('flora_history', 'fauna_history')
content = content.replace('Total: {{ faunaHistory.length }} Flora', 'Total: {{ faunaHistory.length }} Burung')
content = content.replace('Total Flora Ditemukan', 'Total Burung Ditemukan')
content = content.replace('Identifikasi Flora', 'Identifikasi Burung')
content = content.replace('memindai tanaman', 'memindai burung')
content = content.replace('Menganalisis Flora...', 'Menganalisis Burung...')
content = content.replace('penemuan spesifik flora', 'penemuan spesifik burung')
content = content.replace('🌱', '🪶')
content = content.replace('plantDescriptions', 'birdDescriptions')
content = content.replace('plantIslandMap', 'birdIslandMap')
content = content.replace('islandPlants', 'islandBirds')
content = content.replace('getIslandPlantsCount', 'getIslandBirdsCount')
content = content.replace('viewPlantDetail', 'viewBirdDetail')
content = content.replace('selectedPlantDetail', 'selectedBirdDetail')
content = content.replace('randomPlant', 'randomBird')
content = content.replace('allPlants', 'allBirds')

# Birds mock data
old_plants_desc = """const birdDescriptions = {
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
}"""

new_birds_desc = """const birdDescriptions = {
  'Jalak Bali': 'Burung endemik pulau Bali yang sangat indah dengan bulu putih bersih dan topeng biru di sekitar matanya.',
  'Cendrawasih': 'Dikenal sebagai burung surga. Memiliki bulu yang sangat indah dan mempesona, banyak ditemukan di Papua.',
  'Kakatua Raja': 'Kakatua hitam besar yang merupakan spesies kakatua terbesar di Indonesia. Memiliki jambul yang khas.',
  'Elang Jawa': 'Burung pemangsa yang gagah dan sering dianggap sebagai inspirasi burung Garuda. Endemik pulau Jawa.',
  'Rangkong Badak': 'Burung besar dengan paruh dan tanduk (casque) yang menonjol di kepalanya, banyak di Sumatera dan Kalimantan.',
  'Maleo': 'Burung endemik Sulawesi yang tidak mengerami telurnya sendiri, melainkan memendamnya di dalam pasir hangat.',
  'Nuri Bayan': 'Burung nuri dengan perbedaan warna yang sangat mencolok antara jantan (hijau) dan betina (merah).',
  'Burung Hantu Celepuk': 'Burung hantu kecil yang sering ditemukan di sekitar pemukiman atau hutan sekunder di banyak pulau.',
  'Kasuari': 'Burung besar tidak bisa terbang dari wilayah timur Indonesia. Memiliki tanduk pelindung di atas kepalanya.',
  'Murai Batu': 'Burung kicau yang sangat populer karena suaranya yang merdu dan ekornya yang panjang dan elegan.',
  'Merak Hijau': 'Burung yang sangat mempesona dengan ekor kipasnya yang dipenuhi corak mata. Banyak di Jawa.',
  'Cucak Rawa': 'Burung kicau legendaris yang mendiami daerah rawa dan hutan berair, memiliki suara vokal yang khas.',
  'Kuntul Kerbau': 'Burung bangau kecil berwarna putih yang sering terlihat menemani kerbau atau sapi di sawah.',
  'Trulek Jawa': 'Burung air yang sangat langka dan statusnya sangat terancam punah. Merupakan endemik pulau Jawa.',
  'Burung Madu': 'Burung kecil penghisap nektar dengan warna bulu metalik yang sangat cantik dan terbang dengan gesit.'
}"""
content = content.replace(old_plants_desc, new_birds_desc)

old_plant_map = """const birdIslandMap = {
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
}"""

new_bird_map = """const birdIslandMap = {
  'Jalak Bali': 'bali',
  'Cendrawasih': 'papua',
  'Kakatua Raja': 'papua',
  'Elang Jawa': 'jawa',
  'Rangkong Badak': 'kalimantan',
  'Maleo': 'sulawesi',
  'Nuri Bayan': 'maluku',
  'Burung Hantu Celepuk': 'jawa',
  'Kasuari': 'papua',
  'Murai Batu': 'sumatra',
  'Merak Hijau': 'jawa',
  'Cucak Rawa': 'sumatra',
  'Kuntul Kerbau': 'bali',
  'Trulek Jawa': 'jawa',
  'Burung Madu': 'sulawesi'
}"""
content = content.replace(old_plant_map, new_bird_map)


# Replace island setup to allow dragging
# Change islands definition to use defaultX and defaultY instead of positionClass
content = re.sub(r"positionClass: 'top-\[(\d+)%\] left-\[(\d+)%\]',", r"defaultX: \2, defaultY: \1,", content)

island_html_old = """        <div 
          v-for="island in islands" 
          :key="island.id"
          class="absolute transition-all duration-500 cursor-pointer group flex flex-col items-center justify-center animate-float"
          :class="[island.positionClass, island.sizeClass]"
          :style="`animation-delay: ${island.animDelay}s; z-index: ${hoveredIsland?.id === island.id ? 20 : 10}`"
          @mouseenter="handleIslandHover(island)"
          @mouseleave="hoveredIsland = null"
          @click="selectIsland(island)"
        >"""

island_html_new = """        <div 
          v-for="island in islands" 
          :key="island.id"
          class="absolute transition-all duration-500 cursor-pointer group flex flex-col items-center justify-center animate-float touch-none"
          :class="[island.sizeClass, { '!transition-none': isDragging && draggingIsland?.id === island.id }]"
          :style="{ 
            animationDelay: island.animDelay + 's', 
            zIndex: (isDragging && draggingIsland?.id === island.id) ? 30 : (hoveredIsland?.id === island.id ? 20 : 10),
            left: (islandPos[island.id]?.x !== undefined ? islandPos[island.id].x : island.defaultX) + '%',
            top: (islandPos[island.id]?.y !== undefined ? islandPos[island.id].y : island.defaultY) + '%'
          }"
          @mouseenter="handleIslandHover(island)"
          @mouseleave="hoveredIsland = null"
          @click="selectIsland($event, island)"
          @pointerdown="startDrag($event, island)"
        >"""

content = content.replace(island_html_old, island_html_new)
content = content.replace('@click="selectIsland(island)"', '@click="selectIsland($event, island)"')

# Add drag logic variables
script_setup_old = "const floraHistory = ref(JSON.parse(localStorage.getItem('flora_history') || '[]'))"
script_setup_new = """const faunaHistory = ref(JSON.parse(localStorage.getItem('fauna_history') || '[]'))

// Dragging logic
const islandPos = ref(JSON.parse(localStorage.getItem('island_positions') || '{}'))
const isDragging = ref(false)
const draggingIsland = ref(null)
let dragStartX = 0
let dragStartY = 0
let initialIslandX = 0
let initialIslandY = 0

function startDrag(event, island) {
  if (isZooming.value) return;
  isDragging.value = true;
  draggingIsland.value = island;
  dragStartX = event.clientX;
  dragStartY = event.clientY;
  
  // Set initial position in percentages based on what's currently stored or default
  initialIslandX = islandPos.value[island.id]?.x !== undefined ? islandPos.value[island.id].x : island.defaultX;
  initialIslandY = islandPos.value[island.id]?.y !== undefined ? islandPos.value[island.id].y : island.defaultY;
  
  window.addEventListener('pointermove', onDrag);
  window.addEventListener('pointerup', endDrag);
}

function onDrag(event) {
  if (!isDragging.value || !draggingIsland.value) return;
  
  // Calculate delta in pixels
  const deltaX = event.clientX - dragStartX;
  const deltaY = event.clientY - dragStartY;
  
  // Convert delta to percentage of screen/wrapper width. The wrapper is 1500x800 base.
  // We need to divide by the actual scaled width/height.
  const wrapper = document.querySelector('.relative.w-\\\\[1500px\\\\]'); // getting the wrapper element
  if (!wrapper) return;
  const rect = wrapper.getBoundingClientRect();
  
  // Percentage delta
  const pctX = (deltaX / rect.width) * 100;
  const pctY = (deltaY / rect.height) * 100;
  
  const newX = initialIslandX + pctX;
  const newY = initialIslandY + pctY;
  
  islandPos.value[draggingIsland.value.id] = { x: newX, y: newY };
}

function endDrag(event) {
  if (!isDragging.value) return;
  
  // Save to localStorage
  localStorage.setItem('island_positions', JSON.stringify(islandPos.value));
  
  window.removeEventListener('pointermove', onDrag);
  window.removeEventListener('pointerup', endDrag);
  
  // Brief timeout to prevent triggering click event if we were just dragging
  setTimeout(() => {
    isDragging.value = false;
    draggingIsland.value = null;
  }, 100);
}
"""
content = content.replace(script_setup_old, script_setup_new)
content = content.replace("function selectIsland(island) {", """function selectIsland(event, island) {
  if (isDragging.value) return; // Prevent click when dragging
""")

with open('src/views/LandingView.vue', 'w') as f:
    f.write(content)
print("Done rewriting LandingView.vue")
