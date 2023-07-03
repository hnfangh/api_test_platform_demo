
**分层设计思路** 

    - controller : 控制层相当于路由层来接受前端传来的数据，把数据传给service层
    - do : dao层的实体类封装，由新增的DB字段在这个里添加
    - dao : 与数据库交互封装，从service逻辑层去数据库中执行CURD
    - service : 处理业务逻辑层，从controller层拿数据
    - server : 启动后端的服务
    
**目录**


**展示效果**