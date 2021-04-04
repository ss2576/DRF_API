from django.test import TestCase
from .models import City, SiteWeather1, SiteWeather2
import requests
from datetime import datetime

# Create your tests here.


class Start:
    @staticmethod
    def run():

        key_1 = 'key_1'
        key_2 = 'key_2'
        city_list = ['Moscow', 'Tokio', 'Paris', 'Habana', 'Penza', 'Canberra']
        cities_list_in_column = []
        qs_city_list = City.objects.all()

        for qs in qs_city_list:
            cities_list_in_column.append(qs.city)

        for city in city_list:
            if city not in cities_list_in_column:
                city_inst = City()
                city_inst.city = city
                city_inst.save()

                url_1 = f'https://api.weatherbit.io/v2.0/current?city={city}&key={key_1}'
                url_2 = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key_2}'
                request_1 = requests.get(url_1)
                request_2 = requests.get(url_2)
                text_1 = (request_1.json())['data'][0]
                text_2 = request_2.json()

                date_1 = datetime.strptime(text_1['ob_time'], '%Y-%m-%d %H:%M')
                date_unix = int(text_2['dt'])
                date_2 = datetime.fromtimestamp(date_unix)

                temp_2_k = text_2['main']['temp']

                site_weather_1_inst = SiteWeather1()
                site_weather_1_inst.city_id = (City.objects.filter(city=city))[0]
                site_weather_1_inst.datetime = date_1
                site_weather_1_inst.latitude = text_1['lat']
                site_weather_1_inst.longitude = text_1['lon']
                site_weather_1_inst.temperature = text_1['temp']
                site_weather_1_inst.save()

                site_weather_2_inst = SiteWeather2()
                site_weather_2_inst.city_id = (City.objects.filter(city=city))[0]
                site_weather_2_inst.datetime = date_2
                site_weather_2_inst.latitude = text_2['coord']['lat']
                site_weather_2_inst.longitude = text_2['coord']['lon']
                site_weather_2_inst.temperature = round((temp_2_k - 273.15), 1)
                site_weather_2_inst.save()

            else:
                print('такой город уже есть в таблице CITY')
