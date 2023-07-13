from django.contrib import admin
from .models import WeatherData

# Register your models here.

@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ('lat','lon','time','data','detailing_type')
    search_fields = ('lat','lon','time','detailing_type')