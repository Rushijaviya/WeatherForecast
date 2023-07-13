from django.utils import timezone
from django.db import models

# Create your models here.

class WeatherData(models.Model):
    
    detailing_type_choices = (
        ('Current weather','Current weather'),
        ('Minute forecast for 1 hour','Minute forecast for 1 hour'),
        ('Hourly forecast for 48 hours','Hourly forecast for 48 hours'),
        ('Daily forecast for 7 days','Daily forecast for 7 days')
    )

    lat  = models.CharField(max_length=75)
    lon  = models.CharField(max_length=75)
    time = models.DateTimeField(default=timezone.now)
    data = models.TextField()
    detailing_type = models.CharField(max_length=35,choices = detailing_type_choices, default = 'Current weather')