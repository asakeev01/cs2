from django.shortcuts import render

from .models import *

def teams(request):
    team_list = Team.objects.all()
    context = {"team_list": team_list}
    return render(request, "players/index.html", context)

def men(request, team_id):
    men = Man.objects.filter(team_id=team_id)
    context = {"men_list": men}
    return render(request, "players/men.html", context)