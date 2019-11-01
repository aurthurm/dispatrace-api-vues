var jwt = require('jsonwebtoken');

export default {
    logIn({ commit }, userData) {
        return this.$axios.$post('token/extras/', userData) 
        .then(res => {
            commit('setAuth', res)                    
            localStorage.setItem('auth', JSON.stringify(res));
        })
        .catch(err => console.log(err))
    },

    signUp({ commit }, userData) {        
        return this.$axios.$post('accounts/signup/', userData)
        .then(res => {
            commit('setAuth', res)                    
            localStorage.setItem('auth', JSON.stringify(res));
        })
        .catch(err => console.log(err))
    },

    logOut ({ commit }) {
        commit('logOut')
    },

    persistAuth({ commit }) {
        let auth = JSON.parse(localStorage.getItem('auth'))
        if (!auth) {
           return;
        } else {
            var decoded = jwt.decode(auth.access);
            var expiredToken = Date.now() > new Date(decoded.exp * 1000);
            if(expiredToken){
                commit('logOut')
            }
            commit('setAuth', auth)
        }   
        // to do
        // chect if token is about to expire ask user to extend session or let auto logout
    }, 

    async setAccounts({ commit }, header) {
        await this.$axios.$get('accounts/', { headers: header })
        .then(res => {
            commit('setAccounts', res)
        })
        .catch( err => console.log(err))
    }
}