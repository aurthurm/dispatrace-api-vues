<template>
    <nuxt-link :to="'/memo/' + id + ''" tag="a">     
        <div class="result row">
            <div class="col-2 font-weight-bold">
                {{ creator }}
            </div>
            <div class="col-10 d-flex justify-content-between">
                <span>
                    <span class="subject font-weight-bold">{{ subject }}</span> - 
                    <span class="brief text-muted">{{ brief }}</span>
                </span>
                <span class="justify-content-between">   
                    <b-badge variant="info" class="mr-1">{{ status }}</b-badge>
                    <span class="date">{{ created | date  }}</span>                     
                </span>
            </div>                    
        </div>                
        <hr class="mt-1">
    </nuxt-link>
</template>

<script>
export default {
    props: {
        creator: String,
        subject: String,
        brief: String,
        created: String,
        status: String,
        id: Number,
    }
}
</script>