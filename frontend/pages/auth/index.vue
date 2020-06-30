<template>
    <div>        
       <signup-login 
       :login="login"
       :form="form"
       :viewMessage="viewMessage"
       :message="message"
       :authHandle="authHandle"/>
    </div>
</template>

<script>
import SignupLogin from '~/components/auth/signuplogin'
export default {
    data() {
        return {
            login: true,
            viewMessage: false,
            message: '',
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
            let message = ''

            this.$store.dispatch('logIn', data)
            .then( res => {
                if (res.response === undefined) {
                    this.$router.push('/')
                } else if (res.response.status === 401){
                    this.message = "Not Authorised: " + res.response.data.detail + " . Try Again"
                    this.viewMessage = true
                } else if (res.response.status === 400) {
                    this.message = "Not Authorised: Username and or Passwsord fields cannot be left blank"
                    this.viewMessage = true
                } else {
                    // ...
                }             
            })
        }
    },
    components: {
        SignupLogin
    }
}
</script>