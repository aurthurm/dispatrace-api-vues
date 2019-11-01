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
        localStorage.removeItem('auth'); 
        console.log("Logging you out")
        return this.$router.push('/auth')
    }, 

    setAccounts(state, accounts) {
        state.accounts = [...state.accounts , ...accounts]
    }
}
