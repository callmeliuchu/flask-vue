<template>
  <div class="">
      <nav aria-label="breadcrumb">
              <ol class="breadcrumb">
                  <li class="breadcrumb-item"><a href="#">新建文章</a></li>
              </ol>
      </nav>
      <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
          <li class="breadcrumb-item"><a href="#">话题</a></li>
          <li class="breadcrumb-item"><a href="#">{{category_name}}</a></li>
          <li class="breadcrumb-item active" aria-current="page">新建问题</li>
        </ol>
      </nav>


        <div class="form-group">
          <input  class="form-control" placeholder="标题" v-model="title">
        </div>
        <div class="form-group">
          <textarea class="form-control"  rows="3" placeholder="内容" v-model="content"></textarea>
        </div>
         <button  class="btn btn-primary" @click="onSubmit()">提交</button>
  </div>
</template>


<script>

    import Card from "bootstrap-vue/esm/mixins/card";
    import axios from 'axios';

    export default {
      components: {Card},
      data() {
            return {
                title: '',
                content: '',
                category_name:'',
                forum_id : -1,
            }

        },
        methods:{
          onSubmit(){
              const path = 'http://localhost:5000/topic/new';
              let dict_data = {
                title:this.title,
                content:this.content,
                forum_id:this.forum_id,
              }
              axios.post(path,dict_data)
                .then((res) => {
                    // alert('success');
                    this.$router.push({name:'TopicTree'})
                })
                .catch((error) => {
                })
          },
          onReset(){

          }

        },
      created(){
        // alert(this.$route.params.topic_data.id);
        // alert(this.$route.params.topic_data.name);
        this.category_name = this.$route.params.topic_data.name;
        this.forum_id = this.$route.params.topic_data.forum_id;
      }

    }

</script>





