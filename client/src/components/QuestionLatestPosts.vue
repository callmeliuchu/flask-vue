<template>


  <div class="container">
      <div>
        <div class="row">
            <div class="col-xs-12 text-center">
                <p>{{ question.title }}</p>
            </div>
        </div>
        <div class="row">
            <div class="col-xs-12 text-center">
                <p>{{ question.description }}</p>
            </div>
        </div>


        <b-dropdown text="管理" variant="secondary">
          <b-dropdown-item @click="delete_question(question)">删除</b-dropdown-item>
        </b-dropdown>
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
  import navhead from './Head'

  export default {
     data(){
       return {
         id:'',
         question:{},
         posts:[]
       }
     },
    methods:{
       getPostsByQuestion(){
         const path = `http://localhost:5000/question/${this.id}`;
         axios.get(path)
           .then((res) => {
             this.question = res.data.question;
             this.posts = res.data.posts;
             })
           .catch((error) => {
             // eslint-disable-next-line
             console.log(error);
             })
       },
       getDetail(post){
         this.$router.push({name:'PostsStruct',params:{id:post.belong_to_post_id}})
       },
       delete_question(question){
           const path = `http://localhost:5000/question/${question.id}/delete`;
           axios.get(path)
             .then((res) => {
                 this.$router.push({name:'TopicTree'});
               })
             .catch((error) => {
               // eslint-disable-next-line
               console.log(error);
             })
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
      this.getPostsByQuestion();
    }

  }

</script>


<style>


</style>
