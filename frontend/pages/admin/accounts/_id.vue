<template>
    <div class="container">
        <h4>Account Profile Detail</h4>
        <hr>
        <div class="row mb-5">
            <div class="col-md-4">
                <div class="card card-outline-dark p-2">
                    <h4 class="text-center">
                        {{ account.user.get_full_name }}					
                        <span class="float-right mr-auto" v-if="!editProfile">
                            <a class="text-dark btn btn-outline-info" href="#" @click.stop.prevent="initUpdate"><span><font-awesome-icon icon="edit" /></span></a>
                        </span>
                    </h4>
                    <table class="table mt-2" >
                        <!-- <thead>
                            <tr>
                                <th></th>    
                                <th></th>
                            </tr>
                        </thead> -->
                        <tbody>
                            <tr>
                                <td class="text-dark">Username</td>
                                <td class="text-dark">@{{ account.user.username }}</td>
                            </tr>
                            <tr>
                                <td class="text-dark">Email</td>
                                <td class="text-dark">{{ account.user.email }}</td>
                            </tr>
                            <tr>
                                <td class="text-dark">Permission Groups</td>
                                <td class="text-dark">
                                    <span class="mr-1" v-for="group in account.groups" :key="group.index">{{ group.name }}, </span></td>				                
                            </tr>
                            <tr>
                                <td class="text-dark">Title</td>
                                <td class="text-dark">{{ account.title }}</td>				                
                            </tr>
                            <tr>
                                <td class="text-dark">Level</td>
                                <td class="text-dark">{{ account.level.level }}</td>
                            </tr>
                            <tr>
                                <td class="text-dark">Department</td>
                                <td class="text-dark">{{ account.department.name }}</td>
                            </tr>
                            <tr>
                                <td class="text-dark">Office/Branch</td>
                                <td class="text-dark">{{ account.office.name }}</td>
                            </tr>
                            <tr>
                                <td class="text-dark">City</td>
                                <td class="text-dark">{{ account.city.name }}</td>
                            </tr>
                        </tbody>
                    </table>    
                    <button class="btn btn-outline-danger btn-sm" data-toggle="modal" data-target="#PasswordChangeModal">Reset Password</button>
                </div>
            </div>		
            <div class="col-md-8" v-if="editProfile">
                <h5>
                    Profile Edit                    					
                    <span class=" ml-5 text-danger">
                        <a class="text-dark btn btn-outline-info" href="#" @click.stop.prevent="editProfile = false"><span><font-awesome-icon icon="times" /></span></a>
                    </span>
                </h5>
                <hr>
                <b-card bg-variant="light">
                    <b-form >
                        <b-row>
                            <b-col>
                                <b-form-group
                                id="fieldset-horizontal"
                                label-size="sm"
                                label="firstname:"
                                label-for="firstaname"
                                >
                                    <b-form-input 
                                    id="firstname"
                                    v-model="account.firstname"
                                    size="sm"
                                    ></b-form-input>
                                </b-form-group>
                            </b-col>
                            <b-col>
                                <b-form-group
                                id="fieldset-horizontal"
                                label-size="sm"
                                label="lastname:"
                                label-for="lastname"
                                >
                                    <b-form-input 
                                    id="lastname"
                                    v-model="account.lastname"
                                    size="sm"
                                    ></b-form-input>
                                </b-form-group>
                            </b-col>
                        </b-row>

                        <b-row>
                            <b-col>
                                <b-form-group
                                id="fieldset-horizontal"
                                label-size="sm"
                                label="email:"
                                label-for="email"
                                >
                                    <b-form-input 
                                    id="email"
                                    v-model="account.email"
                                    size="sm"
                                    ></b-form-input>
                                </b-form-group>
                            </b-col>
                            <b-col>
                                <b-form-group
                                id="fieldset-horizontal"
                                label-size="sm"
                                label="job title:"
                                label-for="title"
                                >
                                    <b-form-input 
                                    id="title"
                                    v-model="account.title"
                                    size="sm"
                                    ></b-form-input>
                                </b-form-group>
                            </b-col>
                            <b-col >
                                <b-form-group
                                id="fieldset-horizontal"
                                label-size="sm"
                                label="level:"
                                label-for="level"
                                >
                                    <b-form-select 
                                    id="level"
                                    v-model="account.level.id"
                                    :options="options.levels.options"
                                    size="sm"
                                    >
                                    </b-form-select>
                                </b-form-group>
                            </b-col>
                        </b-row>

                        <b-row>
                            <b-col>
                                <b-form-group
                                id="fieldset-horizontal"
                                label-size="sm"
                                label="City:"
                                label-for="city"
                                >
                                    <b-form-select 
                                    id="city"
                                    ref="city"
                                    v-model="account.city.id"
                                    :options="options.cities.options"
                                    @change="onCityUpdate"
                                    size="sm"
                                    >
                                    </b-form-select>
                                </b-form-group>
                            </b-col>
                            <b-col >
                                <b-form-group
                                id="fieldset-horizontal"
                                label-size="sm"
                                label="Office:"
                                label-for="office"
                                >
                                    <b-form-select 
                                    id="office"
                                    ref="office"
                                    v-model="account.office.id"
                                    :options="options.offices.options"
                                    @change="onOfficeUpdate"
                                    size="sm"
                                    >
                                    </b-form-select>
                                </b-form-group>
                            </b-col>
                            <b-col v-if="account.office != null">
                                <b-form-group
                                id="fieldset-horizontal"
                                label-size="sm"
                                label="department:"
                                label-for="department"
                                >
                                    <b-form-select 
                                    id="department"
                                    ref="department"
                                    v-model="account.department.id"
                                    :options="options.departments.options"
                                    size="sm"
                                    >
                                    </b-form-select>
                                </b-form-group>
                            </b-col>
                        </b-row>               

                        <b-row>
                            <b-col>
                                <b-form-group
                                id="fieldset-horizontal"
                                label-cols-sm="3"
                                label-cols-lg="2"
                                label-size="sm"
                                label="groups:"
                                label-for="groups"
                                >
                                    <b-form-select 
                                    id="city"
                                    ref="city"
                                    v-model="account.groups"
                                    :options="options.groups.options"
                                    size="sm"
                                    multiple
                                    :select-size="options.groups.options.length"
                                    >
                                    </b-form-select>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <b-button type="submit" variant="primary" class="float-left" @click.stop.prevent="profileUpdate">Sign In</b-button>
                        <slot></slot>
                    </b-form>
                </b-card>                
            </div>
        </div>
        <!-- password reset modal -->
        <!-- / password reset modal --> 
    </div>
