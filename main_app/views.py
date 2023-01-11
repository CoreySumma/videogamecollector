from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Game

games = [
  {'title' : 'Demon Souls', 'description' : 'An action role-playing game where players take on the role of an adventurer, whose gender and appearance are customized at the beginning of the game, exploring the cursed land of Boletaria.'},
  {'title' : 'Little Nightmares 2', 'description' : 'A suspense adventure game in which you play as Mono, a young boy trapped in a world that has been distorted by an evil transmission.'},
  {'title' : 'World of Warcraft', 'description' : 'Set in the fictional world of Azeroth, WoW allows players to create avatar-style characters and explore a sprawling universe while interacting with other players'},
]

# Create your views here.
# Define the home view
# **REMINDER** Include an .html file extension
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', {
    'games': games
  })

def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  return render(request, 'games/detail.html', {
    'game': game
  })

class GameCreate(CreateView):
  model = Game
  fields = '__all__' 
  success_url = '/games'
  # ALTERNATIVE ---> fields = ['title', ect ect]