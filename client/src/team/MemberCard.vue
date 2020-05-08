<template>
<div>
     <el-col :span="8">
         <div class="block" v-on:click="handleAvatar()"><el-avatar :size="70" :src="url"></el-avatar></div>
     </el-col>
     <el-col :span="15">
       <div v-if="!is_edit">
           <div>{{type}}</div>
           <div>
                <span>{{name}}</span>
                <span v-on:click="makeEdit()"><i class="el-icon-edit"></i></span>
           </div>
       </div>
       <div v-if="is_edit">
           <el-row><el-input v-model="name"></el-input></el-row>
           <el-row>
             <el-col :span="10"><el-button round v-on:click="handleSave()">保存</el-button></el-col>
             <el-col :span="10"><el-button round v-on:click="handleOut()">退出</el-button></el-col>
           </el-row>
       </div>
     </el-col>
</div>
</template>


<script>
  export default {
    props: ['avatar_url','team_name','team_type'],
      data(){
        return {
            'url':'',
            'type':'',
            'name':'',
            'is_edit':false
        }
      },
      created() {
        this.url = this.avatar_url;
        this.name = this.team_name;
        this.type = this.team_type;
      },
      methods:{
        handleAvatar(){
            if(this.is_edit){
                alert(11111)
            }
        },
          makeEdit(){
            this.is_edit = true;
          },
          handleSave(){
            this.is_edit = false;
          },
          handleOut(){
            this.is_edit = false;
          }
      }
  };
</script>
