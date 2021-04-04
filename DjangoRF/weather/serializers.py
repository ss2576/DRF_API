from rest_framework import serializers
from .models import SiteWeather1, SiteWeather2


class NoteSerializer(serializers.ModelSerializer):

    city = serializers.SerializerMethodField('get_city')
    datetime = serializers.SerializerMethodField('get_datetime')
    site_name = serializers.SerializerMethodField('get_site_name')

    def get_site_name(self, instance):
        if isinstance(instance, SiteWeather1):
            site_name = 'www.weatherbit.io'
            return site_name

        if isinstance(instance, SiteWeather2):
            site_name = 'www.openweathermap.org'
            return site_name

    def get_city(self, instance):
        instance_city = instance.city_id
        city: int = instance_city.city
        return city

    def get_datetime(self, instance):
        instance_date = instance.datetime
        datetime: str = '{:%Y-%m-%d %H:%M}'.format(instance_date)
        return datetime

    class Meta:
        model = SiteWeather1
        fields = ('city', 'city_id', 'site_name', 'longitude', 'latitude', 'temperature', 'datetime')
