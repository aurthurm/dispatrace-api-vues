<template>
    <b-container fluid>
       <!-- Notices Categories -->
       <b-row>
           <b-col md="4">
               <b-card bg-variant="light">
                    <template v-slot:header>
                        <span class="d-flex justify-content-between">
                            <h5>Students</h5>
                            <span>
                                <font-awesome-icon icon="edit" /> | <font-awesome-icon icon="times" />
                            </span>
                        </span>
                    </template>
                    <b-card-text class="d-flex justify-content-between">
                       <span>Lorem ipsum dolor.</span>
                       <span><font-awesome-icon icon="edit" /> | <font-awesome-icon icon="eye" /> | <font-awesome-icon icon="times" /></span>
                    </b-card-text>
                    <b-card-text class="d-flex justify-content-between">
                       <span>Lorem ipsum dolor.</span>
                       <span><font-awesome-icon icon="edit" /> | <font-awesome-icon icon="eye" /> | <font-awesome-icon icon="times" /></span>
                    </b-card-text>
                    <template v-slot:footer>
                        <span> + Add Notice</span>
                    </template>
               </b-card>
           </b-col>
       </b-row>
       <hr>
       <!-- Notices Expires -->
       <b-row>
           <b-col md="12">
               <b-card bg-variant="warning" header="Expired Notices">
                   <b-card-text>
                    
                   </b-card-text>
               </b-card>
           </b-col>
       </b-row>
    </b-container>
</template>