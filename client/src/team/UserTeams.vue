<template>
  <el-container>
    <el-header></el-header>
      <el-main>
        <el-row :gutter="2">
          <el-col :span="5" :push="3">
            <el-button round @click="handleCreate()">创建团队</el-button>
          </el-col>
          <el-col :span="5" :push="3">
            <el-button round @click="handleJoinTeam()">加入团队</el-button>
          </el-col>
        </el-row>
        <el-dialog
              title="提示"
              :visible.sync="dialogVisible"
              width="30%"
              :before-close="handleClose">
              <span>是否删除</span>
              <span slot="footer" class="dialog-footer">
                <el-button @click="handleCancel()">取 消</el-button>
                <el-button type="primary" @click="handleSure()">确 定</el-button>
              </span>
        </el-dialog>
        <el-dialog
              title="处理加入团队"
              :visible.sync="joinDialogVisible"
              width="30%"
              :before-close="handleClose1">
              <span>密钥:</span><el-input v-model="secret_key"></el-input>
              <span>待进组:</span><el-input v-model="team_target"></el-input>
              <span slot="footer" class="dialog-footer">
                <el-button @click="joinDialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="handleJoinTeamSure()">确 定</el-button>
              </span>
        </el-dialog>

        <el-row>
          <el-col :span="2" :push="3">
            <el-button round @click="showAll()">全部</el-button>
          </el-col>
          <el-col :span="2" :push="3">
            <el-button round @click="showJoined()">我加入的</el-button>
          </el-col>
          <el-col :span="2" :push="3">
            <el-button round @click="showCreated()">我创建的</el-button>
          </el-col>
        </el-row>

        <el-row v-for="(item,index) in arr">
          <div v-if="filter(item.team_type)">
            <el-col :span="5" :push="3">
             <member :avatar_url="item.url" :team_name="item.team_name" :team_type="item.team_type"></member>
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
            <i class="el-icon-delete" v-on:click="handleDelete(index)"></i>
            </el-col>
          </div>
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
        arr:[{'url':'111','team_name':'哈哈1','team_type':'我创建的','count':10,'updated_time':'2019-10-10 10:10:11'},
             {'url':'111','team_name':'哈哈2','team_type':'我创建的','count':11,'updated_time':'2019-10-10 10:10:11'},
             {'url':'111','team_name':'哈哈3','team_type':'我加入的','count':12,'updated_time':'2019-10-10 10:10:11'},
             {'url':'111','team_name':'哈哈4','team_type':'我加入的','count':13,'updated_time':'2019-10-10 10:10:11'},
             {'url':'111','team_name':'哈哈5','team_type':'其他人的','count':14,'updated_time':'2019-10-10 10:10:11','secret_key':'123'}],
        dialogVisible:false,
        deleteIndex:-1,
        filter_arr:['我加入的','我创建的','其他人的'],
        joinDialogVisible:false,
        team_target:'哈哈5',
        secret_key:'123',
      }
    },

      components:{
        member
      },
      methods:{
          filter(team_type){
              for(let value of this.filter_arr){
                  if(value == team_type){
                      return true;
                  }
              }
              return false;
          },
          handleJoinTeam(){
              this.joinDialogVisible = true;
          },
          showAll(){
             this.filter_arr = ['我加入的','我创建的'];
          },
          showJoined(){
             this.filter_arr = ['我加入的'];
          },
          showCreated(){
             this.filter_arr = ['我创建的'];
          },
          handleCreate(){
            this.arr.splice(0,0,{'url':'','team_name':'默认名字','team_type':'我创建的','count':0,'updated_time':Date.now().toString()});
            // let obj = this.arr[this.arr.length-1];
            // for(let i=this.arr.length-1;i>0;i--){
            //     this.arr[i] = this.arr[i-1];
            // }
            // alert(JSON.stringify(obj));
            // this.arr[0] = obj;
          },
          handleDelete(index){
              this.deleteIndex = index
              this.dialogVisible = true
            // this.arr.splice(index,1);

          },
          handleJoinTeamSure(){
              // this.joinDialogVisible = false;
              let target = null;
              let index = -1;
              for(let i=0;i<this.arr.length;i++){
                  let obj = this.arr[i];
                  if(obj.team_name == this.team_target){
                      target = obj;
                      index = i;
                      break;
                  }
              }
              if(target){
                  if('secret_key' in target){
                      if(target.secret_key == this.secret_key){
                          this.arr[index].team_type = '我加入的';
                          this.joinDialogVisible = false;

                      }else{
                          this.$message('密钥错误');
                      }
                  }else{
                      this.$message('已经加入过该组织');
                  }
              }else{
                  this.$message('没有这个组织');
              }

          },
          handleClose(){
            this.$confirm('确认关闭？')
              .then(_ => {
                this.dialogVisible = false;
              })
              .catch(_ => {});
          },
          handleClose1(){
            this.$confirm('确认关闭？')
              .then(_ => {
                this.joinDialogVisible = false;
              })
              .catch(_ => {});
          },
          handleCancel(){
              this.dialogVisible = false;
          },
          handleSure(){
              this.arr.splice(this.deleteIndex,1);
              this.dialogVisible = false;
          }
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
