from django.db import models


class City(models.Model):
    city = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)


class SiteWeather1(models.Model):
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField()
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)
    temperature = models.FloatField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)


class SiteWeather2(models.Model):
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField()
    latitude = models.FloatField(default=None)
    longitude = models.FloatField(default=None)
    temperature = models.FloatField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
