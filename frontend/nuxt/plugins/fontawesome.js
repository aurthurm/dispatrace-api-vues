import Vue from 'vue'
import { library, config } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faSpinner, faBars, faEye, faEdit, faTimes, faCog, faUsers, faUser, faSignOutAlt } from '@fortawesome/free-solid-svg-icons'

// This is important, we are going to let Nuxt.js worry about the CSS
config.autoAddCss = false

// You can add your icons directly in this plugin
library.add(faSpinner, faBars, faEye, faEdit, faTimes, faCog, faUsers, faUser, faSignOutAlt)

// Register the component globally
Vue.component('font-awesome-icon', FontAwesomeIcon)