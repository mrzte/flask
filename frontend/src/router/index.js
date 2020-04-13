import Vue from 'vue'
import Router from 'vue-router'
import Pilar from '@/components/Pilar'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Pilar',
      component: Pilar
    }
  ]
})
