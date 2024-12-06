import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugings: [react()],
  server: {
    proxy: {
      '/api': 'http://127.0.0.1:5000', // Proxy API requests to FLASK
    },
  },
});

