<template>
    <div class="container-fluid">
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
            <nuxt-link v-for="mstate in memoStates" :to="'/memo' + mstate.link" class="nav-item" tag="a" :key="mstate.title">
                <b-button :variant="mstate.color" >
                    {{ mstate.title }}
                    <b-badge variant="light">{{ mstate.count }}</b-badge>
                </b-button>    
            </nuxt-link>   
            <nuxt-link to="/memo/new" class="nav-item" tag="a">
                <b-button variant="outline-success">+ NEW</b-button>    
            </nuxt-link>       
        </section>
        <hr>
        <section id="dynamic-wrapper" v-if="!searched">
            <nuxt-child :truncate="truncate"/>
        </section> 
        <section id="search-results" v-else>
            <h4>Search Results ...</h4>
            <hr>
            <search-result 
                v-for="result in results" :key="result.created"
                :creator="result.sender.get_full_name"
                :subject="result.subject"
                :brief="result.message"
                :created="result.created"
                :id="result.id"
                status="Incoming"/>
        </section> 
    </div>
</template>

<script>
import SearchResult from '~/components/memo/SearchResult';

export default {
    data() {
        return {
            searched: false,
            results: [],
            searchQuery: '',
            showMemoSubs: false,
            memoStates: [
                {
                    title: "INCOMING",
                    color: "info",
                    link: "",
                    count: 2
                },
                {
                    title: "OUTGOING",
                    color: "success",
                    link: "/outgoing",
                    count: 5
                },
                {
                    title: "DRAFTS",
                    color: "light",
                    link: "/drafts",
                    count: 5
                },
                {
                    title: "CLOSED",
                    color: "warning",
                    link: "/closed",
                    count: 5
                },
                {
                    title: "ARCHIVED",
                    color: "dark",                    
                    link: "/archived",
                    count: 65
                },
            ]          
        }
    },
    methods: {
        truncate(str, numberOfWords) {
            return str.replace(/(<([^>]+)>)/ig,"").split(/\s+/).slice(0, numberOfWords).join(" ") + " ...";
        },
        memoSearch: function() {
            this.searched = true;
            console.log("Query", this.searchQuery)
            this.$axios.$get('/memos/?q=' + this.searchQuery, { headers: this.$store.getters['authHeader'] })
            .then(res => {
                this.results = res
                this.results.forEach(result => { 
                    result.message = this.truncate(result.message, 6)                
                });
                console.log('searched memos', res)
            })
            .catch(err => {
                console.log(err)
            })    
        },
        toggleMemoSubs: function() {
            this.showMemoSubs = !this.showMemoSubs
        }
    },
    watch: {
        $route () {
            // when route changes: toggle searched
            this.searched = false
        }
  },
  components: {
      SearchResult
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
