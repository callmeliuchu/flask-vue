<template>
  <div class="expand">
    <el-button @click="handleSubmit">提交</el-button>
    <tree :api_data="team_organization"></tree>
  </div>
</template>



<script>
  import tree from  '../view/tree'
  import axios from 'axios'

  export default {
      data() {
          return {
              test_data: {'maxexpandId':0,'treelist':[]},
              team_organization:{'maxexpandId':0,'treelist':[]},
          }
      },
      components:{
          tree
      },
      methods:{
          handleSubmit(){
           // alert(JSON.stringify(this.test_data));
           console.log(JSON.stringify(this.team_organization));
           // this.getTeamOrganization();
          },
          getTeamOrganization(){
            const path = `http://localhost:5000/team/organization`;
            axios.get(path)
             .then((res) => {
               this.team_organization = res.data;
               })
             .catch((error) => {
               console.log(error);
               })
          }

      },

      created(){
          this.getTeamOrganization();
      }
  }
</script>


<style>
.expand{
  width:100%;
  height:80%;
  overflow:hidden;
}
.expand>div{
  height:85%;
  padding-top:20px;
  width:50%;
  /*margin:20px auto;*/
  max-width:400px;
  overflow-y:auto;
}
.expand>div::-webkit-scrollbar-track{
  box-shadow: inset 0 0 6px rgba(0,0,0,.3);
  border-radius:5px;
}
.expand>div::-webkit-scrollbar-thumb{
  background-color:rgba(50, 65, 87, 0.5);
  outline:1px solid slategrey;
  border-radius:5px;
}
.expand>div::-webkit-scrollbar{
  width:10px;
}
.expand-tree{
  border:none;
  margin-top:10px;
}
.expand-tree .el-tree-node.is-current,
.expand-tree .el-tree-node:hover{
  overflow:hidden;
}
.expand-tree .is-current>.el-tree-node__content .tree-btn,
.expand-tree .el-tree-node__content:hover .tree-btn{
  display:inline-block;
}
.expand-tree .is-current>.el-tree-node__content .tree-label{
  font-weight:600;
  white-space:normal;
}
</style>
