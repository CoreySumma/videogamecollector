import uuid
import boto3
import os
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Game, Photo

# Create your views here.
# Define the home view


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


@login_required
def games_index(request):
    games = Game.objects.filter(user=request.user)
    return render(request, 'games/index.html', {
        'games': games
    })


@login_required
def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/detail.html', {
        'game': game
    })


class GameCreate(LoginRequiredMixin, CreateView):
    model = Game
    fields = ['title', 'description', 'progress', 'platform']
    success_url = '/games'
    # ALTERNATIVE ---> fields = '__all__'
    # Attach game to each user below

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class GameUpdate(LoginRequiredMixin, UpdateView):
    model = Game
    fields = ['progress']


class GameDelete(LoginRequiredMixin, DeleteView):
    model = Game
    success_url = '/games'


@login_required
def assoc_game(request, game_id):
    game = Game.objects.get(id=game_id)
    game.playing = True
    game.save()
    return redirect('index')


@login_required
def unassoc_game(request, game_id):
    game = Game.objects.get(id=game_id)
    game.playing = False
    game.save()
    return redirect('index')


@login_required
def add_photo(request, game_id):
    game = Game.objects.get(id=game_id)
    if request.method == 'POST':
        # Get the photo file from the request
        photo_file = request.FILES.get('photo-file', None)
        if photo_file:
            s3 = boto3.client('s3')
            # Generate a unique key for the file
            key = uuid.uuid4().hex[:6] + \
                photo_file.name[photo_file.name.rfind('.'):]
            try:
                # Delete the existing photo
                game.photo_set.all().delete()
                # Upload the new photo
                bucket = os.environ['S3_BUCKET']
                s3.upload_fileobj(photo_file, bucket, key)
                url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
                Photo.objects.create(url=url, game_id=game_id)
            except Exception as e:
                print('An error occurred uploading file to S3')
                print(e)
    return redirect('detail', game_id=game_id)
