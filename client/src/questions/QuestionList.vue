<template>
  <el-container>
  <el-header>
    <customer_header></customer_header>
  </el-header>
  <el-container>
    <el-aside width="200px">
            <div>华师教信16级讨论组</div>
             <el-tree
                :data="organizations"
                :props="defaultProps"
                accordion
                @node-click="handleNodeClick">
              </el-tree>
    </el-aside>
    <el-main>
          <div>
            <el-row>华师教信16级讨论组/高老师一班</el-row>
            <el-row>第二小组</el-row>
            <el-tree
                :data="organizations"
                :props="defaultProps"
                accordion
                @node-click="handleNodeClick">
              </el-tree>
          </div>

    </el-main>
  </el-container>
</el-container>

</template>


<script>
import customer_header from './Header'
export default {
    data () {
      return {
        circleUrl: "https://cube.elemecdn.com/3/7c/3ea6beec64369c2642b92c6726f1epng.png",
        squareUrl: "https://cube.elemecdn.com/9/c2/f0ee8a3c7c9638a54940382568c9dpng.png",
        sizeList: ["large", "medium", "small"],
        organizations:
            [{
          label: '一级 1',
          children: [{
            label: '二级 1-1',
            children: [{
              label: '三级 1-1-1'
            }]
          }]
        }, {
          label: '一级 2',
          children: [{
            label: '二级 2-1',
            children: [{
              label: '三级 2-1-1'
            }]
          }, {
            label: '二级 2-2',
            children: [{
              label: '三级 2-2-1'
            }]
          }]
        }, {
          label: '一级 3',
          children: [{
            label: '二级 3-1',
            children: [{
              label: '三级 3-1-1'
            }]
          }, {
            label: '二级 3-2',
            children: [{
              label: '三级 3-2-1'
            }]
          }]
        }]
      }
    },
      components:{
        customer_header
      }
}

</script>

<style>
    .el-header, .el-footer {
  }

  .el-aside {

  }

  .el-main {

  }
  .gap{

  }

</style>
