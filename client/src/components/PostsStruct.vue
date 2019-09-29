<template>
  <b-container>
    <b-card v-for="post_struct in posts_struct">
      <b-row>
        <b-col>
            <post :post_data="post" v-for="post in post_struct.post_2" ></post>
            <post :post_data="post" v-for="post in post_struct.post_3" ></post>
        </b-col>

        <b-col>
            <post :post_data="post" v-for="post in post_struct.post_main"></post>
        </b-col>
        <b-col>

            <post :post_data="post" v-for="post in post_struct.post_4" ></post>
            <post :post_data="post" v-for="post in post_struct.post_5" ></post>

        </b-col>
      </b-row>
    </b-card>
  </b-container>
</template>


<script>
  import axios from 'axios'
  import Post from './Post'

  export default {
    data(){
      return {
        posts_struct: {},
      }
    },
    components:{post:Post},
    methods:{
      getPostsStruct(post_id){
        const path = `http://localhost:5000/poststruct/${post_id}`;
        axios.get(path).then((res) => {
          this.posts_struct = res.data.posts_struct;
          console.log(JSON.stringify(this.posts_struct));
          // alert(JSON.stringify(this.post_main));
        }).catch((error) => {

        })
      }
    },
    created(){
     this.getPostsStruct(this.$route.params.id)
    }
  }

</script>


<style>

</style>
