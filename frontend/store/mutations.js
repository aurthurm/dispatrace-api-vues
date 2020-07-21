import { initialState } from "./initial_state.js";

export default {
    resetState (state) {
        // Object.assign(state, initialState)
        let new_state = initialState();
        Object.keys(state).forEach(key => {
            Object.assign(state[key], new_state[key])
        })
    },

    setAuth (state, auth) {
        state.auth.token = auth.access
        state.auth.refresh = auth.refresh
        state.auth.user = auth.user
        state.auth.loggedIn = true
    },

    logOut (state) {
        // localStorage.removeItem('auth'); 
        localStorage.clear();
        state.auth.token = ""
        state.auth.refresh = ""
        state.auth.user = {
            "username": "",
            "user_id": ""
        }
        state.auth.loggedIn = false
        this.$router.go(this.$router.currentRoute);
        return this.$router.push('/auth')
    }, 

    setAccounts(state, accounts) {
        state.accounts = [ ...accounts]
    },

}
