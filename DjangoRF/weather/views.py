from rest_framework import viewsets
from .models import City, SiteWeather1, SiteWeather2
from .tests import Start
from .serializers import NoteSerializer
from itertools import chain


class NoteViewSet(viewsets.ModelViewSet):
    queryset_1 = SiteWeather1.objects.all()
    queryset_2 = SiteWeather2.objects.all()
    queryset = queryset_1.union(queryset_2)
    serializer_class = NoteSerializer

    def get_queryset(self):
        start = Start()
        start.run()
        queryset_1 = SiteWeather1.objects.all()
        queryset_2 = SiteWeather2.objects.all()
        queryset = list(chain(queryset_1, queryset_2))
        return queryset


class NoteViewSetCity(viewsets.ModelViewSet):
    queryset_1 = SiteWeather1.objects.all()
    queryset_2 = SiteWeather2.objects.all()
    queryset = queryset_1.union(queryset_2)
    serializer_class = NoteSerializer

    def get_queryset(self):
        start = Start()
        start.run()

        if 'city_id' in self.kwargs:
            city_id = self.kwargs['city_id']
            queryset_1 = SiteWeather1.objects.filter(city_id=city_id)
            queryset_2 = SiteWeather2.objects.filter(city_id=city_id)
            queryset = list(chain(queryset_1, queryset_2))

            return queryset

        if 'city_name' in self.kwargs:
            city_name_input = self.kwargs['city_name']
            city_name_title = city_name_input.title()
            city_object = City.objects.all().filter(city=city_name_title)
            city_id = city_object[0].id
            queryset_1 = SiteWeather1.objects.filter(city_id=city_id)
            queryset_2 = SiteWeather2.objects.filter(city_id=city_id)
            queryset = list(chain(queryset_1, queryset_2))

            return queryset








