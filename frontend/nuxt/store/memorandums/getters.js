export default {
    getMemos(state) {
      return state.memorandums
    },
    
    getMemoStates(state) {
      return state.states
    },

    getSearchStatus(state) {
      return state.searched
    },

    getSelectedState(state) {
      return state.selectedState
    },

    getMemoDetailView(state) {
       return state.detailView
    },
}
