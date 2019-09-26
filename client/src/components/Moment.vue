<template>
  <div class="container">
    <div class="row">
      <div>
        <h1>moment</h1>
        <hr><br><br>
        <br><br>
        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col" v-for="column in columns">{{ column }}</th>
          </tr>
          </thead>
          <tbody>
          <tr  v-for="moment in moments">
            <td v-for="column in columns">{{ moment[column] }}</td>
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
        moments:[],
      }
    },

    methods:{
      getMoments() {
        const path = 'http://localhost:5000/moments';
        axios.get(path)
          .then((res) => {
            this.columns = res.data.columns;
            this.moments = res.data.moments;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error);
          })
      }
    },


    created(){
      this.getMoments()
    }



  }



</script>

