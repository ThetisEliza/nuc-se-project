import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { fileURLToPath } from 'url'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL("./src",  import.meta.url))
    }
  },
  server: {
    port: 8080,
    cors: true, 
    open: true, // 在服务器启动时自动在浏览器中打开应用程序
    //反向代理配置，注意rewrite写法，开始没看文档在这里踩了坑
    proxy: {// 本地开发环境通过代理实现跨域，生产环境使用 nginx 转发
      '/api': {
        target: 'http://47.94.152.114:8080/', // 通过代理接口访问实际地址。这里是实际访问的地址。vue会通过代理服务器来代理请求
        changeOrigin: true,
        // rewrite: (path) => path.replace(/^\/api/, '') // 将api替换为空
      }
    }
  }
})
