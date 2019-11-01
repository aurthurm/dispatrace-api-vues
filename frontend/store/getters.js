export default {
    isAuthenticated(state) {
      return state.auth.loggedIn
    },
  
    loggedInUser(state) {
      return state.auth.user.username
    },

    accessToken(state) {
        return state.auth.token
    },

    refreshToken(state) {
        return state.auth.refresh
    },

    authHeader() {
      let auth = JSON.parse(localStorage.getItem('auth'))
      if (auth && auth.access) {
          return { Authorization: `Bearer  ${auth.access}` }
      } else {
        return this.$router.push('/auth')
      }     
    },

    getAccounts(state) {
      return state.accounts
    }
}