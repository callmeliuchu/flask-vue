<template>
  <div>
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="映点论坛" name="first">用户管理</el-tab-pane>
      <el-tab-pane label="团队讨论" name="second">团队讨论</el-tab-pane>
      <el-tab-pane label="个人空间" name="third">个人空间</el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
   export default {
    data() {
      return {
        activeName: 'second'
      };
    },
    methods: {
      handleClick(tab, event) {
         if(this.activeName === "second"){
              this.$router.push({
                path:'/posts',
                name:'Posts',
                params:{}
              })
         }
      }
    }
  };
</script>

<style scoped>

</style>
