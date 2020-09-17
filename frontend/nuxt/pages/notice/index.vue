<template>
    <b-container fluid>
        <H4>NOTICES MANAGER 
            <b-button class="mb-2 float-right" variant="success" @click="showCatModal($event, { catid: null, new: true })" >New Category</b-button>
        </H4>
        <hr>
       <!-- Notices Categories -->
       <b-row>
           <b-col 
            v-for="category in categories"
            :key="category.id"
            md="4" class="mb-3">
               <b-card  bg-variant="light">
                    <template v-slot:header>
                        <span class="d-flex justify-content-between">
                            <h5>{{ category.title }}</h5>
                            <span>
                              <a href="#" @click.stop.prevent="showCatModal($event, { catid: category.id, new: false , title: category.title })"><font-awesome-icon icon="edit" /></a>
                                | 
                              <a href="#" @click.stop.prevent="deleteCategory($event, { catid: category.id })"><font-awesome-icon icon="times" /></a>
                            </span>
                        </span>
                    </template>

                    <b-card-text 
                    v-for="notice in category.notice_categories"
                    :key="notice.id"
                    class="d-flex justify-content-between">
                       <span>{{ notice.title }}</span>
                       <span>
                           <a href="#" @click.stop.prevent="noticeModal($event, { notice, new: false })"><font-awesome-icon icon="edit" /></a> | 
                           <a href="#" @click.stop.prevent="viewNotice($event, { notice })"><font-awesome-icon icon="eye" /></a> | 
                           <a href="#" @click.stop.prevent="deleteNotice($event, { noticeid: notice.id })"><font-awesome-icon icon="times" /></a>
                        </span>
                    </b-card-text>

                    <template v-slot:footer>
                        <span><a href="#" @click.stop.prevent="noticeModal($event, { notice, new: true })">+ Add Notice</a></span>
                    </template>
               </b-card>

           </b-col>
       </b-row>
       <hr>
       <!-- Notices Expires -->
       <b-container fluid>
            <b-card bg-variant="warning" header="Expired Notices" class="">

                <b-row>
                    <b-col
                    v-for="notice in expiredNotices"
                    :key="notice.id">
                        <b-card-text 
                        class="d-flex justify-content-between bg-light mb-2 px-1">
                            <span>{{ notice.title }}</span>
                            <span>
                                <a href="#" @click.stop.prevent="noticeModal($event, { notice, new: false })"><font-awesome-icon icon="edit" /></a> | 
                                <a href="#" @click.stop.prevent="viewNotice($event, { notice })"><font-awesome-icon icon="eye" /></a> | 
                                <a href="#" @click.stop.prevent="deleteNotice($event, { noticeid: notice.id })"><font-awesome-icon icon="times" /></a>
                            </span>
                        </b-card-text>
                    </b-col>
                </b-row>

            </b-card>
       </b-container>

       <!-- Category Modal -->
        <b-modal 
        ref="categorymodal" 
        title="Category"
        size="lg"
        @ok="handleCatOk"
        centered
        >
            <b-form ref="form" @submit.stop.prevent="handleCatSubmit">
                <b-row>
                    <b-col>
                        <b-form-group
                        id="fieldset-horizontal"
                        label-cols-sm="3"
                        label-cols-lg="2"
                        label-size="sm"
                        description="Title"
                        label="Title"
                        label-for="category"
                        invalid-feedback="title is required"
                        >
                            <b-form-input 
                            id="category"
                            v-model="categoryTitle"
                            required
                            ></b-form-input>
                        </b-form-group>
                    </b-col>                
                </b-row>
                <slot></slot>
            </b-form>
        </b-modal>
       <!--  / Category Modal -->

       <!-- Noice View Modal -->
        <b-modal 
        ref="noticeViewmodal" 
        title="Notice Preview"
        size="lg"
        centered
        >
            <h4>{{ noticePreview.title }}</h4>
            <b-card-text >
                {{ noticePreview.description }}
            </b-card-text>
        </b-modal>
       <!--  / Notice View Modal-->

       <!-- Noice Modal -->
        <b-modal 
        ref="noticeModal" 
        title="Notice Preview"
        size="lg"
        centered
        @ok="handleNoticeOk"
        >
                <b-card bg-variant="light">
                    <b-form >
                        <b-row>
                            <b-col>
                                <b-form-group
                                id="fieldset-horizontal"
                                label-size="sm"
                                label="title:"
                                label-for="title"
                                >
                                    <b-form-input 
                                    id="title"
                                    v-model="notice.title"
                                    size="sm"
                                    ></b-form-input>
                                </b-form-group>
                            </b-col>
                            <b-col>
                                <b-form-group
                                id="fieldset-horizontal"
                                label-size="sm"
                                label="expiry:"
                                label-for="expiry"
                                >
                                    <b-form-input 
                                    id="expiry"
                                    v-model="notice.expiry"
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
                                label="City:"
                                label-for="city"
                                >
                                    <b-form-select 
                                    id="city"
                                    ref="city"
                                    v-model="notice.city.value"
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
                                    v-model="notice.office.value"
                                    :options="options.offices.options"
                                    @change="onOfficeUpdate"
                                    size="sm"
                                    >
                                    </b-form-select>
                                </b-form-group>
                            </b-col>
                            <b-col v-if="notice.office != null">
                                <b-form-group
                                id="fieldset-horizontal"
                                label-size="sm"
                                label="department:"
                                label-for="department"
                                >
                                    <b-form-select 
                                    id="department"
                                    ref="department"
                                    v-model="notice.department.value"
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
                                label="categories:"
                                label-for="categories"
                                >
                                    <b-form-select 
                                    id="categories"
                                    ref="category"
                                    v-model="notice.category.value"
                                    :options="options.categories.options"
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
                                label="description:"
                                label-for="description"
                                >
                                    <b-form-textarea 
                                    id="description"
                                    ref="description"
                                    v-model="notice.description"
                                    size="sm"
                                    >
                                    </b-form-textarea>
                                </b-form-group>
                            </b-col>
                        </b-row>
                        <!-- <b-button type="submit" variant="primary" class="float-left" @click.stop.prevent="noticeUpdate">Submit Notice</b-button> -->
                        <slot></slot>
                    </b-form>
                </b-card>   
        </b-modal>
       <!--  / Notice Modal-->







    </b-container>
