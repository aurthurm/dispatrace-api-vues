import Vue from 'vue'
import Router from 'vue-router'
import { interopDefault } from './utils'
import scrollBehavior from './router.scrollBehavior.js'

const _ff9299e0 = () => interopDefault(import('../pages/auth.vue' /* webpackChunkName: "pages/auth" */))
const _5d54ad93 = () => interopDefault(import('../pages/auth/index.vue' /* webpackChunkName: "pages/auth/index" */))
const _04e7b1a7 = () => interopDefault(import('../pages/auth/signup.vue' /* webpackChunkName: "pages/auth/signup" */))
const _04d1d1a2 = () => interopDefault(import('../pages/memo.vue' /* webpackChunkName: "pages/memo" */))
const _3021d2b6 = () => interopDefault(import('../pages/memo/index.vue' /* webpackChunkName: "pages/memo/index" */))
const _512c7e4d = () => interopDefault(import('../pages/memo/_id.vue' /* webpackChunkName: "pages/memo/_id" */))
const _0e625710 = () => interopDefault(import('../pages/memo/_id/index.vue' /* webpackChunkName: "pages/memo/_id/index" */))
const _48aaaa3c = () => interopDefault(import('../pages/memo/_id/edit.vue' /* webpackChunkName: "pages/memo/_id/edit" */))
const _ed9d927a = () => interopDefault(import('../pages/notice/index.vue' /* webpackChunkName: "pages/notice/index" */))
const _68e94911 = () => interopDefault(import('../pages/admin/accounts/index.vue' /* webpackChunkName: "pages/admin/accounts/index" */))
const _6e0ddecb = () => interopDefault(import('../pages/admin/settings.vue' /* webpackChunkName: "pages/admin/settings" */))
const _c3e63de4 = () => interopDefault(import('../pages/admin/settings/index.vue' /* webpackChunkName: "pages/admin/settings/index" */))
const _8d289186 = () => interopDefault(import('../pages/admin/settings/cities.vue' /* webpackChunkName: "pages/admin/settings/cities" */))
const _3592165c = () => interopDefault(import('../pages/admin/settings/country.vue' /* webpackChunkName: "pages/admin/settings/country" */))
const _789915c6 = () => interopDefault(import('../pages/admin/settings/departments.vue' /* webpackChunkName: "pages/admin/settings/departments" */))
const _070a4e63 = () => interopDefault(import('../pages/admin/settings/levels.vue' /* webpackChunkName: "pages/admin/settings/levels" */))
const _0fb7041a = () => interopDefault(import('../pages/admin/settings/offices.vue' /* webpackChunkName: "pages/admin/settings/offices" */))
const _01a85bb9 = () => interopDefault(import('../pages/admin/accounts/_id.vue' /* webpackChunkName: "pages/admin/accounts/_id" */))
const _020ac59a = () => interopDefault(import('../pages/index.vue' /* webpackChunkName: "pages/index" */))

Vue.use(Router)

export const routerOptions = {
  mode: 'history',
  base: decodeURI('/'),
  linkActiveClass: 'nuxt-link-active',
  linkExactActiveClass: 'nuxt-link-exact-active',
  scrollBehavior,

  routes: [{
    path: "/auth",
    component: _ff9299e0,
    children: [{
      path: "",
      component: _5d54ad93,
      name: "auth"
    }, {
      path: "signup",
      component: _04e7b1a7,
      name: "auth-signup"
    }]
  }, {
    path: "/memo",
    component: _04d1d1a2,
    children: [{
      path: "",
      component: _3021d2b6,
      name: "memo"
    }, {
      path: ":id",
      component: _512c7e4d,
      children: [{
        path: "",
        component: _0e625710,
        name: "memo-id"
      }, {
        path: "edit",
        component: _48aaaa3c,
        name: "memo-id-edit"
      }]
    }]
  }, {
    path: "/notice",
    component: _ed9d927a,
    name: "notice"
  }, {
    path: "/admin/accounts",
    component: _68e94911,
    name: "admin-accounts"
  }, {
    path: "/admin/settings",
    component: _6e0ddecb,
    children: [{
      path: "",
      component: _c3e63de4,
      name: "admin-settings"
    }, {
      path: "cities",
      component: _8d289186,
      name: "admin-settings-cities"
    }, {
      path: "country",
      component: _3592165c,
      name: "admin-settings-country"
    }, {
      path: "departments",
      component: _789915c6,
      name: "admin-settings-departments"
    }, {
      path: "levels",
      component: _070a4e63,
      name: "admin-settings-levels"
    }, {
      path: "offices",
      component: _0fb7041a,
      name: "admin-settings-offices"
    }]
  }, {
    path: "/admin/accounts/:id",
    component: _01a85bb9,
    name: "admin-accounts-id"
  }, {
    path: "/",
    component: _020ac59a,
    name: "index"
  }],

  fallback: false
}

export function createRouter () {
  return new Router(routerOptions)
}
