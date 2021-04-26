import Home from './views/Home.vue'
import Vue from './views/Vue.vue'
import Swift from './views/Swift.vue'
import AWS from './views/AWS.vue'
import Python from './views/Python.vue'
import About from './views/About.vue'
import NotFound from './views/NotFound.vue'

/** @type {import('vue-router').RouterOptions['routes']} */
export const routes = [
  { path: '/', component: Home, 
    // meta: { title: 'Home' } 
  },
  { path: '/vue', component: Vue, 
    // meta: { title: 'Vue' } 
  },
  { path: '/swift', component: Swift, 
    // meta: { title: 'Swift' } 
  },
  { path: '/aws', component: AWS, 
    // meta: { title: 'AWS' } 
  },
  { path: '/python', component: Python, 
    // meta: { title: 'Python' } 
  },
  {
    path: '/about',
    // meta: { title: 'About' },
    component: About,
    // example of route level code-splitting
    // this generates a separate chunk (About.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: () => import('./views/About.vue')
  },
  { path: '/:path(.*)', component: NotFound },
]
