<template>
    <div class="container-fluid">
      <h4>Registered User Accounts <b-button size='sm' variant='info' @click="showModal">+ New User</b-button></h4>
        <hr>
        <table class="table">
            <thead>
                <tr>
                    <th>Username</th>    
                    <th>Full Name</th>
                    <th data-breakpoints="xs">Job Title</th>
                    <th data-breakpoints="xs sm md" data-title="DOB">City</th>
                    <th>Office</th>
                    <th>Department</th>
                    <th>Satus</th>
                    <th>View Profile</th>
                </tr>
            </thead>
            <tbody>
                <tr 
                v-for="account in accounts"
                :key="account.id"
                data-expanded="true" 
                class="bg-warning text-white">
                        <td >@{{ account.username }}</td>
                        <td>{{ account.userFullName }}</td>
                        <td>{{ account.title }}</td>
                        <td>{{ account.city }}</td>
                        <td>{{ account.office }}</td>
                        <td>{{ account.department }}</td>                       
                        <td>
                            <b-badge variant="info" class="p-1">{{ account.level }}</b-badge> 
                            <span v-if="account.active"> | <b-badge variant="success" class="p-1">active</b-badge></span>
                            <span v-else> | <b-badge variant="success" class="p-1">deactivate</b-badge></span>
                        </td>
                        <td>
                            <nuxt-link :to="'/admin/accounts/' + account.id + '-' + account.username + ''" tag="a"><font-awesome-icon icon="eye" /></nuxt-link>
                        </td>  
                </tr>
                You have nobody registered yet
            </tbody>
        </table>

        <!-- New User Modal -->
        <b-modal 
        ref="addUserModal" 
        title="Register a New User"
        size="lg"
        @ok="handleOk"
        centered
        >

            <signup-login 
            :login="login"
            :form="form"
            :authHandle="handleOk"/>

        </b-modal>
        <!-- /New User Modal -->

    </div>
</template>

<script>
import SignupLogin from '~/components/auth/signuplogin'
export default {
    data() {
        return {
            accounts: [],
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
    mounted() {
        this.$axios.$get('accounts/', { headers: this.$store.getters['authHeader'] })
        .then(res => {
             res.forEach(account => {
                let accountData = {}
                accountData['id'] = account.id
                accountData['active'] = account.active
                accountData['username'] = account.user.username
                accountData['userId'] = account.user.user_id
                accountData['userFullName'] = account.user.get_full_name
                accountData['title'] = account.title
                accountData['force_password_change'] = account.force_password_change
                accountData['city'] = account.city === null ? '--' : account.city.name 
                accountData['department'] = account.department === null ? '--' : account.department.name
                accountData['office'] = account.office === null ? '--' : account.office.name
                accountData['level'] = account.level === null ? '-' : account.level.level
                this.accounts.push(accountData)   
             });
        })
        .catch( err => console.log(err))
    },
    methods: {
        showModal() {
            this.resetForm()
            this.$refs['addUserModal'].show()
        },
        handleOk() {
            this.authHandle()
        },
        authHandle() {
            var data = {}
            data['username'] = this.form.username
            data['password'] = this.form.password
            data['password2'] = this.form.password2                
            data['firstname'] = this.form.firstname
            data['lastname'] = this.form.lastname
            data['email'] = this.form.email
            this.$store.dispatch('signUp', data)
        },
        resetForm() {            
            this.form.username = ''
            this.form.password = ''
            this.form.password2 = ''            
            this.form.firstname = ''
            this.form.lastname = ''
            this.form.email = ''
        }
    },
    components: {
        SignupLogin
    }
}
</script>