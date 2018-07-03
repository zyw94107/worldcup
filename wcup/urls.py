from django.contrib import admin
from django.urls import path, re_path

from wcup import views
app_name = 'wcup'

urlpatterns = [
    path('update_matches/', views.UpdateMatch.as_view(), name='update'),
    path('update_teams/', views.UpdateTeamInfo.as_view(), name='score'),
    path('team_list', views.TeamListView.as_view(), name='teams'),
    path('goal_dif', views.GoalDifferenceView.as_view(), name='gd'),
    path('match_goal_dif', views.MatchGoalDifferenceView.as_view(), name='mgd'),
    path('group_adv', views.TeamAdvancedOfGroupView.as_view(), name='adv'),
]
