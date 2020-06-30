var jwt = require('jsonwebtoken');

export default {
    logIn({ commit }, userData) {
        return this.$axios.$post('token/extras/', userData) 
        .then(res => {
            // check if data exists :: to do
            commit('setAuth', res)                    
            localStorage.setItem('auth', JSON.stringify(res));
            return res
        })
        .catch(err => err)
    },

    signUp({ commit }, userData) {        
        return this.$axios.$post('accounts/signup/', userData)
        .then(res => {
            this.$router.push('/admin/accounts/' + res.id  + '-' + res.username + '/')
        })
        .catch(err  => {
          if(err.response.status === 401){
            return this.$router.push('/auth')
          }  
        })  
    },

    logOut ({ commit }) {
        commit('logOut')
    },

    persistAuth({ commit }) {
        let auth = JSON.parse(localStorage.getItem('auth'))
        if (!auth) {
           return;
        } else {

            let decoded = jwt.decode(auth.access);
            let decodedTime = new Date(decoded.exp * 1000);
            let nowTime = Date.now();
            let expiredToken = nowTime > decodedTime;

            if(expiredToken){
                commit('logOut') 
                return;
            }
            commit('setAuth', auth)
        }   
    }, 

    async setAccounts({ commit }, header) {
        await this.$axios.$get('accounts/', { headers: header })
        .then(res => {
            commit('setAccounts', res)
        })
        .catch(err  => {
          if(err.response.status === 401){
            return this.$router.push('/auth')
          }  
        })  
    },

    checkTimeLeft() {   
        let auth = JSON.parse(localStorage.getItem('auth'))
        if (!auth) {
          return;
        } else {
          let decoded = jwt.decode(auth.access);
          let decodedTime = new Date(decoded.exp * 1000);
          let nowTime = Date.now();
          function timeToSessionExpiry(currentTime, expiryTime) {
            let currentTimeMinutes = new Date(currentTime).getHours() * 60 + new Date(currentTime).getMinutes()
            let expiryTimeMinutes = expiryTime.getHours() * 60 + expiryTime.getMinutes()
            return expiryTimeMinutes - currentTimeMinutes
          }
          let minutesLeft = timeToSessionExpiry(nowTime, decodedTime);
          let hoursLeft = +((minutesLeft/60).toString().substring(0,1));
          let timeLeft = { 
            hours: hoursLeft, 
            minutes: minutesLeft 
          }
          return timeLeft
        }
    },

    async extendSession() {
      let auth = JSON.parse(localStorage.getItem('auth'))
      if (!auth || !auth.refresh) return;
      await this.$axios.post('refresh/', { "refresh": auth.refresh })
            .then(res => {
              auth.access = res.data.access
              // localStorage.removeItem('auth'); 
              localStorage.setItem('auth', JSON.stringify(auth))
              return res
            })
            .catch(err => console.log(err)) 
    }

}