from datetime import timedelta
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
)
from .models import WeatherData
from django.utils import timezone
import requests
from django.conf import settings
# Create your views here.

class WeatherForecastDataViews(APIView):

    def get(self,request):
        lat = self.request.GET.get('lat')
        lon = self.request.GET.get('lon')
        # detailing_type = self.request.GET.get('detailing_type')
        detailing_type = 'Current weather'      # free version of API only supports detailing type of Current weather
        curr_time = timezone.now()
        max_prev_time = curr_time - timedelta(minutes=10)
        weather_query = WeatherData.objects.filter(lat=lat,lon=lon,detailing_type=detailing_type,time__lte=curr_time,time__gte=max_prev_time)
        
        if weather_query:
            data = weather_query.latest('time').data
            data = eval(data)
        else:
            data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={settings.WEATHER_API_KEY}")
            if data.status_code!=200:
                return Response(data.json(),status=HTTP_400_BAD_REQUEST)
            data = data.json()
            weather_query = WeatherData.objects.filter(lat=lat,lon=lon,detailing_type=detailing_type)
            if weather_query:
                weather_query = weather_query.latest('time')
                weather_query.data = data
                weather_query.time = timezone.now()
                weather_query.save()
            else:
                WeatherData.objects.create(lat=lat,lon=lon,detailing_type=detailing_type,data=data)                

        return Response(data,status=HTTP_200_OK)