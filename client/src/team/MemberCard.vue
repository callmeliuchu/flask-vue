<template>
<div>
     <el-col :span="6">
         <div class="block"><el-avatar :size="50" :src="url"></el-avatar></div>
     </el-col>
     <el-col :span="8">
         <div>{{team_type}}</div>
         <div>{{team_name}}</div>
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
        }
      },
      created() {
        this.url = this.avatar_url;
        // this.type = this.team_type;
        // this.name = this.user_name;
      }
  };
</script>
