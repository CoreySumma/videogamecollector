from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game

# Create your views here.
# Define the home view

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
  fields = ['title', 'description', 'progress', 'platform'] 
  success_url = '/games'
  # ALTERNATIVE ---> fields = '__all__' 

class GameUpdate(UpdateView):
  model = Game
  fields = ['progress']

class GameDelete(DeleteView):
  model = Game
  success_url = '/games'

def assoc_game(request, game_id):
  game = Game.objects.get(id=game_id)
  game.playing=True
  game.save()
  return redirect('index')

def unassoc_game(request, game_id):
  game = Game.objects.get(id=game_id)
  game.playing=False
  game.save()
  return redirect('index')