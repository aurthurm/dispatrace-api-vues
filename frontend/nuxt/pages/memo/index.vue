<template>
    <div class="container-fluid">
        <single-memorandum 
            v-for="result in results" :key="result.created"
            :creator="result.sender.get_full_name"
            :subject=truncate(result.subject)
            :brief=truncate(result.message)
            :created="result.created"
            :id="result.id"
            :status="result.memo_state"/>
    </div>
</template>

<script>
import SingleMemorandum from '~/components/memo/SingleMemorandum';

export default {
    props: {
        showMemoSubs: Boolean,
        truncate: Function,
        results: Array,
        getMemorandums: Function
    },
    mounted () {           
        this.$store.dispatch('memorandums/setMemoDetailView', false)
        this.getMemorandums(event, { memo_state: 'INCOMING' })
    },
    components: {
        SingleMemorandum
    }
}
</script>