<template>
   <cTree :data="myData"></cTree>
</template>



<script>
    import axios from  'axios'
    import cTree from './tree'
    export default {
        data(){
            return {
              myData:[],
            }
        },
      components:{
          cTree
      },
      methods:{
          getTopicTree(){
            const path = `http://localhost:5000/topictree`;
            axios.get(path)
             .then((res) => {
               this.myData = res.data;
               })
             .catch((error) => {
               // eslint-disable-next-line
               console.log(error);
               })
          }
      },
      created(){
          this.getTopicTree();
      }
    }
</script>
