<template>
    <div class="container-fluid">
        <div v-if="!isDetailView">
            <div class="d-flex justify-content-between align-content-center pt-2">
                <h3>
                    MEMORANDUMS 
                    <button class="text-dark btn fa-btn" type="button" @click="toggleMemoSubs">
                        <font-awesome-icon icon="bars" />
                    </button>                
                </h3>
                <b-nav-form v-if="showMemoSubs">
                    <b-form-input size="sm" class="mr-sm-2" v-model="searchQuery" placeholder="Search"></b-form-input>
                    <b-button size="sm" class="my-2 my-sm-0" type="submit" @click.prevent="memoSearch">Search</b-button>
                </b-nav-form>
            </div>
            <hr v-if="showMemoSubs">
            <section class="d-flex justify-content-between" v-if="showMemoSubs">
                <b-button 
                v-for="mstate in memoStates" 
                :variant="mstate.color" 
                :key="mstate.title"
                @click="getMemorandums($event, { memo_state: mstate.title })">
                    {{ mstate.title }}
                    <b-badge variant="light">{{ mstate.count }}</b-badge>
                </b-button>    
                <b-button variant="outline-success" @click="startNewMemo">+ NEW</b-button>
            </section>
            <hr>
            <h4 v-if="selectedState != ''">{{ selectedState }} ...</h4>        
            <h4 v-else>NEW MEMO</h4>
            <hr>
        </div>
        <section id="dynamic-wrapper">
            <nuxt-child
                v-if="!newMemo"
                :results="results"
                :truncate="truncate" 
                :showMemoSubs="showMemoSubs" 
                :getMemorandums="getMemorandums"/>

            <Create 
                :form="form"
                :onSubmit="onSubmit"
                :onReset="onReset"
                :config="config"
                v-else>        
            <b-button type="reset" variant="danger">Reset</b-button>
            </Create>
        </section> 
    </div>
</template>

<script>
import Create from '~/components/memo/Create'
import { mapGetters } from 'vuex';

export default {
    data() {
        return {
            searchQuery: '',
            newMemo: false,
            showMemoSubs: false,  
            form: {
                to: '',
                recipients: '',
                subject: '',
                priority: null,
                accesibility: null,
                commenting: null,
                content: null,
            },
            config: {
            // Get options from https://alex-d.github.io/Trumbowyg/documentation
            }
        }
    },
    computed: {        
        results: {
            get: (event) => event.$store.getters['memorandums/getMemos'],
            set: (value) => value
        },         
        searched: {
            get: (event) => event.$store.getters['memorandums/getSearchStatus'],
            set: (value) => value
        },        
        selectedState: {
            get: (event) => event.$store.getters['memorandums/getSelectedState'],
            set: (value) => value
        },       
        isDetailView: {
            get: (event) => event.$store.getters['memorandums/getMemoDetailView'],
            set: (value) => value
        },
        ...mapGetters({
            memoStates: 'memorandums/getMemoStates',
        })
    },
    watch: {
        results(newValue, oldValue){
            this.results = newValue
        },

        selectedState(newValue, oldValue){
            this.selectedState = newValue
        },

        isDetailView(newValue, oldValue){
            this.isDetailView = newValue
        }
    },
    methods: {
        startNewMemo() {
            this.newMemo = true
            this.$store.dispatch('memorandums/setSelectedState', 'NEW MEMORANDUM')
        },
        truncate(str, numberOfWords) {
            return str.replace(/(<([^>]+)>)/ig,"").split(/\s+/).slice(0, numberOfWords).join(" ") + " ...";
        },
        getMemorandums(event, data) {
            // Hackt
            // let route_path = this.$route.path;
            // if (route_path !== "/memo") {
            //     this.$router.push("/memo")
            // }
            // Done hacking         

            this.newMemo = false
            this.$store.dispatch('memorandums/setMemos', data)
            .then(() => {
                this.results = this.$store.getters['memorandums/getMemos']
                this.selectedState = this.$store.getters['memorandums/getSelectedState']
            })
        },
        memoSearch: function() {
            this.newMemo = false
            this.$store.dispatch('memorandums/setSelectedState', 'SEARCH ...')
            this.$store.dispatch('memorandums/setSearchResults', this.searchQuery)
            .then(() => {
                this.results = this.$store.getters['memorandums/getSearchResults']
            })
        },
        toggleMemoSubs: function() {
            this.showMemoSubs = !this.showMemoSubs
        },
        onSubmit(evt) {
            evt.preventDefault()
            console.log(this.form)
            this.$store.dispatch('memorandums/createMemorandum', this.form)
        },
        onReset(evt) {
            evt.preventDefault()
            this.form.to = ''
            this.form.recipients = ''
            this.form.subject = ''
            this.form.priority = null
            this.form.accesibility = null
            this.form.commenting = null
            this.form.content = null
        }
    },
    mounted() {
    },
    components: {
        Create
    }
}
</script>

<style lang="css" scoped>
.fa-btn {
    margin-top: -4px;
}

.fa-btn > .fa-bars {
    font-size: 1.275em;
}
</style>
