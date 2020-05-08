<template>
  <el-container>
    <el-header></el-header>
      <el-main>
        <el-row :gutter="2">
          <el-col :span="5" :push="3">
            <el-button round>创建团队</el-button>
          </el-col>
          <el-col :span="5" :push="3">
            <el-button round>加入团队</el-button>
          </el-col>
        </el-row>


        <el-row>
          <el-col :span="2" :push="3">
            <el-button round>全部</el-button>
          </el-col>
          <el-col :span="2" :push="3">
            <el-button round>我加入的</el-button>
          </el-col>
          <el-col :span="2" :push="3">
            <el-button round>我创建的</el-button>
          </el-col>
        </el-row>

        <el-row v-for="item in arr">
          <el-col :span="5" :push="3">
           <member :avatar_url="item.team.url" :team_name="item.team.team_name" :team_type="item.team.team_type"></member>
         </el-col>
          <el-col :span="5" :push="3">
              <div>人数</div>
             <div>{{item.count}}</div>
         </el-col>
          <el-col :span="5" :push="3">
              <div>更新时间</div>
             <div>{{item.updated_time}}</div>
         </el-col>
          <el-col :span="5" :push="3">
            <i class="el-icon-delete"></i>
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
        sizeList: ["large", "medium", "small"],
        arr:[{'team':{'url':'111','team_name':'哈哈','team_type':'哈哈哈哈'},'count':10,'updated_time':'2019-10-10 10:10:11'},
             {'team':{'url':'111','team_name':'哈哈','team_type':'哈哈哈哈'},'count':10,'updated_time':'2019-10-10 10:10:11'},
             {'team':{'url':'111','team_name':'哈哈','team_type':'哈哈哈哈'},'count':10,'updated_time':'2019-10-10 10:10:11'},
             {'team':{'url':'111','team_name':'哈哈','team_type':'哈哈哈哈'},'count':10,'updated_time':'2019-10-10 10:10:11'}]
      }
    },
      components:{
        member
      }
  }

</script>

<style>
    .row-bg {
    padding: 10px 0;
    background-color: #f9fafc;
  }
    .el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
</style>
