export default {

    resetMemorandumState ({ commit }) {
      commit('resetMemorandumState')
    },

    async createMemorandum({}, data) {   
      console.log("form", data)   
      await this.$axios.$post('/memos/', { form_data: data }, { headers: this.getters['authHeader'] })
      .then(res => {
        this.$router.push({ path: '/memo/' + res.data.id})
      })
      .catch(err  => {
        if(err.response.status === 401){
          return this.$router.push('/auth')
        }  
      })  
    },

    async setMemos({ commit }, data) { 
      commit('setSelectedState', data.memo_state)
      await this.$axios.$get('/memos/?mstate=' + data.memo_state.toLocaleLowerCase() , { headers: this.getters['authHeader'] })
        .then(res => {        
          commit('setMemos', { data: res, status: data.memo_state.toLocaleLowerCase()})
        })
        .catch(err  => {
          if(err.response.status === 401){
            return this.$router.push('/auth')
          }  
        })    
    },

    async setSearchResults({ commit }, searchQuery) { 
      commit('setSearchStatus', true)
      await this.$axios.$get('/memos/?q=' + searchQuery, { headers: this.getters['authHeader'] })
        .then(res => {  
            commit('setMemos', res) 
        })
        .catch(err  => {
          // if(err.response.status === 401){
          //   return this.$router.push('/auth')
          // }  
          console.log("Check err status if accessible");
          console.log(err);
        })  
    },

    setSelectedState({ commit }, selected) {
      commit('setSelectedState', selected)
    },    

    setMemoDetailView({ commit }, isDetail) {
      commit('setMemoDetailView', isDetail)
    },

}