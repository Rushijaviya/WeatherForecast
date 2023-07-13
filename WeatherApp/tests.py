from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework.status import HTTP_400_BAD_REQUEST
# Create your tests here.

class WeatherForecastTestCase(APITestCase):
    def test_weather_forecast(self):
        response=self.client.get(reverse('weatherforecast'))
        self.assertEqual(response.status_code,HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['cod'],'400')