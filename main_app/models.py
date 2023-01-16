from django.db import models
from django.urls import reverse

# Create your models here.
class Game(models.Model):
  title = models.CharField(max_length=150)
  description = models.CharField(max_length=250)
  progress = models.CharField(max_length=300)
  platform=models.CharField(max_length=50)
  playing=models.BooleanField(default=False)
  # rating = models.IntegerChoices()

  def __str__(self): 
    return self.title

  def get_absolute_url(self):
    return reverse('detail', kwargs={'game_id' : self.id})

# class Difficulty(models):