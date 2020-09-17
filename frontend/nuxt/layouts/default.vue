<template>
  <div>
    <div class="site-content d-flex justify-content-start">
      <LeftSideNavigation />
      <div class="d-flex flex-column w-100" id="mainSiteWrapper">
        <MainNavigation />
        <main>
          <nuxt />
        </main>
      </div>
    </div>
  </div>
</template>

<style>
html {
  font-family: 'Source Sans Pro', -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, 'Helvetica Neue', Arial, sans-serif;
  font-size: 16px;
  word-spacing: 1px;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
  -moz-osx-font-smoothing: grayscale;
  -webkit-font-smoothing: antialiased;
  box-sizing: border-box;
}

body {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
  padding-right: 0 !important;
}

.site-content {
  flex: 1;
}

#mainSiteWrapper {
  padding-left: 200px!important;
}

*,
*:before,
*:after {
  box-sizing: border-box;
  margin: 0;
}

.button--green {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #3b8070;
  color: #3b8070;
  text-decoration: none;
  padding: 10px 30px;
}

.button--green:hover {
  color: #fff;
  background-color: #3b8070;
}

.button--grey {
  display: inline-block;
  border-radius: 4px;
  border: 1px solid #35495e;
  color: #35495e;
  text-decoration: none;
  padding: 10px 30px;
  margin-left: 15px;
}

.button--grey:hover {
  color: #fff;
  background-color: #35495e;
}
</style>

<script>
import MainNavigation from '~/components/layouts/MainNavigation.vue'
import LeftSideNavigation from '~/components/layouts/LeftSideNavigation.vue'

export default {
  middleware: ['force-auth'],
  components: {
    MainNavigation,
    LeftSideNavigation
  }
}
</script>
