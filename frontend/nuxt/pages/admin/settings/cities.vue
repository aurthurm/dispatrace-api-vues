<template>
    <div>
        <h4>Cities <b-button variant="info" size="sm" class="ml-5" @click.stop.prevent="showCModal($event, { new: true })">+ City</b-button> </h4>
        <hr>
        <b-table striped hover :items="items" :fields="fields">            
            <template v-slot:cell(offices)="data">
                <span v-for="branch in data.item.offices" :key="branch.id"> {{ branch.name }},</span>
            </template>

            <template v-slot:cell(action)="data">
                <a href="#" @click.stop.prevent="showCModal($event, { new: false, item: data.item })"><font-awesome-icon icon="edit" /></a> | 
                <a href="#" @click.stop.prevent="deleteCity($event, { item: data.item })"><font-awesome-icon icon="times" /></a>
            </template>
        </b-table>
        <!-- Cities Modal -->
        <b-modal 
        ref="cityModal" 
        title="City"
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
                            <b-form-select 
                            id="categories"
                            ref="category"
                            v-model="form.country"
                            :options="options.countries.options"
                            size="sm"
                            >
                            </b-form-select>
                        </b-form-group>
                    </b-col>
                    <b-col></b-col>            
                </b-row>
                <b-row>
                    <b-col>
                        <b-form-group
                        id="fieldset-horizontal"
                        label-cols-sm="3"
                        label-cols-lg="2"
                        label-size="sm"
                        description="City Name"
                        label="City"
                        label-for="city"
                        invalid-feedback="title is required"
                        >
                            <b-form-input 
                            type="text"
                            id="city"
                            v-model="form.city"
                            required
                            ></b-form-input>
                        </b-form-group>
                    </b-col>    
                    <b-col>
                        <b-form-group
                        id="fieldset-horizontal"
                        label-cols-sm="3"
                        label-cols-lg="2"
                        label-size="sm"
                        description="City Abbreviation"
                        label="Abbr"
                        label-for="abbreviation"
                        invalid-feedback="title is required"
                        >
                            <b-form-input 
                            type="text"
                            id="abbreviation"
                            v-model="form.abbreviation"
                            required
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
                        description="Branches/Offices"
                        label="Branches"
                        label-for="office"
                        invalid-feedback="title is required"
                        >
                            <b-form-select 
                            id="office"
                            ref="office"
                            v-model="form.offices"
                            :options="options.offices.options"
                            size="sm"
                            multiple
                            :select-size="options.offices.options.length"
                            >
                            </b-form-select>
                        </b-form-group>
                    </b-col>
                </b-row>
                <slot></slot>
            </b-form>
        </b-modal>
        <!-- / Cities Modal -->
    </div>
</template>

<script>
  export default {
    data() {
      return {
        fields: [
            { key: 'name', label: 'City' }, 
            'abbreviation',  
            { key: 'offices', label: 'Branches'},
            'action'
        ],
        items: [],
        new: true,
        form: {
            country: {},
            city: '',
            id: null,
            offices: [],
            abbreviation: ''
        },
        options: {
            countries: {
                options: [
                    { value: null, text: "Select a Country" },
                ]
            },
            offices: {
                options: [
                    { value: null, text: "Select some Office(s)" },
                ]
            }
        }
      }
    },
    methods: {
        showCModal(event, data) {            
            this.new = data.new
            
            this.form.offices = []
            if(!data.new){
                this.form.country = data.item.country
                this.form.city = data.item.name
                this.form.abbreviation = data.item.abbreviation
                this.form.id = data.item.id
                data.item.offices.forEach(office => {
                    this.form.offices.push(office.id)
                })
            } else {
                this.form.country = ''
                this.form.city = ''
                this.form.abbreviation = ''
            }
            console.log(this.form.offices)
            this.$refs['cityModal'].show()
        },
        handleOk() {
           this.handleSubmit()
        },
        handleSubmit() {            
            let axiosMethod = this.new ? this.$axios.$post : this.$axios.$put
            axiosMethod('accounts/city-settings/', this.form, { headers: this.$store.getters['authHeader'] })
            .then(res => {
                this.items = res
                console.log(res)
            })
            .catch(err => console.log(err))
        },
        deleteCity(event, data) {
            this.$axios.delete('accounts/city-settings/' + data.item.id  + '/', { headers: this.$store.getters['authHeader'] })
            .then(res => {
                 this.items = res.data
            })
            .catch(err => console.log(err))
        }
    },
    mounted() {
        this.$axios.get('accounts/city-settings/', { headers: this.$store.getters['authHeader'] } )
        .then(res => {
            this.items = res.data
        })
        .catch(err => console.log(err))
        // initialise countries
        this.options.countries.options = [{ value: null, text: "Select a Country" }]
        this.$axios.get('accounts/country-settings/', { headers: this.$store.getters['authHeader'] } )
        .then(res => {
            res.data.forEach(country => {
                this.options.countries.options.push({ value: country.id,  text: country.name })
            });
        })
        .catch(err => console.log(err))
        // initialise offices
        this.options.offices.options = [{ value: null, text: "Select some Office(s)" }]
        this.$axios.get('accounts/office-settings/', { headers: this.$store.getters['authHeader'] } )
        .then(res => {
            res.data.forEach(office => {
                this.options.offices.options.push({ value: office.id,  text: office.name })
            });
        })
        .catch(err => console.log(err))
    }
  }
</script>