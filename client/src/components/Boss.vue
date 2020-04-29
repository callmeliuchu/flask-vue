<template>

  <el-container>
    <el-header>
        <navhead></navhead>
    </el-header>
    <el-container>
        <el-aside width="200px">
          <el-button @click="handleSubmit">提交</el-button>
          <tree :api_data.sync="team_organization"></tree>
        </el-aside>
       <el-container>
            <el-main>Main</el-main>
           <el-footer>Footer</el-footer>
        </el-container>
    </el-container>
  </el-container>
</template>



<script>
  import tree from  '../view/tree'
  import axios from 'axios'
  import navhead from './Head'

  export default {
      data() {
          return {
              test_data: {'maxexpandId':0,'treelist':[]},
              team_organization:{'maxexpandId':0,'treelist':[]},
          }
      },
      components:{
          tree,
          navhead
      },

      methods:{
          handleSubmit(){
            const path = `http://localhost:5000/team/new`;
              axios.post(path,this.team_organization)
                .then((res) => {
                    alert('success');
                    // this.$router.push({name:'TopicTree'})
                })
                .catch((error) => {
                })


           // this.getTeamOrganization();
          },
          getTeamOrganization(){
            const path = `http://localhost:5000/team/organization`;
            // let data1 = null;
            // alert(1);
            axios.get(path)
             .then((res) => {
                 // alert(JSON.stringify(res.data));
                 this.team_organization = res.data;
                 // alert(2);
                 // alert(data1);
                 // this.$set(this.team_organization,'maxexpandId',res.data['maxexpandId'])
                 // this.$set(this.team_organization,'treelist',res.data['treelist'])
              // this.team_organization.maxexpandId=res.data['maxexpandId'];
              // this.team_organization.treelist=res.data['treelist'];
               })
             .catch((error) => {
                 alert(error);
               console.log(error);
               })
              // alert(3);
          }


      },
      //
      // mounted(){
      //     this.getTeamOrganization();
      // },

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
