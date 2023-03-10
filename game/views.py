from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from .models import Game

# Create your views here.

def game(request, game_name_url):
    game = Game.objects.get(name_url=game_name_url)
    return render(request, 'game_sheet.html', {'game': game})