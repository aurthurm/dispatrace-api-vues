<template>
    <div>
        <h4>Country <b-button variant="info" size="sm" class="ml-5" @click.stop.prevent="showCModal($event, { new: true })">+ Country</b-button> </h4>
        <hr>
        <b-table striped hover :items="items" :fields="fields">            
            <template v-slot:cell(action)="data">
                <a href="#" @click.stop.prevent="showCModal($event, { new: false, item: data.item })"><font-awesome-icon icon="edit" /></a> | 
                <a href="#" @click.stop.prevent="deleteCountry($event, { item: data.item })"><font-awesome-icon icon="times" /></a>
            </template>
        </b-table>
        <!-- Country Modal -->
        <b-modal 
        ref="countryModal" 
        title="Country"
        size="lg"
        @ok="handleOk"
        centered
        >
            <b-form  @submit.stop.prevent="handleSubmit">
                <b-row>
                    <b-col>
                        <b-form-group
                        id="fieldset-horizontal"
                        label-cols-sm="3"
                        label-cols-lg="2"
                        label-size="sm"
                        description="Country Name"
                        label="Country"
                        label-for="country"
                        invalid-feedback="title is required"
                        >
                            <b-form-input 
                            type="text"
                            id="country"
                            v-model="form.country"
                            required
                            ></b-form-input>
                        </b-form-group>
                    </b-col>              
                </b-row>
                <slot></slot>
            </b-form>
        </b-modal>
        <!-- / Country Modal -->
    </div>
</template>

<script>
  export default {
    data() {
        return {
            fields: ['name', 'action'],
            items: [], //  e.g { id: 1, name: 'Zimbabwe' }
            new: true,
            form: {
                country: '',
                id: null
            }
        }
    },
    methods: {
        showCModal(event, data) {            
            this.new = data.new
            if(!data.new){
                this.form.country = data.item.name
                this.form.id = data.item.id
            } else {
                this.form.country = ''
            }
            this.$refs['countryModal'].show()
        },
        handleOk() {
           this.handleSubmit()
        },
        handleSubmit() {            
            let axiosMethod = this.new ? this.$axios.$post : this.$axios.$put
            let data = {}
            data['country'] = this.form.country
            if(!this.new){
                data['id'] = this.form.id
            }
            axiosMethod('accounts/country-settings/', data, { headers: this.$store.getters['authHeader'] })
            .then(res => {
                this.items = res
            })
            .catch(err => console.log(err))
        },
        deleteCountry(event, data) {
            this.$axios.delete('accounts/country-settings/' + data.item.id  + '/', { headers: this.$store.getters['authHeader'] })
            .then(res => {
                 this.items = res.data
            })
            .catch(err => console.log(err))
        }
    },
    mounted() {
        this.$axios.get('accounts/country-settings/', { headers: this.$store.getters['authHeader'] } )
        .then(res => {
            this.items = res.data
        })
        .catch(err => console.log(err))
    }
  }
</script>