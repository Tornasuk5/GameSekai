from django.shortcuts import render
from game.models import Game

def home(request):
    games = list(Game.objects.values())
    return render(request, 'home.html', {'games': games})

def games_list(request):
    games = list(Game.objects.values())
    return render(request, 'games_grid.html', {'games': games})