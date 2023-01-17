import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game, Photo

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

def add_photo(request, game_id):
  # photo-file maps to the "name" attr on the <input>
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    # Need a unique "key" (filename)
    # It needs to keep the same file extension
    # of the file that was uploaded (.png, .jpeg, etc.)
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, game_id=game_id)
    except Exception as e:
      print('An error occurred uploading file to S3')
      print(e)
  return redirect('detail', game_id=game_id)