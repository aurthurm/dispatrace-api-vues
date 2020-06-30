export default function ({ context, store, state, redirect }) {
    if (!store.state.auth.token) {
      return redirect('/auth')
    }
  }
  