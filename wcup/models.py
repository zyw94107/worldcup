from django.db import models

# Create your models here.


class Team(models.Model):
    """
    球队模型
    """
    name = models.CharField(max_length=32, verbose_name='球队名字', unique=True)
    name_pinyin = models.CharField(max_length=32, verbose_name='球队名拼音')
    group = models.CharField(max_length=16, verbose_name='组别')
    win_num = models.IntegerField(default=0, verbose_name='球队胜利场次')
    lose_num = models.IntegerField(default=0, verbose_name='球队战败场次')
    draw_num = models.IntegerField(default=0, verbose_name='球队战平场次')
    goals = models.IntegerField(default=0, verbose_name='球队进球数')
    goals_lose = models.IntegerField(default=0, verbose_name='球队失球数')
    goal_difference = models.IntegerField(default=0, verbose_name='净胜球')
    score = models.IntegerField(default=0, verbose_name='分数')
    match_num = models.IntegerField(default=0, verbose_name='比赛场次')

    def __str__(self):
        return self.name


class Match(models.Model):
    """
    比赛模型
    """
    group = models.CharField(max_length=16, verbose_name='组别')
    team1 = models.CharField(max_length=32, verbose_name='球队1名称')
    team2 = models.CharField(max_length=32, verbose_name='球队2名称')
    goals1 = models.CharField(max_length=32, verbose_name='球队1进球数')
    goals2 = models.CharField(max_length=32, verbose_name='球队2进球数')
    match_time = models.DateTimeField("%Y-%m-%d %H:%M")
    goals_difference = models.IntegerField(default=0, verbose_name='分差')

    def __str__(self):
        return "{0}组比赛：{1}:{2}".format(self.group, self.team1, self.team2)