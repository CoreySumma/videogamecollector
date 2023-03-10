from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Game(models.Model):
  title = models.CharField(max_length=150)
  description = models.CharField(max_length=250)
  progress = models.CharField(max_length=300)
  platform=models.CharField(max_length=50)
  playing=models.BooleanField(default=False)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  # rating = models.IntegerChoices()

  def __str__(self): 
    return self.title

  def get_absolute_url(self):
    return reverse('detail', kwargs={'game_id' : self.id})

# Class Photo Model

class Photo(models.Model):
  url = models.CharField(max_length=200)
  game = models.ForeignKey(Game, on_delete=models.CASCADE)

  def __str__(self):
    return f"Photo for game_id: {self.game_id} @{self.url}"