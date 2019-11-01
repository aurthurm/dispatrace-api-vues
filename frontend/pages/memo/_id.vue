<template>
    <div>
        <nuxt-child  :memo="memo"/>
    </div>
</template>

<script>
export default {
    data(){
        return {            
            memo: {
                archived: null,
                commenting_required: null,
                created: null,
                date_sent: null,
                id: null,
                is_open: null,
                mem_priority: null,
                memo_type: null,
                message: null,
                receptors: [],
                recipients: [],
                reference_number: null,
                sender: {},
                sent: null,
                slug: null,
                subject: null,
                to: {},
            },
        }
    },
    mounted () {
        this.$axios.$get('/memos/' + this.$route.params.id + '/', { headers: this.$store.getters['authHeader'] })
        .then(res => {
            this.memo = res
            console.log('fetched single memo', this.memo)
        })
        .catch(err => {
            console.log(err)
        })        
    },
}
</script>