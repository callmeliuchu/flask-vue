<template>
  <el-container>
    <el-header></el-header>
      <el-main>
        <el-row :gutter="10" v-for="i in [1,2,3,5,3,45,6,3,22,32,2,3,22,2,2,33,32,22,3]" :justify="center">
          <el-col :span="5" v-for="j in [1,2,4,5]" :push="3">
           <member></member>
         </el-col>
        </el-row>
      </el-main>
    </el-container>
</template>
<script>
  import member from './MemberCard'
  export default {
    data () {
      return {
        circleUrl: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
        squareUrl: "https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png",
        sizeList: ["large", "medium", "small"]
      }
    },
      components:{
        member
      }
  }
</script>
<style>
  .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }

  .el-main {
    text-align: center;
  }

</style>
