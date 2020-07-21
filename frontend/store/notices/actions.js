export default {

  resetNoticesState ({ commit }) {
    commit('resetNoticesState')
  },
  
  async setNotices({ commit }, header) {  
      await this.$axios.$get('/notices/', { headers: header })
      .then(res => {
        commit('setNotices', res)
      })
      .catch(err  => {
        if(err.response.status === 401){
          return this.$router.push('/auth')
        }  
      })  
  },

}