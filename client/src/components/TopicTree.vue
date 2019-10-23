<template>
  <div>
    <topicnewmdal :ops="options" :selected="selected"></topicnewmdal>
    <cTree :data="myData"></cTree>
  </div>
</template>



<script>
    import axios from  'axios'
    import cTree from './tree'
    import topicnewmdal from './TopicNewModal'
    export default {
        data(){
            return {
              myData:[],
              options:[],
              selected:''
            }
        },
      components:{
          cTree,
          topicnewmdal
      },
      methods:{
          getTopicTree(){
            const path = `http://localhost:5000/topictree`;
            axios.get(path)
             .then((res) => {
               this.myData = res.data;
               this.generateOptions();
               if(this.options.length > 0){
                 this.selected = this.options[0]['item'];
               }
               })
             .catch((error) => {
               // eslint-disable-next-line
               console.log(error);
               })
          },
          generateOptions(){
              for(let child of this.myData){
                for(let sub_child of child['children']){
                  let item = sub_child.id;
                  let name = sub_child.name;
                  this.options.push({item:item,name:name});
                }
              }
          }
      },
      created(){
          this.getTopicTree();
      }
    }
</script>
