<template>


  <div class="container">
      <div>
        <div class="row">
            <div class="col-xs-12 text-center">
                <p>{{ topic.title }}</p>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-12 text-center">
                <p>{{ topic.description }}</p>
            </div>
        </div>
      </div>
      <hr/>
      <div v-for="(post,index) in posts" :key="index">
        <div class="row">
          <div class="col-xs-12"><p @click="getDetail(post)">{{ post.title }}</p></div>
        </div>
        <div class="row">
          <div class="col-xs-12"><p @click="getDetail(post)">{{ post.content }}</p></div>
        </div>
        <div class="row">
          <div class="col-xs-12"><p>{{ post.date_created }}</p></div>
        </div>
        <hr/>
      </div>
  </div>
</template>



<script>
  import axios from 'axios';

  export default {
     data(){
       return {
         id:'',
         topic:{},
         posts:[]
       }
     },
    methods:{
       getPostsByTopic(){
         const path = `http://localhost:5000/topic/${this.id}`;
         axios.get(path)
           .then((res) => {
             this.topic = res.data.topic;
             this.posts = res.data.posts;
             })
           .catch((error) => {
             // eslint-disable-next-line
             console.log(error);
             })
       },
       getDetail(post){
         this.$router.push({name:'PostsStruct',params:{id:post.belong_to_post_id}})
       }
    },
    // methods: {
    //   getParams () {
    //     this.id = this.$router.params.id;
    //     alert(this.id)
    //   }
    // },
    // watch: {
    //   '$router': 'getParams'
    // },
    created(){
       // id = this.$router.params.id;
      // alert();
      this.id = this.$route.params.id;
      this.getPostsByTopic();
    }

  }

</script>


<style>


</style>
