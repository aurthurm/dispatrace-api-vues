<template>
    <div>
        <nuxt-child />
    </div>
</template>

<script>
// import { mapGetters } from 'vuex';

export default {
    mounted() {
        this.$store.dispatch('memorandums/setMemoDetailView', true);
    }
}
</script>