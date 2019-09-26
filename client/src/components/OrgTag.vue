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
            <th scope="col" v-for="[tag,value] in tags">
              <p @click="queryTag(tag)">{{tag}}</p><br>
              <p>{{value}}</p>
            </th>
          </tr>
          </thead>
          <MomentRow :moments="moments"  :columns="columns"></MomentRow>
        </table>
      </div>
    </div>
  </div>
</template>


<script>
  import axios from 'axios';
  import MomentRow from './MomentRow';

  export default {
    components: {MomentRow},
    data(){
     return {
       tags: [['你好',100],['哈哈',99]],
       org_id:'2cc47f92-f419-40a5-a387-c6d1e56e10d1',
       moments:[],
       columns:[]
     }
   },
    methods:{
     getOrgTag(){
      const path = `http://localhost:5000/orgtag/${this.org_id}`;
      axios.get(path).then((res)=>{
        this.tags = res.data.tags;
      }).catch((error)=>{
        console.log(error);
      })
     },
      queryTag(tag){
       const path = `http://localhost:5000/orgtag/${this.org_id}/${tag}`;
      axios.get(path).then((res)=>{
        this.moments = res.data.moments;
        this.columns = res.data.columns;
      }).catch((error)=>{
        console.log(error);
      })
      }
    },
    created(){
     this.getOrgTag()
    }

  }
</script>
