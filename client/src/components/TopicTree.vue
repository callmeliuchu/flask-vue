<template>
  <div>
      <navhead></navhead>
      <div class="table-container">
       <!--topicnewmdal :ops="options" :selected="selected"></topicnewmdal-->
       <div class="table-left">
         <cTree :data="team_organization"  :custom_method="get_topic_tree_by_team"></cTree>
       </div>
       <div class="table-right">
         <cTree :data="topic_tree" :custom_method="test_f" ></cTree>
       </div>
      </div>
  </div>
</template>



<script>
    import axios from  'axios'
    import cTree from './tree'
    import topicnewmdal from './TopicNewModal'
    import topoJson from '../data/topoData1.js'
    import navhead from './Head'
    //
    export default {
        data(){
            return {
              topic_tree:[],
              options:[],
              selected:'',
              topoJson:topoJson,
              team_organization:[]
            }
        },
      components:{
          navhead,
          cTree,
          topicnewmdal,
      },
      methods:{
          getTopicTree(){
            const path = `http://localhost:5000/main_page`;
            axios.get(path)
             .then((res) => {
               // this.topic_tree = res.data.topic_tree;
               this.team_organization = res.data.team_organization;
               this.topic_tree = [];
               // this.generateOptions();
               // if(this.options.length > 0){
               //   this.selected = this.options[0]['item'];
               // }
               })
             .catch((error) => {
               // eslint-disable-next-line
               console.log(error);
               })
          },
          // generateOptions(){
          //     for(let child of this.myData){
          //       for(let sub_child of child['children']){
          //         let item = sub_child.id;
          //         let name = sub_child.name;
          //         let parent = child.id;
          //         this.options.push({item:item,name:name,forum_id:parent});
          //       }
          //     }
          // },
          test_f(data){
              this.$router.push({name:'TopicLatestPosts',params:{id:data.id}})
          },
          get_topic_tree_by_team(data){
              let team_id = data.id;
              const path = `http://localhost:5000/team/${team_id}/topic_tree`;
              axios.get(path)
             .then((res) => {
               this.topic_tree = res.data;
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


<style>
.table-container{
    width: 100%;
    padding: 5px;
    border: 1px solid #eee;
    display: table;
}
.table-left{
    width: 200px;
    /*background-color: mediumspringgreen;*/
}

.table-right{
    /*background-color: skyblue;*/
}

.table-left, .table-right{
    height: 100px;
    display: table-cell;
}
</style>
