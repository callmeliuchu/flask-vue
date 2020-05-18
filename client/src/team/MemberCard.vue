<template>
<div>
     <el-col :span="8">
         <div class="block" v-on:click="handleAvatar()"><el-avatar :size="70" :src="url"></el-avatar></div>
       <el-dialog
          title="更换封面"
          :visible.sync="dialogVisible"
          width="15%"
          :before-close="handleClose">

         <el-upload
            class="avatar-uploader"
            action="https://jsonplaceholder.typicode.com/posts/"
            :show-file-list="false"
            :on-success="handleAvatarSuccess"
            :before-upload="beforeAvatarUpload">
            <img v-if="imageUrl" :src="imageUrl" class="avatar">
            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
          </el-upload>

          <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button type="primary" @click="handleUpload()">确 定</el-button>
          </span>
        </el-dialog>
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
            'url':'https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png',
            'type':'',
            'name':'',
            'is_edit':false,
            'dialogVisible':false,
            'imageUrl': ''

        }
      },
      watch:{
          avatar_url(n,o){ //n为新值,o为旧值;
            this.url = n;
          },
          team_name(n,o){
              this.name = n;
          },
          team_type(n,o){
              this.type = n;
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
                this.dialogVisible = true;
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
          },
          handleClose(done) {
            this.$confirm('确认关闭？')
              .then(_ => {
                done();
              })
              .catch(_ => {});
         },
          handleAvatarSuccess(res, file) {
            this.imageUrl = URL.createObjectURL(file.raw);
            this.url = this.imageUrl;
          },
          handleUpload(){
            this.url = this.imageUrl;
            this.dialogVisible = false;
          },
          beforeAvatarUpload(file) {
            const isJPG = file.type === 'image/jpeg';
            const isLt2M = file.size / 1024 / 1024 < 2;

            if (!isJPG) {
              this.$message.error('上传头像图片只能是 JPG 格式!');
            }
            if (!isLt2M) {
              this.$message.error('上传头像图片大小不能超过 2MB!');
            }
            return isJPG && isLt2M;
          }
      }
  };
</script>


<style>
   .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409EFF;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>
