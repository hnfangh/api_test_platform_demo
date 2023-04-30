<template>
    <el-tabs :tab-position="tabPosition" style="height: 200px;">
      <el-tab-pane label="用户管理">用户管理</el-tab-pane>
      <el-tab-pane label="配置管理">配置管理</el-tab-pane>
      <el-tab-pane label="角色管理">角色管理</el-tab-pane>
      <el-table
      :data="tableData"
      border
      style="width: 100%">
      <el-table-column
        fixed
        prop="userid"
        label="ID"
        width="100">
      </el-table-column>
      <el-table-column
        prop="name"
        label="姓名"
        width="120">
      </el-table-column>
      <el-table-column
        prop="password"
        label="密码"
        width="120">
      </el-table-column>
      <el-table-column
        label="操作"
        width="100">
        <template slot-scope="scope">
          <el-button  @click.native.prevent="deleteRow(scope.$index, tableData)" type="text" size="small">删除</el-button>
          <el-button type="text" size="small">编辑</el-button>
        </template>
      </el-table-column>
    </el-table>
    </el-tabs>
  </template>
  
  <script>
    export default {
      methods: {
        handleClick(row) {
          console.log(row);
        },
        deleteRow(index, rows) {
        rows.splice(index, 1);
        }
      },
  
      data() {
        return {
          // tabPosition: 'left',
          tableData: [{
            userid: '001',
            name: '王小虎',
            password: 'abcdnfgh',
          }, {
            userid: '002',
            name: '王小虎',
            password: '13578hjhj',
          }, {
            userid: '003',
            name: '王小虎',
            password: '1897525uilry',
          }, {
            userid: '004',
            name: '王小虎',
            password: '13175!@#',
          }]
        }
      }
    }
  </script>