</template>

<script>
export default {
    props: {
        showModal: Function
    },
    data() {
        return {
            categoryTitle: '',
            newCategory: true,
            editCategoryId: null,
            categories: [],
            expiredNotices: [],
            noticePreview: {},
            newNotice: false,
            notice: { 
                id: null,          
                city: {},     
                office: {},
                department: {},
                category: {}
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
                categories: {
                    options: [
                        { value: null, text: "Select a Category" },
                    ]
                }
            }
        }
    },
    methods: {            
        showCatModal(event, data) {
            this.newCategory = data.new
            this.editCategoryId = data.catid
            this.$refs['categorymodal'].show()
            if(!this.newCategory){
              this.categoryTitle = data.title
            }
        },
        handleCatOk(bvModalEvt){
            bvModalEvt.preventDefault();
            this.handleCatSubmit()            
        },
        handleCatSubmit(){
            let axiosMethod = this.newCategory ? this.$axios.$post : this.$axios.$put
            let data = {}
            data['title'] = this.categoryTitle
            if(!this.newCategory){
                data['id'] = this.editCategoryId
            }
            axiosMethod('notices/category/', data, { headers: this.$store.getters['authHeader'] })
            .then(res => {
                 this.$refs['categorymodal'].hide()
                 this.segregateNotices(res)
                 this.categoryTitle = ''
                if(this.newCategory){
                    data['id'] = null
                }
            })
            .catch(err => console.log(err))
        },
        deleteCategory(event, data){
            let candelete = this.categories.filter(x => x.id === data.catid)
            .map(x => x.notice_categories.length === 0)
            if(candelete[0]){
                let categoryId = data.catid
                this.$axios.$delete('notices/category/' + categoryId + '/', { headers: this.$store.getters['authHeader'] })
                .then(res => this.segregateNotices(res))
                .catch(err => console.log(err))
            } else {
                alert("You can not delete a category with notices !!!")
            }    
        },
        updateCategory(event, data){
            let categoryId = data.catid
            this.$axios.$delete('notices/category/' + categoryId + '/', { headers: this.$store.getters['authHeader'] })
            .then(res => this.segregateNotices(res))
            .catch(err => console.log(err))    
        },
        segregateNotices(categories){
            categories.forEach(category => {
                let notices = category.notice_categories
                category.notice_categories = []
                this.expiredNotices = []
                notices.forEach( notice => {                    
                    let noticeDestination = new Date(notice.expiry) < Date.now() ? this.expiredNotices : category.notice_categories
                    noticeDestination.push(notice)
                })
            })
            this.categories = [...categories]
        },
        getNotices() {
            this.$axios.$get('notices/categories/', { headers: this.$store.getters['authHeader'] })
            .then(res => this.segregateNotices(res))
            .catch(err => console.log(err))            
        },
        deleteNotice(event, data){
            let noticeid = data.noticeid
            this.$axios.$delete('notices/notice/' + noticeid + '/', { headers: this.$store.getters['authHeader'] })
            .then(res => this.segregateNotices(res))
            .catch(err => console.log(err))              
        },
        viewNotice(event, data) {     
            this.noticePreview = {}
            this.$refs['noticeViewmodal'].show()
            this.noticePreview.title = data.notice.title  
            this.noticePreview.description = data.notice.description
        },
        initUpdate() {
           // Initialise Cities           
            this.options.cities.options = [{ value: null, text: "Select a City"}]  
            this.$axios.$get('accounts/cities/', { headers: this.$store.getters['authHeader'] })
            .then(res => {
                res.forEach(city => {
                    this.options.cities.options.push({ value: city.id, text: city.name})
                });
            })
            .catch( err => console.log(err))
            // Initialise Ctaegories   
            this.options.categories.options = [{ value: null, text: "Select a Category"}]
            this.categories.forEach(category => {
                this.options.categories.options.push({ value: category.id, text: category.title})
            });
        },
        onCityUpdate() {
            // initialise offices
            this.options.offices.options = [{ value: null, text: "Select an Office"}]
            // initialise departments
            this.options.departments.options = [{ value: null, text: "Select a Department"}]
            this.$axios.$get('accounts/offices?city=' + this.notice.city.value, { headers: this.$store.getters['authHeader'] })
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
            this.$axios.$get('accounts/departments?office=' + this.notice.office.value, { headers: this.$store.getters['authHeader'] })
            .then(res => {
                // add new options
                res.forEach(department => {
                    this.options.departments.options.push({ value: department.id, text: department.name})
                });
            })
            .catch( err => console.log(err))         
        },
        handleNoticeOk(bvModalEvt){
            bvModalEvt.preventDefault();
            this.handleNoticeSubmit()            
        },
        noticeModal(event, data) {   
            this.newNotice = data.new
           // Initialise Empty object if NEW  
           if(this.newNotice) {
                this.notice.city = {} 
                this.notice.office = {} 
                this.notice.department = {}
                this.notice.title = ''
                this.notice.description = ''
                this.notice.expiry = ''
           } else {
                let notice = data.notice
                this.notice.id = notice.id
                this.notice.city = { value: notice.city, text: '' }
                this.notice.office = { value: notice.office, text: '' }
                this.notice.department = { value: notice.department, text: '' }
                this.notice.title = notice.title
                this.notice.description = notice.description
                this.notice.expiry = notice.expiry                 
                this.$axios.$get('accounts/offices?city=' + notice.city, { headers: this.$store.getters['authHeader'] })
                .then(res => {
                    res.forEach(office => {
                        this.options.offices.options.push({ id: office.id, text: office.name})
                    });
                })
                this.$axios.$get('accounts/departments?office=' + notice.office, { headers: this.$store.getters['authHeader'] })
                .then(res => {
                    res.forEach(department => {
                        this.options.departments.options.push({ id: department.id, text: department.name})
                    });
                })
           }
            this.notice.category = { value: data.notice.category, text: ''}
            this.initUpdate()   
            this.$refs['noticeModal'].show()
        },
        handleNoticeSubmit(){
            let axiosMethod = this.newNotice ? this.$axios.$post : this.$axios.$put
            axiosMethod('notices/notice/', { notice_data: this.notice }, { headers: this.$store.getters['authHeader'] })
            .then(res => {
                 this.$refs['noticeModal'].hide()
                 this.segregateNotices(res)
            })
            .catch(err => console.log(err))
        }
    },
    mounted() {
        this.getNotices()
    }
}
</script>