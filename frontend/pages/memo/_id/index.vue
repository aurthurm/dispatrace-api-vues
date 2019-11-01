<template>
    <article>
        <button class="btn btn-warning mb-2" @click="editMemo">EDIT</button>
        <b-card variant="bg-light" class="memo mb-5">
            <b-row>
                <b-col cols="2">FROM:</b-col>
                <b-col class="d-flex justify-content-between">
                    <span>
                        {{memo.sender.get_full_name || memo.sender.username}}
                    </span>
                    <span>
                        TO: {{memo.to.get_full_name || memo.to.username}}
                    </span>
                    <span>
                        {{memo.date_sent}}
                    </span>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="2">RECIPIENTS:</b-col>
                <b-col>
                    <span class="mr-2" v-for="recipient in memo.recipients" :key="recipient.id">@{{recipient.username}} </span>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="2">SUBJECT:</b-col>
                <b-col class="font-weight-bold text-uppercase">{{memo.subject}}</b-col>
            </b-row>
            <b-row>
                <b-col cols="2">REFERENCE:</b-col>
                <b-col class="font-italic font-weight-light">{{memo.reference_number}}</b-col>
            </b-row>
            <b-row>
                <b-col class="bg-dark mx-0 my-2 p-1" cols="12"><h5 class="h5 ml-2 mb-0 text-white">BODY:</h5></b-col>                
                <b-col class="" cols="12">
                    <b-card-text v-html="memo.message">
                    </b-card-text>
                </b-col>
            </b-row>
            <b-row >
                <b-col class="bg-dark mx-0 my-2 p-1" cols="12">
                    <h5 class="h5 ml-2 mb-0 text-white">
                        COMMENTS: {{memo.comment_count}} 
                        <b-button id="show-btn" @click="showModal" class="float-right btn-sm" data-comment='new'>New Comment</b-button> 
                    </h5>
                </b-col>  
                <ul class="list-unstyled mt-2 mb-0">
                    <b-media tag="li" class="mb-4" v-for="comment in memo.memocomment_comment" :key="comment.id">
                        <template v-slot:aside>
                            <b-img blank blank-color="#abc" width="50" alt="placeholder" class="rounded-circle"></b-img>
                        </template>
                        <h5 class="h6 mt-0 mb-1 font-weight-light">{{ comment.commenter.get_full_name }} | {{ comment.timestamp | date }} <span class="ml-5 text-small" data-comment='old' :data-comment-id="comment.id" :data-comment-text="comment.comment"  @click="showModal">Edit</span> </h5>
                        <p class="mb-0">
                            {{ comment.comment }}
                        </p>
                    </b-media>
                </ul>
            </b-row>
        </b-card>
        <b-modal 
        ref="modal" 
        title="Comment"
        size="lg"
        @ok="handleOk"
        centered
        >
            <b-form ref="form" @submit.stop.prevent="handleSubmit">
                <b-row>
                    <b-col>
                        <b-form-group
                        id="fieldset-horizontal"
                        :state="nameState"
                        label-cols-sm="3"
                        label-cols-lg="2"
                        label-size="sm"
                        description="Comment"
                        label="Comment"
                        label-for="comment"
                        invalid-feedback="comment is required"
                        >
                            <b-form-textarea 
                            id="comment"
                            v-model="form.comment"
                            :state="nameState"
                            required
                            ></b-form-textarea>
                        </b-form-group>
                    </b-col>                
                </b-row>
                <slot></slot>
            </b-form>
        </b-modal>
    </article>
</template>

<script>
export default {
    props: {
        memo: Object
    },
    data() {
        return {
            form: {
                comment: null,
                new: null,
                id: null
            },
            nameState: null
        }
    },
    methods: {
        editMemo() {
            return this.$router.push({ path: '/memo/' + this.$route.params.id + '/edit' })
        },
        checkFormValidity(){
            const valid = this.$refs.form.checkValidity()
            this.nameState = valid ? 'valid' : 'invalid'
            return valid
        },
        showModal(event) {
            this.$refs['modal'].show()
            let dataComment = event.target.attributes['data-comment'].value
            this.form.new = dataComment
            if(dataComment === "old")
            {                
                this.form.id = event.target.attributes['data-comment-id'].value
                this.form.comment = event.target.attributes['data-comment-text'].value
            }
            else {                
                this.form.id = null
                this.form.comment = null
            }
        },
        handleOk(bvModalEvt){
            bvModalEvt.preventDefault();
            this.handleSubmit()            
        },
        handleSubmit(){
            let axiosMethod = this.form.new === "new" ? this.$axios.$post : this.$axios.$put
            axiosMethod('memos/comments/', {
                new: this.form.new,
                comment: this.form.comment,
                memo_id: this.$route.params.id,
                comment_id: this.form.id
            })
            .then(res => {
                this.$nextTick(() => {
                    this.$refs.modal.hide()
                })
                // window.location.reload()
                this.$router.push({ path: '/memo/' + this.$route.params.id + '/' })
            })
            .catch(err => {
                console.log(err)
            })
        }
    }
}
</script>