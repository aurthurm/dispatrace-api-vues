<template>
    <div>
        <hr>
        <section >
            <b-card bg-variant="light">
                <b-form >
                    <b-row>
                        <b-col>
                            <b-form-group
                            id="fieldset-horizontal"
                            label-cols-sm="3"
                            label-cols-lg="2"
                            label-size="sm"
                            label="Username:"
                            label-for="username"
                            >
                                <b-form-input 
                                id="username"
                                :class="viewMessage ? 'border-danger' : ''"
                                v-model="form.username"
                                ></b-form-input>
                            </b-form-group>
                        </b-col>
                        <b-col v-if="!login">
                            <b-form-group
                            id="fieldset-horizontal"
                            label-cols-sm="4"
                            label-cols-lg="3"
                            label-size="sm"
                            label="Email Adress:"
                            label-for="email"
                            >
                                <b-form-input 
                                id="email"
                                v-model="form.email"
                                ></b-form-input>
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
                            label="Password:"
                            label-for="password"
                            >
                            <b-form-input 
                            id="password"
                            type="password"
                            :class="viewMessage ? 'border-danger' : ''"
                            v-model="form.password"></b-form-input>
                            </b-form-group>
                        </b-col>
                        <b-col v-if="!login">
                            <b-form-group
                            id="fieldset-horizontal"
                            label-cols-sm="4"
                            label-cols-lg="3"
                            label-size="sm"
                            label="Password Confirm:"
                            label-for="password2"
                            >
                            <b-form-input 
                            id="password2"
                            type="password"
                            v-model="form.password2"></b-form-input>
                            </b-form-group>
                        </b-col>
                    </b-row>

                    <b-row v-if="!login">
                        <b-col>
                            <b-form-group
                            id="fieldset-horizontal"
                            label-cols-sm="3"
                            label-cols-lg="2"
                            label-size="sm"
                            label="First Name:"
                            label-for="firstname"
                            >
                            <b-form-input 
                            id="firstname"
                            v-model="form.firstname"></b-form-input>
                            </b-form-group>
                        </b-col>
                        <b-col v-if="!login">
                            <b-form-group
                            id="fieldset-horizontal"
                            label-cols-sm="4"
                            label-cols-lg="3"
                            label-size="sm"
                            label="Last Name:"
                            label-for="lastname"
                            >
                            <b-form-input 
                            id="lastname"
                            v-model="form.lastname"></b-form-input>
                            </b-form-group>
                        </b-col>
                    </b-row>
                    <b-button type="submit" variant="primary" class="float-left ml-5" v-if="login" @click.stop.prevent="authHandle">Sign In</b-button>
                    <b-button type="submit" variant="primary" class="float-left d-none" v-if="!login" @click.stop.prevent="authHandle">Sign Up</b-button>
                    <slot></slot>
                </b-form>
                <p class="text-danger" v-if="viewMessage">{{ message }}</p>
            </b-card>
        </section>
    </div>
</template>

<script>
export default {
    props: {
        login: Boolean,
        form: Object,
        authHandle: Function,
        message: String,
        viewMessage: Boolean
    }
}
</script>