import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import tailwindcss from '@tailwindcss/vite'
import { VitePWA } from 'vite-plugin-pwa'

const isVercel = process.env.VERCEL === '1' || process.env.VERCEL === 'true'
const appBase = isVercel ? '/' : '/florascan/'

export default defineConfig({
  base: appBase,
  server: {
    watch: {
      ignored: ['**/venv/**']
    }
  },
  optimizeDeps: {
    entries: ['index.html']
  },
  plugins: [
    vue({
      template: {
        compilerOptions: {
          isCustomElement: tag => tag.startsWith('Tres') && tag !== 'TresCanvas',
        },
      },
    }),
    tailwindcss(),
    VitePWA({
      registerType: 'autoUpdate',
      workbox: {
        globPatterns: ['**/*.{js,css,html,ico,png,svg,json,bin,webmanifest}'],
        maximumFileSizeToCacheInBytes: 5 * 1024 * 1024
      },
      manifest: {
        id: appBase,
        name: 'FaunaNusantara.ai',
        short_name: 'FaunaNusantara',
        description: 'Professional AI Bird Identifier',
        theme_color: '#059669',
        background_color: '#ffffff',
        display: 'standalone',
        orientation: 'portrait',
        scope: appBase,
        start_url: appBase,
        icons: [
          {
            src: 'pwa-192x192.png',
            sizes: '192x192',
            type: 'image/png',
            purpose: 'any maskable'
          },
          {
            src: 'pwa-512x512.png',
            sizes: '512x512',
            type: 'image/png',
            purpose: 'any maskable'
          }
        ]
      },
      devOptions: {
        enabled: true,
        type: 'module',
      }
    })
  ]
})
