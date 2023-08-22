from django.db import models
from datetime import date

class Client(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    phone = models.CharField(max_length=12, blank=False, null=False)
    mobile = models.CharField(max_length=12, blank=False, null=False)
    email = models.EmailField()
    company = models.CharField(max_length=50, blank=False, null=False)
    date_start = models.DateField(default=date.today)
    dni = models.CharField(max_length=12, blank=False, null=False)
    notes = models.TextField(blank=False, null=False)
    
    def __str__(self):
        return self.name