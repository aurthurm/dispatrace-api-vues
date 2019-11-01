<template>
  <div class="container-fluid">
    <h3>DASHBOARD</h3>
    <hr>
    <div class="row">
      <div class="col-6">
        NOTICES
        <hr>        
      <div role="tablist">
          <b-card no-body class="mb-1" v-for="notice in notices" :key="notice.id">
            <b-card-header header-tag="header" class="p-1" role="tab">
              <b-button class="text-left" block href="#" v-b-toggle="'accordion-' + notice.id" variant="info">{{ notice.title }}</b-button>
            </b-card-header>
            <b-collapse :id="'accordion-' + notice.id" accordion="my-accordion" role="tabpanel">
              <b-card-body>
                <b-card-text>{{ notice.description }}</b-card-text>
              </b-card-body>
            </b-collapse>
          </b-card>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
  data() {
    return {
     
    }
  },
  computed: {
    ...mapGetters({
      notices: 'notices/getNotices'
    })
  },
  mounted() {
    this.$store.dispatch('notices/setNotices', this.$store.getters['authHeader'] )
  },
  components: {
  }
}
</script>

<style>

</style>
