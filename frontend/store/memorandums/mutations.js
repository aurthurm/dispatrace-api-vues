export default {
    setMemos (state, memos) {
        let memorandums = [];
        if(memos.data === undefined) {
            memorandums = memos
        } else {
            memorandums = memos.data
        }
        memorandums.forEach(memoir => {
            memoir.memo_state = memos.status
        });
        state.memorandums = [ ...memorandums]
    },

    setSearchStatus(state, sstatus) {
        state.searched = sstatus
    },

    setSelectedState(state, sstate) {
        state.selectedState = sstate
    },

    setMemoDetailView(state, isDetail) {
        state.detailView = isDetail
    },
}