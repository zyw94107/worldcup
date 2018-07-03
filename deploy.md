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

### 2.配置uwsgi

安装```uwsgi```,步骤省略

在项目根目录```worldcup```新建uswgi.ini文件，以及run.log文件

并编辑uswgi.ini，输入以下内容：
```
[uwsgi]
chdir = /home/ubuntu/site/worldcup   //项目根目录
module = worldcup.wsgi:application   //指定wsgi模块
socket = 127.0.0.1:8000              //对本机8000端口提供服务
master = true                        //主进程
daemonize = /home/ubuntu/site/worldcup/run.log //设置日志文件
disable-logging = true              
```
### 3.配置Nginx
备份```/etc/nginx/sites-available```文件夹内的```default```文件,然后编辑
```
server {
    listen 80;
    listen [::]:80;
    server_name 123.207.60.129;  //服务器ip，这里为我自己的服务器ip

    location / {
        include  uwsgi_params;
                uwsgi_pass  127.0.0.1:8000;
    }
}
```
重启nginx

```sudo service nginx restart```

### 4.启动服务

将```wcup/setting.py```中更改为```ALLOWED_HOSTS = ['*']```，```DEBUG = False```

到项目根目录，执行
```
$ sudo uwsgi uwsgi.ini
```

