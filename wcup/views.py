from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from django.core import serializers
from xpinyin import Pinyin
# Create your views here.

import json

from wcup import models


class UpdateMatch(View):
    def get(self, request):
        with open('/Users/yiwei/PycharmProjects/worldcup/wcup/world_cup.json', "r", encoding='utf8') as f:
            datas = json.load(f)
            # 导入json文件，并解析，然后写入Match表中
            for data in datas:
                match_time = data['date'] + " " + data['time']
                goals_dif = abs(int(data['Score1']) - int(data['Score2']))
                info = models.Match.objects.get_or_create(group=data['group'], team1=data['Team1'], team2=data['Team2'],
                                                          goals1=int(data['Score1']), goals2=int(data['Score2']),
                                                          match_time=match_time, goals_difference=goals_dif,
                                                          )
                # 关闭文件
                f.close()

        # 取出比赛中的球队数据，并去重，将球队数据写入Team表中
        p = Pinyin()
        objs = models.Match.objects.values('team1', 'group').distinct()
        for obj in objs:
            name = obj.get('team1')
            city_pinyin = p.get_pinyin(name, '')
            info = models.Team.objects.get_or_create(name=name, name_pinyi=city_pinyin, group=obj.get('group'))
        return HttpResponse("suc")


class UpdateTeamInfo(View):
    def get(self, request):
        matches = models.Match.objects.all()
        for match in matches:
            team1 = match.team1
            team2 = match.team2
            goals1 = int(match.goals1)
            goals2 = int(match.goals2)
            if goals1 > goals2:
                goal_difference = goals1 - goals2
                # team1 取胜，更新得分，进球，净胜球等数据
                team_1 = models.Team.objects.get(name=team1)
                # 判断球队进行场次是达到3次，若达到三次则不进行更新
                if team_1.match_num < 3:
                    team_1.goals += goals1
                    team_1.goals_lose += goals2
                    team_1.goal_difference += goal_difference
                    team_1.score += 3
                    team_1.win_num += 1
                    team_1.match_num += 1
                    # team2 输，更新数据
                    team_2 = models.Team.objects.get(name=team2)
                    team_2.goals += goals2
                    team_2.goals_lose += goals1
                    team_2.goal_difference -= goal_difference
                    team_2.lose_num += 1
                    team_2.match_num += 1
                    # 保存数据
                    team_1.save()
                    team_2.save()
                else:
                    return HttpResponse('已经导入')

            elif goals1 == goals2:
                # team1,team2 战平，更新得分，进球，净胜球等数据
                team_1 = models.Team.objects.get(name=team1)
                if team_1.match_num < 3:
                    team_1.goals += goals1
                    team_1.goals_lose += goals2
                    team_1.score += 1
                    team_1.draw_num += 1
                    team_1.match_num += 1
                    # team2 输，更新数据
                    team_2 = models.Team.objects.get(name=team2)
                    team_2.goals += goals2
                    team_2.goals_lose += goals1
                    team_2.draw_num += 1
                    team_2.match_num += 1
                    team_2.score += 1
                    team_1.save()
                    team_2.save()
                else:
                    return HttpResponse('已经导入')
            elif goals2 > goals1:
                goal_difference = goals2 - goals1
                # team2 取胜，更新得分，进球，净胜球等数据
                team_2 = models.Team.objects.get(name=team2)
                if team_2.match_num < 3:
                    team_2.goals += goals1
                    team_2.goals_lose += goals2
                    team_2.goal_difference += goal_difference
                    team_2.score += 3
                    team_2.win_num += 1
                    team_2.match_num += 1
                    # team1 输，更新数据
                    team_1 = models.Team.objects.get(name=team1)
                    team_1.goals += goals2
                    team_1.goals_lose += goals1
                    team_1.goal_difference -= goal_difference
                    team_1.lose_num += 1
                    team_1.match_num += 1
                    # 保存数据
                    team_1.save()
                    team_2.save()
                else:
                    return HttpResponse('已经导入')

        return HttpResponse("suc")


class TeamListView(View):
    # 返回所有32强所有球队，要求使用分页(参数page和per_page分别代表第几页和每页多少条记录）
    def get(self, request):
        all_teams = models.Team.objects.all()
        team_list = []
        team_count = all_teams.count()

        # 获取GET page和per_page参数，默认值为1和5
        page = int(request.GET.get('page', 1))
        per_page = int(request.GET.get("per_page", 5))
        # 判断page是否大于可分页数目，若大于则将page设置为最大分页数。
        page = team_count // int(per_page) + 1 if int(page) > (team_count // int(per_page)) + 1 else page
        start_num = (page - 1) * per_page + 1
        # 根据队伍名拼音排序。
        all_teams_sort = all_teams.order_by('name_pinyin')[start_num:start_num + per_page]

        # 获取筛选出来的球队名
        for team in all_teams_sort:
            team_list.append(team.name)
        # 转换成json格式
        team_list_json = json.dumps(team_list,  ensure_ascii=False)
        return HttpResponse(team_list_json, 'application/json', charset='utf-8')


class GoalDifferenceView(View):
    # 返回每个小组净胜球最多的球队
    def get(self, request):
        gd_list = []
        group_list = [chr(i) for i in range(65, 73)]
        for group in group_list:
            gd = models.Team.objects.filter(group=group).order_by('-score', 'name_pinyin')[:1]
            gd_list.append({group: [gd.get().name, gd.get().score]})
        print(gd_list)
        gd_list_json = json.dumps(gd_list,  ensure_ascii=False)
        return HttpResponse(gd_list_json, 'application/json', charset='utf-8')


class MatchGoalDifferenceView(View):
    # 返回比分差距最大的3场比赛记录(按照比赛日期逆序排序)
    def get(self, request):
        mgds_list = []
        mgd_list = models.Match.objects.all().order_by('-goals_difference', 'match_time')[:3]
        for mgd in mgd_list:
            mgds_list.append(["{}:{}".format(mgd.team1, mgd.team2),
                              "{}:{}".format(mgd.goals1, mgd.goals2),
                              "{}".format(mgd.match_time)])

        mgds_list_json = json.dumps(mgds_list, ensure_ascii=False)
        print(mgds_list_json)
        return HttpResponse(mgds_list_json, content_type='application/json', charset='utf-8')


class TeamAdvancedOfGroupView(View):
    # 返回每个小组晋级的两只球队(排名优先级：积分、净胜球、球队名)；
    def get(self, request):
        advs_list = []
        group_list = [chr(i) for i in range(65, 73)]
        for group in group_list:
            adv_list = []
            adv_teams = models.Team.objects.filter(group=group).order_by('-score',
                                                                         '-goal_difference',
                                                                         '-name_pinyin')[:2]
            for adv_team in adv_teams:
                adv_list.append([adv_team.name, adv_team.score])
            advs_list.append({group: adv_list})
        advs_list_json = json.dumps(advs_list,  ensure_ascii=False)
        return HttpResponse(advs_list_json, 'application/json', charset='utf-8')
