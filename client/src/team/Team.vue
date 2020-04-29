<template>
  <div>
      <el-row :gutter="10">
    <el-col :span="5">
      <member></member>
    </el-col>
    <el-col :span="5">
      <member></member>
    </el-col>
    <el-col :span="5">
      <member></member>
    </el-col>
  </el-row>
        <el-row :gutter="10">
    <el-col :span="5">
      <member></member>
    </el-col>
    <el-col :span="5">
      <member></member>
    </el-col>
    <el-col :span="5">
      <member></member>
    </el-col>
  </el-row>
          <el-row :gutter="10">
    <el-col :span="5">
      <member></member>
    </el-col>
    <el-col :span="5">
      <member></member>
    </el-col>
    <el-col :span="5">
      <member></member>
    </el-col>
  </el-row>


  </div>


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
</style>
