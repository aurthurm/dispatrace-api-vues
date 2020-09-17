<template>        
    <b-card bg-variant="light" class="mb-5">
        <b-form  @submit.stop.prevent="onSubmit" @reset="onReset">
            <b-row>
                <b-col>
                    <b-form-group
                    id="fieldset-horizontal"
                    label-cols-sm="3"
                    label-cols-lg="2"
                    label-size="sm"
                    description="Final Memo Recipient"
                    label="TO:"
                    label-for="memo-to"
                    >
                    <b-form-input 
                    id="memo-to"
                    v-model="form.to"
                    ></b-form-input>
                    </b-form-group>
                </b-col>
                <b-col>
                    <b-form-group
                    label-cols-sm="3"
                    label="Priority:"
                    label-align-sm="right" class="mb-0"
                    >
                        <b-form-radio-group
                        class="pt-2"
                        :options="['Normal', 'Moderate', 'Very Urgent']"                    
                        v-model="form.priority"
                        ></b-form-radio-group>
                    </b-form-group>
                </b-col>
            </b-row>

            <b-row>
                <b-col>
                    <b-form-group
                    id="fieldset-horizontal"
                    label-cols-sm="3"
                    label-cols-lg="2"
                    label-size="sm"
                    description="CC:"
                    label="RECIPIENTS:"
                    label-for="memo-recipients"
                    >
                    <b-form-input 
                    id="memo-recipients"
                    v-model="form.recipients"></b-form-input>
                    </b-form-group>
                </b-col>
                <b-col>
                    <b-form-group
                    label-cols-sm="3"
                    label="Accessibility:"
                    label-align-sm="right" class="mb-0"
                    >
                        <b-form-radio-group
                        class="pt-2"
                        :options="['Public', 'Private']"
                        v-model="form.accesibility"
                        ></b-form-radio-group>
                    </b-form-group>
                </b-col>
            </b-row>

            <b-row>
                <b-col>
                    <b-form-group
                    id="fieldset-horizontal"
                    label-cols-sm="3"
                    label-cols-lg="2"
                    label-size="sm"
                    label="SUBJECT:"
                    label-for="memo-subject"
                    >
                    <b-form-input 
                    id="memo-subject"
                    v-model="form.subject"></b-form-input>
                    </b-form-group>
                </b-col>
                <b-col>
                    <b-form-group
                    label-cols-sm="3"
                    label="Commenting:"
                    label-align-sm="right" class="mb-0"
                    >
                        <b-form-radio-group
                        class="pt-2"
                        :options="['Required', 'Not Required']"
                        v-model="form.commenting"
                        ></b-form-radio-group>
                    </b-form-group>
                </b-col>
            </b-row>  
            
            <b-row class="mb-2">
                <b-col sm="12">
                    <label for="textarea-memo">Memo Body:</label>
                    <trumbowyg v-model="form.content" :config="config" class="form-control" name="content"></trumbowyg>
                </b-col>
            </b-row>

            <!-- <b-card class="my-3" header="Form Data Result">
                <pre class="m-0">{{ form }}</pre>
            </b-card> -->

            <b-button type="submit" variant="primary">Submit</b-button>
            <slot></slot>
        </b-form>
    </b-card>
</template>

<script>
export default {
    props: {
        form: Object,
        onSubmit: Function,
        onReset: {
            type: Function,
            default: function(){}
        },
        config: Object,
    }
}
</script>
