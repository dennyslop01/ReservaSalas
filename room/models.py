from django.db import models

from django.db import models
from datetime import date, datetime

from client.models import Client

class Room(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    phone = models.CharField(max_length=12, blank=False, null=False)
    address = models.CharField(max_length=50, blank=False, null=False)
    date_start = models.DateField(default=date.today)
    notes = models.TextField(blank=False, null=False)
    disable = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
   client = models.ForeignKey(Client, on_delete=models.CASCADE)
   room = models.ForeignKey(Room, on_delete=models.CASCADE)
   date_start = models.DateTimeField(default=datetime.now)
   date_end = models.DateTimeField(null=True)