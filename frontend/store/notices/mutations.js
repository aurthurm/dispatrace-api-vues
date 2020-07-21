import { initialState } from "./initial_state.js";

export default {
    resetNoticesState (state) {
        // Object.assign(state, initialState)
        let new_state = initialState();
        Object.keys(state).forEach(key => {
            Object.assign(state[key], new_state[key])
        })
    },

    setNotices (state, notices) {
        state.notices = notices
    }
}