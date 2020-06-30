<template>
    <div class="container-fluid mb-5">
        <h4>EDIT MEMO</h4>
        <hr>
        <Create 
        :form="form"
        :onSubmit="onSubmit"
        :config="config"
        ></Create>
    </div>
</template>

<script>
import Create from '~/components/memo/Create'

  export default {
    data() {
      return {
        form: {
          to: '',
          recipients: [],
          subject: '',
          priority: null,
          accesibility: null,
          commenting: null,
          content: null
        },
        config: {
          // Get options from https://alex-d.github.io/Trumbowyg/documentation
        }
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        // console.log("This form", JSON.stringify(this.form))
        this.$axios.$put('/memos/' + this.$route.params.id + '/', { memo_form: this.form }, { headers: this.$store.getters['authHeader'] })
        .then(res => {
          this.$router.push({ path: '/memo/' + res.data.id})
        })
        .catch(err => {
          console.log(err)
        })
        // return this.$router.push({ path: '/memo/1'})
      }
    },
    mounted () {
        // this.$store.dispatch('memorandums/setMemoDetailView', true);
        this.$axios.$get('/memos/' + this.$route.params.id + '/', { headers: this.$store.getters['authHeader'] })
        .then(res => {
            this.memo = res.data
            this.extras = res.extras    

            let recipients = []
            this.memo.recipients.forEach(recipient => {
              recipients.push(recipient.username)
            });
            let shouldComment =  this.memo.commenting_required ? "Required" : "Not Required"
            let accesibility =  this.memo.accesibility === "PVT" ? "Private" : "Public"
            this.form = {
              to: this.memo.to.username,
              recipients: recipients.join(),
              subject: this.memo.subject,
              priority: this.memo.mem_priority,
              accesibility: accesibility,
              commenting: shouldComment,
              content: this.memo.message
            }
        })
        .catch(err => {
            console.log(err)
        })  
    },
    components: {
      Create
    }
  }
</script>