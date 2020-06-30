export default {
    setAuth (state, auth) {
        state.auth.token = auth.access
        state.auth.refresh = auth.refresh
        state.auth.user = auth.user
        state.auth.loggedIn = true
    },

    logOut (state) {
        state.auth.token = null
        state.auth.refresh = null
        state.auth.user = ''
        state.auth.loggedIn = false
        state. timeLeft = { hours: 0, minutes: 0 }
        localStorage.removeItem('auth'); 
        return this.$router.push('/auth')
    }, 

    setAccounts(state, accounts) {
        state.accounts = [ ...accounts]
    },

}
