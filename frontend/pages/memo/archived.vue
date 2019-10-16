<template>
    <div class="container-fluid">
        <h4>ARCHIVED ...</h4>
        <hr>
        <search-result 
            v-for="result in results" :key="result.created"
            :creator="result.creator"
            :subject="result.subject"
            :brief="result.brief"
            :created="result.created"
            :status="result.status"/>
    </div>
</template>

<script>
import SearchResult from '~/components/memo/SearchResult';

export default {
    data() {
        return {
            results: [
                {
                    creator: "Aurthur Musendame",
                    subject: "Data Analystics",
                    brief: "Lets be warry about the importance of data",
                    created: "Jan 15 2018",
                    status: "archived"
                },
                {
                    creator: "Paul Chingongo",
                    subject: "Visit to Mars 2",
                    brief: "I had a wonderful and awesome spaceship flight to mars",
                    created: "Oct 01 2019",
                    status: "archived"
                }
            ]
        }
    },
  components: {
      SearchResult
  }
}
</script>