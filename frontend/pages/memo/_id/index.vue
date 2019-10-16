<template>
    <article>
        <button class="btn btn-warning mb-2" @click="editMemo">EDIT</button>
        <b-card variant="bg-light" class="memo mb-5">
            <b-row>
                <b-col cols="2">FROM:</b-col>
                <b-col class="d-flex justify-content-between">
                    <span>
                        Aurthur Musedame
                    </span>
                    <span>
                        TO: Paul Chingongo
                    </span>
                    <span>
                        28 Jul 2018
                    </span>
                </b-col>
            </b-row>
            <b-row>
                <b-col cols="2">RECIPIENTS:</b-col>
                <b-col>Andriatah, Brian, Peter, Samson, ...</b-col>
            </b-row>
            <b-row>
                <b-col cols="2">SUBJECT:</b-col>
                <b-col class="font-weight-bold text-uppercase">Lorem ipsum dolor, sit amet consectetur adipisicing elit.</b-col>
            </b-row>
            <b-row>
                <b-col cols="2">REFERENCE:</b-col>
                <b-col class="font-italic font-weight-light">M-23748683HHUEHJJJ</b-col>
            </b-row>
            <b-row>
                <b-col class="bg-dark mx-0 my-2 p-1" cols="12"><h5 class="h5 ml-2 mb-0 text-white">BODY:</h5></b-col>                
                <b-col class="" cols="12">
                    <b-card-text>
                        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Architecto recusandae, quam magnam exercitationem provident velit nulla ab cum, iure debitis in nostrum veritatis molestiae qui labore consequuntur inventore sed tempore.
                        Lorem ipsum dolor sit amet consectetur adipisicing elit. Nemo nostrum aspernatur delectus. Molestiae dolor maiores non laboriosam minus. Id, qui! Aperiam voluptate pariatur laborum in, culpa minima cupiditate autem earum.
                        </p>
                        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Rerum magnam possimus at odio omnis quas similique inventore voluptatem sequi. Rerum voluptas odit sit sunt, vitae ad eveniet nesciunt explicabo quisquam.</p>
                        <p>Lorem ipsum, dolor sit amet consectetur adipisicing elit. Nobis, nostrum tempore? Odit unde amet ratione, animi placeat exercitationem repellat labore nihil, quis, in porro! Quo voluptates qui quae sapiente nemo?
                        Lorem ipsum dolor sit, amet consectetur adipisicing elit. Aut nisi, cumque dolores inventore iste iusto perferendis numquam itaque adipisci accusantium cum tenetur similique laboriosam officiis eligendi officia corporis ab incidunt?
                        Lorem, ipsum dolor sit amet consectetur adipisicing elit. Sed dolores asperiores eaque laudantium rem aut dicta ex et adipisci fugiat ratione maxime corporis corrupti esse deserunt vero dolorum, dolor quibusdam!</p>

                    </b-card-text>
                </b-col>
            </b-row>
            <b-row >
                <b-col class="bg-dark mx-0 my-2 p-1" cols="12"><h5 class="h5 ml-2 mb-0 text-white">COMMENTS:</h5></b-col>  
                <ul class="list-unstyled mt-2 mb-0">
                    <b-media tag="li" class="mb-4" v-for="comment in comments" :key="comment.index">
                        <template v-slot:aside>
                            <b-img blank blank-color="#abc" width="50" alt="placeholder" class="rounded-circle"></b-img>
                        </template>
                        <h5 class="mt-0 mb-1 font-weight-light">{{ comment.commentor }} | {{ comment.commented }}</h5>
                        <p class="mb-0">
                            {{ comment.comment }}
                        </p>
                    </b-media>
                </ul>
            </b-row>
        </b-card>
    </article>
</template>

<script>
export default {
    data() {
        return {
            comments: [
                {
                    commentor: "Aurthur Musendame",
                    comment: "Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin.",
                    commented: "May 7, 2019, 1:53 p.m."
                },
                {
                    commentor: "Bravo Stulo",
                    comment: "Cras sit amet nibh libero, in gravida nulla",
                    commented: "May 7, 2019, 1:53 p.m."
                },
                {
                    commentor: "Cardinal Ndowu",
                    comment: "Nulla vel metus scelerisque ante sollicitudin, in gravida nulla.",
                    commented: "May 7, 2019, 1:53 p.m."
                }
            ]
        }
    },
    methods: {
        editMemo() {
            return this.$router.push({ path: '/memo/1/edit'})
        }
    },
}
</script>