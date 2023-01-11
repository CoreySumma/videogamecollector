from django.db import models

# Create your models here.
class Game(models.Model):
  title = models.CharField(max_length=150)
  description = models.CharField(max_length=250)
  progress = models.CharField(max_length=300)
  # rating = models.IntegerChoices()