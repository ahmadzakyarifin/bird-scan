<template>
  <TresGroup :position="position" :rotation="rotation" :scale="scale">
    <!-- If model is loading or failed, show fallback -->
    <Suspense>
      <GLTFModel 
        v-if="modelPath"
        :path="modelPath" 
        draco 
        receive-shadow 
        cast-shadow 
      />
      
      <!-- Fallback geometry passed via slot if model is not used or while loading -->
      <template #fallback>
        <slot></slot>
      </template>
    </Suspense>
    
    <!-- Invisible Hitbox for precise clicking regardless of model shape -->
    <TresMesh 
      @click="(e) => { e.stopPropagation(); $emit('click', e) }"
      @pointer-enter="(e) => { e.stopPropagation(); document.body.style.cursor='pointer' }"
      @pointer-leave="(e) => { e.stopPropagation(); document.body.style.cursor='default' }"
      :visible="false"
    >
      <TresBoxGeometry :args="hitboxArgs" />
      <TresMeshBasicMaterial color="red" :wireframe="true" />
    </TresMesh>
  </TresGroup>
</template>

<script setup>
import { GLTFModel } from '@tresjs/cientos'

const props = defineProps({
  position: { type: Array, default: () => [0, 0, 0] },
  rotation: { type: Array, default: () => [0, 0, 0] },
  scale: { type: Array, default: () => [1, 1, 1] },
  modelPath: { type: String, default: '' },
  hitboxArgs: { type: Array, default: () => [3, 3, 3] }
})

const emit = defineEmits(['click'])
</script>
