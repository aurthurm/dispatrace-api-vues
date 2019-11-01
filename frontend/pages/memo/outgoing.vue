<template>
    <div class="container-fluid">
        <h4>OUTGOING ...</h4>
        <hr>
        <search-result 
            v-for="result in results" :key="result.created"
            :creator="result.sender.get_full_name"
            :subject="result.subject"
            :brief="result.message"
            :created="result.created"
            :id="result.id"
            status="Outgoing"/>
    </div>
</template>

<script>
import SearchResult from '~/components/memo/SearchResult';

export default {
    props: {
        truncate: Function,
    },
    data() {
        return {
            results: []
        }
    },
    mounted () {
        this.$axios.$get('/memos/?mstate=outgoing', { headers: this.$store.getters['authHeader'] })
        .then(res => {
            this.results = res
            this.results.forEach(result => { 
                result.message = this.truncate(result.message, 6)                
            });
            console.log('fetched outgoing memos', res)
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