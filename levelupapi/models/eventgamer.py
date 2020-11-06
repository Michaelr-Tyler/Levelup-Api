"""Eventgame model module"""
from levelupapi.models import event
from django.db import models

class EventGamer(models.Model):
    """Eventgame database model"""
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="registrations")
    event = models.ForeignKey("Event", on_delete=models.CASCADE, related_name="registrations")
    