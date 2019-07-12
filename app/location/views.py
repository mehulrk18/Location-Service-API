from rest_framework import viewsets, mixins  # , status

from location.models import City, Location
from location import serializers


class CityViewSet(viewsets.ModelViewSet,
                  mixins.ListModelMixin):  # mixins.CreateModelMixin):
    """City Model Viewset"""
    serializer_class = serializers.CitySerializer
    queryset = City.objects.all()


class LocationViewSet(viewsets.ModelViewSet,
                      mixins.ListModelMixin):  # mixins.CreateModelMixin):
    """Location Model Viewset"""
    serializer_class = serializers.LocationSerializer
    queryset = Location.objects.all()
