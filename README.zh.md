<!--
 * @Date: 2024-03-25 15:26:27
 * @LastEditors: ThetisEliza wxf199601@gmail.com
 * @LastEditTime: 2024-03-25 19:18:40
 * @FilePath: \nuc-se-project\README.zh.md
-->
# 中北大学软件工程课程作业

该项目为中北大学软件工程课程作业，贡献者为"软件工程学到死"团队。项目通过Vue+Flask+MySQL搭建


## 技术栈

### 前端

前端主要依赖Vue，我们使用了一些更加比较通用的模块来辅助搭建前端，比如Vite、Vuetify、vuew-router和vuex等。


Vue是前端三大件融合框架，将前端HTML渲染、Javascript、CSS融合到一个Vue File中，可以响应式的控制前端渲染的内容，不需要再操作具体的Document Node。

Vite是前端构建工具，主要用来方便版本管理，一些配置等。

Vuetify是前端UI框架，内含很多支持Vue的Component，有了这些Component，可以直接将设计好的UI元素嵌套在Vue文件中，如导航栏，按钮，表格等。

Vue-router是Vue框架下常用的用来切换页面的包，可以非常快的部署不一样的页面内容。

Vuex：TODO 主要用来提供各页面的共享变量，待引入


### 后端


后端主要依赖Flask框架，用非常轻量的模块部署后端服务。数据库我们选用了MySQL作为数据库服务器。

Flask是python语言常用的后端服务框架，我们可以基于Flask快速构建后端服务，只需进行适当的配置和函数定义。

## 开发路径

### 开发链路流程


#### 1. 环境部署

##### python
python环境搭建，服务器自带python，我们仅需要在项目初始建立一个虚拟环境即可
```bash
python3 -m venv venv
```
如果没有venv可以用apt安装对应的包

##### flask
使用pip安装即可
```bash
pip3 install flask
```

##### nodejs
官网下载并解压，之后配置对应的程序路径即可 [](https://nodejs.org/en)

##### vite
使用npm安装，详细可见 [vite](https://cn.vitejs.dev/guide/)

#### 2. Demo

顺利跑通第一个功能我们选择了模拟请求所有的`队伍信息`。在这个功能中，需要前端构建一个表格用来展示所有的`队伍信息`
- 前端： vue创建一个 GroupList.vue文件，作为前端展示主文件，我们使用vuetify提供的 v-data-table-server 组件来展示数据，该组件可以显示的绑定一个js请求函数，我们采用`axios`构建这个函数发起get请求，参数默认为空
- 后端我们创建一个 get_all_groups() 函数，使用flask添加路由为 `/api/group/all` 该方法返回我们构造的模拟后端数据 `GroupList`，包含 `id`，`name`，`score`, `regularScore`的字段的一个结构化的数据，在收到该url请求时，返回json化的`groupList`列表
- 前端拿到该请求结果后，我们需要为该列表配置一个header字段，该字段会指明对获取的数据列表采用何种形式和字段展示
- 前后端调通后，我们需要把模拟的数据填入数据库中，通过调用数据库的形式来存储和管理真实数据。我们创建一个nuc_groups的表，列名和所需数据结构字段名称对应，采用python原生的pymysql包执行sql语句来直接操作mysql
  
#### 3. 主要功能
- 数据分页
  - 前端数据表组件可自行设置参数对数据进行分页，并在后端api绑定对应参数传入
  - 后端在筛选数据时，可根据分页参数组织sql语句筛选对应页的数据
- 排序：
  - 排序同分页
- 搜索
  - 前端加入文本框，可输入搜索内容，数据表组件可绑定搜索参数提供搜索功能
- 登录
  - 前端新增一个登录页面，通过文本框填入用户名和密码，并增加一个登录按钮，在登录时对后端发起post请求，如果返回成功，则记录用户名和登录状态
  - 后端直接构建了一个组用户密码字典，用来提供管理员账号
- 管理员界面
  - 前端新增一个管理员界面，该界面可以更清楚的展示团队成员，并增加编辑按钮
  - 编辑
    - 前端新增一个对话框组件，在点击编辑按钮后，设置对话框绑定的展示参数为`true`，弹出编辑框，同时复制该`group`的参数到`editingTargetGroup`，并设置`editingGroup`为`group`
    - 分数编辑采用对话框展示
    - 团队成员管理采用选择组件展示
    - 确认和取消
      - 确认按钮被点击，则认为编辑生效，会请求后端分数修改api，后端成员变更api
      - 取消按钮被点击，则认为编辑无效，会不做任何修改，将`editingTargetGroup`置为空
    - 解散团队
      - 解散按钮被点击后，会调用对话框的内部的 `v-card` 组件的隐藏功能，弹出是否确认的指示
- 前端页面
  - 主要提供三个页面：`GroupList`、`AdminEdit`和`AdminLogin`，分别用作团队展示，管理员展示和用户登录
  - 页面切换主要通过`vue-router`的`push`功能提供，切换操作绑定在需要的按钮和后端结果验证上
  
#### 4. 主要技术点说明
- 前后端分离
  - 前端主要通过node来开发，通过nginX部署，调用后端API接口实现数据交互，后端采用flask来监听请求。为了解决跨域问题，自定义flask提供的中间件，保证其他地址的请求准入以及OPTION请求的过滤
- NavBar
  - 前端采用`Navbar`导航组件，添加页面总领的连续性，有效增加了用户操作性和美观性

### TODO
1. 用户登录的完备性：目前通过直接存储用户名称的方式判断用户是否登录，后面需要加入用户验证以及采用vuex访问存储对象的形式，保证每个页面都可以获取用户登录装填
2. 后端数据库：目前采用原生数据库接口进行和数据库的交互，操作比较繁琐且容易出错，后面采用sqlArchmy包来实现更结构化和正规的操作形式