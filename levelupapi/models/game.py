"""Event model module"""
from django.db import models

class Game(models.Model):
    """Event database model"""
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    title = models.CharField(max_length=75)
    number_of_players= models.IntegerField()
    skill_level= models.IntegerField()
    gametype = models.ForeignKey("GameType", on_delete=models.CASCADE)
