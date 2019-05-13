import Vue from 'vue'
import Router from 'vue-router'
Vue.use(Router)


// route level code-splitting
// this generates a separate chunk (vuefile.[hash].js) for each route
// which is lazy-loaded when the route is visited.
export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      components: {
        default: () => import('@/views/Home'),
        commonHeader: () => import('@/views/common/Header'),
        commonFooter: () => import('@/views/common/Footer')
      },
    },
    {
      path: '/video',
      name: 'video',
      components: {
        default: () => import('@/views/Video'),
        commonHeader: () => import('@/views/common/Header'),
        commonFooter: () => import('@/views/common/Footer')
      },
    },
    {
        path: '/region',
        name: 'region',
        components: {
          default: () => import('@/views/Region'),
          commonHeader: () => import('@/views/common/Header'),
          commonFooter: () => import('@/views/common/Footer')
        },
    },
    {
        path: '/tv',
        name: 'tv',
        components: {
          default: () => import('@/views/Tv'),
          commonHeader: () => import('@/views/common/Header'),
          commonFooter: () => import('@/views/common/Footer')
        },
    },
    
  ]
})
