# Generated by Django 2.0.7 on 2018-07-03 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=16, verbose_name='组别')),
                ('team1', models.CharField(max_length=32, verbose_name='球队1名称')),
                ('team2', models.CharField(max_length=32, verbose_name='球队2名称')),
                ('goals1', models.CharField(max_length=32, verbose_name='球队1进球数')),
                ('goals2', models.CharField(max_length=32, verbose_name='球队2进球数')),
                ('match_time', models.DateTimeField(verbose_name='%Y-%m-%d %H:%M')),
                ('goals_difference', models.IntegerField(default=0, verbose_name='分差')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='球队名字')),
                ('name_pinyin', models.CharField(max_length=32, verbose_name='球队名拼音')),
                ('group', models.CharField(max_length=16, verbose_name='组别')),
                ('win_num', models.IntegerField(default=0, verbose_name='球队胜利场次')),
                ('lose_num', models.IntegerField(default=0, verbose_name='球队战败场次')),
                ('draw_num', models.IntegerField(default=0, verbose_name='球队战平场次')),
                ('goals', models.IntegerField(default=0, verbose_name='球队进球数')),
                ('goals_lose', models.IntegerField(default=0, verbose_name='球队失球数')),
                ('goal_difference', models.IntegerField(default=0, verbose_name='净胜球')),
                ('score', models.IntegerField(default=0, verbose_name='分数')),
                ('match_num', models.IntegerField(default=0, verbose_name='比赛场次')),
            ],
        ),
    ]
