<template>
    <div>
        <h4>Branches <b-button variant="info" size="sm" class="ml-5" @click.stop.prevent="showOModal($event, { new: true })">+ Branch</b-button> </h4>
        <hr>
        <b-table striped hover :items="items" :fields="fields">            
            <template v-slot:cell(departments)="data">
                <span v-for="department in data.item.departments" :key="department.id"> {{ department.name }},</span>
            </template>

            <template v-slot:cell(action)="data">
                <a href="#" @click.stop.prevent="showOModal($event, { new: false, item: data.item })"><font-awesome-icon icon="edit" /></a> | 
                <a href="#" @click.stop.prevent="deleteOffice($event, { item: data.item })"><font-awesome-icon icon="times" /></a>
            </template>
        </b-table>
        <!-- Cities Modal -->
        <b-modal 
        ref="officeModal" 
        title="Branch/Office"
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
                            @change="onCountryUpdate"
                            >
                            </b-form-select>
                        </b-form-group>
                    </b-col>
                    <b-col>
                        <b-form-group
                        id="fieldset-horizontal"
                        label-cols-sm="3"
                        label-cols-lg="2"
                        label-size="sm"
                        description="City Name"
                        label="city"
                        label-for="city"
                        invalid-feedback="title is required"
                        >
                            <b-form-select 
                            id="city"
                            ref="city"
                            v-model="form.city"
                            :options="options.cities.options"
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
                        description="Branch Name"
                        label="Branch"
                        label-for="branch"
                        invalid-feedback="title is required"
                        >
                            <b-form-input 
                            type="text"
                            id="city"
                            v-model="form.branch"
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
                        description="branch Abbreviation"
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
                            v-model="form.departments"
                            :options="options.departments.options"
                            size="sm"
                            multiple
                            :select-size="options.departments.options.length"
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
            { key: 'name', label: 'Branch' }, 
            'abbreviation',  
            'departments',
            'action'
        ],
        items: [],
        new: true,
        form: {
            country: {},
            city: {},
            branch: '',
            id: null,
            abbreviation: '',
            departments: []
        },
        options: {
            countries: {
                options: [
                    { value: null, text: "Select a Country" },
                ]
            },
            cities: {
                options: [
                    { value: null, text: "Select a City" },
                ]
            },
            departments: {
                options: [
                    { value: null, text: "Select some Department(s)" },
                ]
            }
        }
      }
    },
    methods: {
        onCountryUpdate(){
            this.options.cities.options = [{ value: null, text: "Select a City"}]
            this.$axios.$get('accounts/cities?country=' + this.form.country, { headers: this.$store.getters['authHeader'] })
            .then(res => {
                res.forEach(city => {
                    this.options.cities.options.push({ value: city.id, text: city.name})
                });
            })
            .catch( err => console.log(err))  
            
        },
        showOModal(event, data) {            
            this.new = data.new
            this.form.departments = []
            if(!data.new){
                this.form.country = data.item.country
                this.form.city = data.item.city
                this.form.branch = data.item.name
                this.form.abbreviation = data.item.abbreviation
                this.form.id = data.item.id
                this.onCountryUpdate()
                data.item.departments.forEach(department => {
                    this.form.departments.push(department.id)
                })
            } else {
                this.form.country = ''
                this.form.city = ''
                this.form.branch = ''
                this.form.abbreviation = ''
            }
            this.$refs['officeModal'].show()
        },
        handleOk() {
           this.handleSubmit()
        //    console.log(this.form)
        },
        handleSubmit() {            
            let axiosMethod = this.new ? this.$axios.$post : this.$axios.$put
            axiosMethod('accounts/office-settings/', this.form, { headers: this.$store.getters['authHeader'] })
            .then(res => {
                this.items = res
            })
            .catch(err => console.log(err))
        },
        deleteOffice(event, data) {
            this.$axios.delete('accounts/office-settings/' + data.item.id  + '/', { headers: this.$store.getters['authHeader'] })
            .then(res => {
                 this.items = res.data
            })
            .catch(err => console.log(err))
        }
    },
    mounted() {
        this.$axios.get('accounts/office-settings/', { headers: this.$store.getters['authHeader'] } )
        .then(res => {
            this.items = res.data
        })
        .catch(err => console.log(err))
        // initialise country
        this.options.countries.options = [{ value: null, text: "Select a Country" }]
        this.$axios.get('accounts/country-settings/', { headers: this.$store.getters['authHeader'] } )
        .then(res => {
            res.data.forEach(country => {
                this.options.countries.options.push({ value: country.id,  text: country.name })
            });
        })
        .catch(err => console.log(err))
        // initialise departments
        this.options.departments.options = [{ value: null, text: "Select some Office(s)" }]
        this.$axios.get('accounts/department-settings/', { headers: this.$store.getters['authHeader'] } )
        .then(res => {
            res.data.forEach(department => {
                this.options.departments.options.push({ value: department.id,  text: department.name })
            });
        })
        .catch(err => console.log(err))
    }
  }
</script>