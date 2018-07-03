# worldcup
2018世界杯小组赛情况实现一些查询功能接口

本项目使用django web框架搭建

## 接口：
分数相同根据球队名正序排序；

未完成的小组赛在合理情况内自行决定比赛分数

1、返回所有32强所有球队，要求使用分页(参数page和per_page分别代表第几页和每页多少条记录)

2、返回每个小组净胜球最多的球队

3、返回比分差距最大的3场比赛记录(按照比赛日期逆序排序)

4、返回每个小组晋级的两只球队(排名优先级：积分、净胜球、球队名)

⬇️⬇️⬇️

[接口文档](https://github.com/zyw94107/worldcup/blob/master/api.md)

## 数据导入
首先根据数据参考链接http://2018.sina.com.cn/schedule/group.shtml

获取json格式的比赛数据，并保存在wcup目录中[world_cup.json](https://github.com/zyw94107/worldcup/blob/master/wcup/world_cup.json)

```http://*/wcup/update_matches```自动更新比赛数据，并保存在数据库

```http://*/wcup/update_teams```根据比赛数据，自动更新队伍信息，包括：胜场次，负场次，进球，失球，净胜球，得分等信息

## 项目部署

参考[部署文档](https://github.com/zyw94107/worldcup/blob/master/deploy.md)
