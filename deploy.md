# 部署文档

## 部署依赖环境

系统版本 ```Ubuntu 16.04.1 ```
Nginx版本 ```nginx/1.14.0```
Python版本 ```Python 3.5.2```

## 步骤
### 1.获取在github上的源码并安装依赖包和uswgi包

新建文件夹用来保存项目并转到site文件夹中
```mkdir /home/ubuntu/site/```
```
$ git clone https://github.com/zyw94107/worldcup.git
$ cd worldcup
```
安装 virtualenv 并 进入项目中虚拟环境,安装依赖包
```pip install -r requirements```

安装```uwsgi```,步骤省略

在项目根目录```worldcup```新建uswgi.ini文件，以及run.log文件

并编辑uswgi.ini，输入以下内容：
