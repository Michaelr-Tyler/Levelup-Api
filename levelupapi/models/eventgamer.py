"""Eventgame model module"""
from django.db import models

class EventGamer(models.Model):
    """Eventgame database model"""
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="registrations")
    game = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="registrations")