</template>


<script>
export default {    
    data() {
        return {
            editProfile: false,
            account: {
                user: '',
                firstname: '',
                lastname: '',
                title: '',
                email: '',
                department: '',
                city: '',
                office: '',
                level: '',
                groups: []
            },
            options: {                
                cities: {
                    options: [
                        { value: null, text: "Select a City" }
                    ]
                },                
                departments: {
                    options: [
                        { value: null, text: "Select a Department" },
                    ]
                },                
                offices: {
                    options: [
                        { value: null, text: "Select an Office" },
                    ]
                },                
                levels: {
                    options: [
                        { value: null, text: "Select a level" },
                    ]
                },                
                groups: {
                    options: [
                        { value: null, text: "Select a Group" },
                    ]
                }
            }
        }
    },
    mounted() {
        this.$axios.$get('accounts/' + this.$route.params.id.split('-')[0] + '/', { headers: this.$store.getters['authHeader'] })
        .then(res => {
            this.account = res
            this.account.firstname = this.account.user.first_name
            this.account.lastname = this.account.user.last_name
            this.account.email = this.account.user.email
        })
        .catch( err => console.log(err))
    },
    methods: {
        initUpdate() {
            this.editProfile = true
            console.log('initialise cities')   
            this.$axios.$get('accounts/cities/', { headers: this.$store.getters['authHeader'] })
            .then(res => {
                res.forEach(city => {
                    this.options.cities.options.push({ value: city.id, text: city.name})
                });
            })
            .catch( err => console.log(err))   
            console.log('initialise levels')   
            this.$axios.$get('accounts/levels/', { headers: this.$store.getters['authHeader'] })
            .then(res => {
                res.forEach(level => {
                    this.options.levels.options.push({ value: level.id, text: level.level})
                });
            })
            .catch( err => console.log(err))     
            console.log('initialise groups')   
            this.$axios.$get('accounts/groups/', { headers: this.$store.getters['authHeader'] })
            .then(res => {
                res.forEach(group => {
                    this.options.groups.options.push({ value: { id: group.id, name: group.name }, text: group.name })
                });
            })
            .catch( err => console.log(err))   
            
            // Init  Offices Option default
            this.options.offices.options.push({ value: this.account.office.id, text: this.account.office.name })
            // Init  department Option default
            this.options.departments.options.push({ value: this.account.department.id, text: this.account.department.name })
        },
        onCityUpdate() {
            // initialise offices
            this.options.offices.options = [{ value: null, text: "Select an Office"}]
            // initialise departments
            this.options.departments.options = [{ value: null, text: "Select a Department"}]
            console.log('initialise offices for city', this.account.city)   
            this.$axios.$get('accounts/offices?city=' + this.account.city.id, { headers: this.$store.getters['authHeader'] })
            .then(res => {
                res.forEach(office => {
                    this.options.offices.options.push({ value: office.id, text: office.name})
                });
            })
            .catch( err => console.log(err))         
        },
        onOfficeUpdate() {
            // initialise departments
            this.options.departments.options = [{ value: null, text: "Select a Department"}]
            console.log('initialise departmnets for office', this.account.office)   
            this.$axios.$get('accounts/departments?office=' + this.account.office.id, { headers: this.$store.getters['authHeader'] })
            .then(res => {
                // add new options
                res.forEach(department => {
                    this.options.departments.options.push({ value: department.id, text: department.name})
                });
            })
            .catch( err => console.log(err))         
        },
        profileUpdate() { 
            console.log(this.account)
            this.$axios.$put('accounts/' + this.$route.params.id.split('-')[0] + '/', {  account_data: this.account  }, { headers: this.$store.getters['authHeader']})
            .then(res => {
                console.log(res)
            })
            .catch( err => console.log(err))  
            // this.editProfile = false
        }
    },
    watch: {

    }
}
</script>