<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>posts</h1>
        <hr><br><br>
        <br><br>
        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col" v-for="(column,index) in columns" :key="index">{{ column }}</th>
          </tr>
          </thead>
          <tbody>
          <tr v-for="post in posts">
            <td v-for="column in columns">
              {{ post[column] }}
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>


<script>
  import axios from 'axios';

  export default {
    data(){
     return {
       columns:[],
       posts:[],
     }
   },

    methods:{
      getPosts() {
        const path = 'http://localhost:5000/posts';
        axios.get(path)
          .then((res) => {
            this.columns = res.data.columns;
            this.posts = res.data.posts;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error);
          })
      }
    },

    created(){
      this.getPosts()
    }


  }
</script>
