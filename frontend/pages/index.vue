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
                <b-card-text>{{ notice.text }}</b-card-text>
              </b-card-body>
            </b-collapse>
          </b-card>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      notices: [
        {
            title: "Staff Meeting Tomorrow",
            text: "May you all please try to attend. You will get a negative score for non attendancee",
            author: "Raaj Pranav 1",
            expiry: "Today 4:40",
            id: "001"
        },{
            title: "Staff Meeting Tomorrow",
            text: "May you all please try to attend. You will get a negative score for non attendancee",
            author: "Mlotshwa 2",
            expiry: "Today 4:40",
            id: "002"
        },{
            title: "Staff Meeting Tomorrow",
            text: "May you all please try to attend. You will get a negative score for non attendancee",
            author: "Snadisiwe 3",
            expiry: "Today 4:40",
            id: "003"
        },{
            title: "Visitors for Accreditation arriving tomorro",
            text: "dont find yourself late",
            author: "Aurthur M",
            expiry: "Today 4:40",
            id: "004"
        }
      ]
    }
  },
  components: {
  }
}
</script>

<style>

</style>
