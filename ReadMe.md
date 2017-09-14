中山大学
潘茂林
电影订票系统
软件分析与设计
课程作业
@copyright: 14331017

# 访问:<120.78.64.41:5266> 查看最终效果(有效期至2018-03-14)

## 安装方法:

### 1.mysql 安装
`sudo apt-get install mysql-server mysql-client libmysqlclient-dev`

### 2.python2.7 环境安装
`pip install tornado torndb mysql-python`

### 3.数据库创建
* `数据库文件位于doc文件夹下的formal.sql,已有少量测试数据`
* `进入mysql,创建database`
* `mysql -u root -p <YOUR PASSWORD>`
* `create database <DB_NAME>`
* `source <formal.sql FILE PATH>`

### 4.修改settings.py
`改变最下方与sql链接有关的即可`
`DATABSE PASSWORD USER HOST`

### 5.启动
`python app.py`

## 概况

### 技术栈
* mysql 数据库
* python2.7 + tornado 服务器
* bootstrap 前端

### 来源
* 前端基本仿照 <https://github.com/littlethunder/ustchacker.com>完成,logo未换
* 座位选择为自己写的简单button列表实现
* 再次感谢 USTC HACKER
