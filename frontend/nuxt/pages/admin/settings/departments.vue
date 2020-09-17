<template>
    <div>
        <h4>Departments <b-button variant="info" size="sm" class="ml-5" @click.stop.prevent="showOModal($event, { new: true })">+ Department</b-button> </h4>
        <hr>
        <b-table striped hover :items="items" :fields="fields">
            <template v-slot:cell(action)="data">
                <a href="#" @click.stop.prevent="showOModal($event, { new: false, item: data.item })"><font-awesome-icon icon="edit" /></a> | 
                <a href="#" @click.stop.prevent="deleteOffice($event, { item: data.item })"><font-awesome-icon icon="times" /></a>
            </template>
        </b-table>
        <!-- Cities Modal -->
        <b-modal 
        ref="departmentModal" 
        title="Department"
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
                        description="Department Name"
                        label="Dept"
                        label-for="department"
                        invalid-feedback="title is required"
                        >
                            <b-form-input 
                            id="department"
                            ref="department"
                            v-model="form.department"
                            size="sm"
                            >
                            </b-form-input>
                        </b-form-group>
                    </b-col>
                    <b-col>
                        <b-form-group
                        id="fieldset-horizontal"
                        label-cols-sm="3"
                        label-cols-lg="2"
                        label-size="sm"
                        description="Dept Abbr"
                        label="Abbr"
                        label-for="abbreviation"
                        invalid-feedback="title is required"
                        >
                            <b-form-input 
                            id="abbreviation"
                            ref="abbreviation"
                            v-model="form.abbreviation"
                            size="sm"
                            >
                            </b-form-input>
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
            { key: 'name', label: 'Department' }, 
            'abbreviation',  
            'action'
        ],
        items: [],
        new: true,
        form: {
            id: null,
            abbreviation: ''
        }
      }
    },
    methods: {
        showOModal(event, data) {            
            this.new = data.new
            if(!data.new){
                this.form.abbreviation = data.item.abbreviation
                this.form.department = data.item.name
                this.form.id = data.item.id
            } else {
                this.form.abbreviation = ''
                this.form.department = ''
                this.form.id = null
            }
            this.$refs['departmentModal'].show()
        },
        handleOk() {
           this.handleSubmit()
        //    console.log(this.form)
        },
        handleSubmit() {            
            let axiosMethod = this.new ? this.$axios.$post : this.$axios.$put
            axiosMethod('accounts/department-settings/', this.form, { headers: this.$store.getters['authHeader'] })
            .then(res => {
                this.items = res
            })
            .catch(err => console.log(err))
        },
        deleteOffice(event, data) {
            this.$axios.delete('accounts/department-settings/' + data.item.id  + '/', { headers: this.$store.getters['authHeader'] })
            .then(res => {
                 this.items = res.data
            })
            .catch(err => console.log(err))
        }
    },
    mounted() {
        this.$axios.get('accounts/department-settings/', { headers: this.$store.getters['authHeader'] } )
        .then(res => {
            this.items = res.data
        })
        .catch(err => console.log(err))
    }
  }
</script>