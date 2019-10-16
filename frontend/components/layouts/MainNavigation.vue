<template>
<div>
  <b-navbar toggleable="lg" type="dark" variant="info">
    <b-navbar-brand href="#">NavBar</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#">Link</b-nav-item>
        <b-nav-item href="#" disabled>Disabled</b-nav-item>
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">

        <b-nav-item-dropdown text="Lang" right>
          <b-dropdown-item href="#">EN</b-dropdown-item>
          <b-dropdown-item href="#">ES</b-dropdown-item>
          <b-dropdown-item href="#">RU</b-dropdown-item>
          <b-dropdown-item href="#">FA</b-dropdown-item>
        </b-nav-item-dropdown>

        <b-nav-item-dropdown right>
          <!-- Using 'button-content' slot -->
          <template v-slot:button-content>
            <em>User</em>
          </template>
          <b-dropdown-item href="#">Profile</b-dropdown-item>
          <b-dropdown-item href="#">Sign Out</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</div>
</template>

<style  scoped>
  nav {
    position: fixed;
    top: 0;
    z-index: 999999;
  }
</style>

<script>
export default {
  methods: {
    adjustNavBar() {
      var msw = document.querySelector("#mainSiteWrapper");
      var sb = document.querySelector("#sidebar");
      var navWidth = msw.clientWidth - sb.clientWidth;
      var navbar = document.querySelector("nav.navbar");
      navbar.style.width = navWidth + "px";
    },
    adjustMainContent() {
      var navbar = document.querySelector("nav.navbar");
      var navheight = navbar.clientHeight + 5;
      var contentWindow = document.querySelector("main");
      contentWindow.style.paddingTop = navheight + "px";
    }
  },
  mounted() {
    this.adjustNavBar()
    this.adjustMainContent()
  }
}


</script>