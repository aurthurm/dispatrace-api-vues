<template>
    <div class="container-fluid mb-5">
        <h4>NEW MEMO</h4>
        <hr>
        <Create 
        :form="form"
        :onSubmit="onSubmit"
        :onReset="onReset"
        :config="config"
        >        
          <b-button type="reset" variant="danger">Reset</b-button>
        </Create>
    </div>
</template>

<script>
import Create from '~/components/memo/Create'

  export default {
    data() {
      return {
        form: {
          to: '',
          recipients: '',
          subject: '',
          priority: null,
          accesibility: null,
          commenting: null,
          content: null,
        },
        config: {
          // Get options from https://alex-d.github.io/Trumbowyg/documentation
        }
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        this.$axios.$post('/memos/', { form_data:this.form }, { headers: this.$store.getters['authHeader'] })
        .then(res => {
          console.log(res)
          this.$router.push({ path: '/memo/' + res.data.id})
        })
        .catch(err => {
          console.log(err)
        })
        // return this.$router.push({ path: '/memo/1'})
        // console.log("This form", JSON.stringify(this.form))
      },
      onReset(evt) {
        evt.preventDefault()
        this.form.to = ''
        this.form.recipients = ''
        this.form.subject = ''
        this.form.priority = null
        this.form.accesibility = null
        this.form.commenting = null
        this.form.content = null

      }
    },
    components: {
      Create
    }
  }
</script>