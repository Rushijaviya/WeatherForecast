from django.urls import path
from .views import WeatherForecastDataViews

urlpatterns = [
    path('get-weatherforecast-data',WeatherForecastDataViews.as_view(),name='weatherforecast'),
]