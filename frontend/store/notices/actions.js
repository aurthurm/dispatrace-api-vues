export default {
    async setNotices({ commit }, header) {  
        await this.$axios.$get('/notices/', { headers: header })
        .then(res => {
          commit('setNotices', res)
        })
        .catch(err => console.log(err))
    },
}