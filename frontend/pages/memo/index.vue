<template>
    <div class="container-fluid">
        <h4>INCOMING ...</h4>
        <hr>
        <search-result 
            v-for="result in results" :key="result.created"
            :creator="result.sender.get_full_name"
            :subject="result.subject"
            :brief="result.message"
            :created="result.created"
            :id="result.id"
            status="Incoming"/>
    </div>
</template>

<script>
import SearchResult from '~/components/memo/SearchResult';

export default {
    data() {
        return {
            results: []
        }
    },
    methods: {
        truncate(str, numberOfWords) {
            return str.replace(/(<([^>]+)>)/ig,"").split(/\s+/).slice(0, numberOfWords).join(" ") + " ...";
        }
    },
    mounted () {
        this.$axios.$get('/memos/?mstate=incoming', { headers: this.$store.getters['authHeader'] })
        .then(res => {
            this.results = res
            this.results.forEach(result => { 
                result.message = this.truncate(result.message, 6)                
            });
            console.log('fetched incoming memos')
        })
        .catch(err => {
            console.log(err)
        })        
    },
    components: {
        SearchResult
    }
}
</script>