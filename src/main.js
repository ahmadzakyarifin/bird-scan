import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from './router'
import i18n from './i18n'
import Tres from '@tresjs/core'

// PWA Registration
import { registerSW } from 'virtual:pwa-register'

registerSW({ immediate: true })

// Cek dan aplikasikan Dark Mode awal (target html tag instead of body for tailwind)
if (localStorage.getItem('theme') === 'dark' || (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
  document.documentElement.classList.add('dark')
} else {
  document.documentElement.classList.remove('dark')
}

const app = createApp(App)
app.use(Tres)
app.use(router)
app.use(i18n)
app.mount('#app')
