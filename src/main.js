import { createApp } from 'vue'
import './tailwind.css'
import App from './App.vue'
import { routes } from './routes.js'
import { createRouter, createWebHistory } from 'vue-router'
import { Menu } from 'ant-design-vue'
import { Card } from 'ant-design-vue'
import { Avatar } from 'ant-design-vue'
import "ant-design-vue/dist/antd.css"


const app = createApp(App)

const router = createRouter({
  history: createWebHistory(),
  routes,
})


app.use(router)
app.use(Menu)
app.use(Card)
app.use(Avatar)
app.mount('#app')
