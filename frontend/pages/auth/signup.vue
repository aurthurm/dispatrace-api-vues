<template>
    <div>        
       <signup-login 
       :login="login"
       :form="form"
       :authHandle="authHandle"/>
    </div>
</template>

<script>
import SignupLogin from '~/components/auth/signuplogin'
export default {
    data() {
        return {
            login: false,
            form: {
                username: '',
                password: '',
                password2: '',
                firstname: '',
                lastname: '',
                email: ''
            }
        }
    },
    methods: {
        authHandle() {
            var data = {}
            data['username'] = this.form.username
            data['password'] = this.form.password
            data['password2'] = this.form.password2                
            data['firstname'] = this.form.firstname
            data['lastname'] = this.form.lastname
            data['email'] = this.form.email
            this.$store.dispatch('signUp', data)
        }
    },
    components: {
        SignupLogin
    }
}
</script>