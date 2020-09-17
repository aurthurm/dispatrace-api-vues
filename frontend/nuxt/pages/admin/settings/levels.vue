<template>
    <div>
        <h4>User Levels <b-button variant="info" size="sm" class="ml-5" @click.stop.prevent="showLModal($event, { new: true })">+ Level</b-button> </h4>
        <hr>
        <b-table striped hover :items="items" :fields="fields">
            <template v-slot:cell(action)="data">
                <a href="#" @click.stop.prevent="showLModal($event, { new: false, item: data.item })"><font-awesome-icon icon="edit" /></a> | 
                <a href="#" @click.stop.prevent="deleteOffice($event, { item: data.item })"><font-awesome-icon icon="times" /></a>
            </template>
        </b-table>
        <!-- Cities Modal -->
        <b-modal 
        ref="levelModal" 
        title="User Level"
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
                        description="Level Name"
                        label="Level"
                        label-for="levelname"
                        invalid-feedback="title is required"
                        >
                            <b-form-input 
                            id="levelname"
                            ref="levelname"
                            v-model="form.levelname"
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
                        description="Level e.g 1, 2, 3"
                        label="Level"
                        label-for="level"
                        invalid-feedback="title is required"
                        >
                            <b-form-input 
                            id="level"
                            ref="level"
                            v-model="form.level"
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
            { key: 'name', label: 'Level Name' }, 
            'level',  
            'action'
        ],
        items: [],
        new: true,
        form: {
            levelname: '',
            level: '',
            id: null,
        }
      }
    },
    methods: {
        showLModal(event, data) {            
            this.new = data.new
            if(!data.new){
                this.form.levelname = data.item.name
                this.form.level = data.item.level
                this.form.id = data.item.id
            } else {
                this.form.levelname = ''
                this.form.level = ''
                this.form.id = null
            }
            this.$refs['levelModal'].show()
        },
        handleOk() {
           this.handleSubmit()
        },
        handleSubmit() {            
            let axiosMethod = this.new ? this.$axios.$post : this.$axios.$put
            axiosMethod('accounts/level-settings/', this.form, { headers: this.$store.getters['authHeader'] })
            .then(res => {
                this.items = res
            })
            .catch(err => console.log(err))
        },
        deleteOffice(event, data) {
            this.$axios.delete('accounts/level-settings/' + data.item.id  + '/', { headers: this.$store.getters['authHeader'] })
            .then(res => {
                 this.items = res.data
            })
            .catch(err => console.log(err))
        }
    },
    mounted() {
        this.$axios.get('accounts/level-settings/', { headers: this.$store.getters['authHeader'] } )
        .then(res => {
            this.items = res.data
        })
        .catch(err => console.log(err))
    }
  }
</script>