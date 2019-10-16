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
          recipients: '',
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
        return this.$router.push({ path: '/memo/1'})
      }
    },
    created () {
          this.form = {
            to: 'Aurthur Musendame',
            recipients: 'Antony, Paul, Desmond, Samantha',
            subject: 'Crazy memorandum expo',
            priority: 'Very Urgent',
            accesibility: 'Private',
            commenting: 'Required',
            content: 'loren ipsum dolor asimet colmoder, asit, el emodegly'
        }
    },
    components: {
      Create
    }
  }
</script>