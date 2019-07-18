from rest_framework import viewsets, mixins  # , status

from django.db.models import Q, F
# from django_earthdistance.models import EarthDistance, LlToEarth
# from django.db.models.expressions import RawSQL

# from math import sqrt

from location.models import City, Location
from location import serializers


# Location.objects.in_distance(
#     1500,
#     fields=['latitude', 'longitude'],
#     points=[0.00, 0.00]
# )


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

    # def _params_to_segs(self, qs):
    #     """Convert list of string ids to list of integers"""
    #     return [str_id for str_id in qs.split(',')]

    def get_queryset(self):
        """Returns location to the user"""
        localities = self.request.query_params.get('place')
        latlong = self.request.query_params.get('latlong')
        [lat, long] = [0.0, 0.0]

        print(lat, long)
        print("latlong ", latlong)

        # distance=EarthDistance([
        #     LlToEarth([lat, long]),
        #     LlToEarth([18.969, 72.8205])])

        # print("distance= ", distance)
        queryset = self.queryset

        if localities:
            # locality_ids = self._params_to_segs(localities)
            queryset = queryset.filter(
                Q(locality__istartswith=localities) |
                Q(city__name__istartswith=localities)
            ).annotate(
                distance=((lat-F('latitude'))**2 - (long-F('longitude'))**2)
                # distance=EarthDistance([
                #     LlToEarth([lat, long]),
                #     LlToEarth(['latitude', 'longitude'])])
            ).order_by('distance').distinct()[:2]

        if latlong:
            latlong = [float(val) for val in latlong.split(',')]
            [lat, long] = latlong

            # RSQ = RawSQL(
            #     f'SELECT (sqrt(POWER(({lat} - latitude), 2) \
            #     + POWER(({long} - longitude), 2))) FROM \
            #     location_location', 'locality'
            # )
            queryset = queryset.annotate(
                distance=((lat-F('latitude'))**2
                          + (long-F('longitude'))**2)**0.5
            ).filter(distance__lte=10).order_by('distance').distinct()

            # print(distance=EarthDistance([
            #         LlToEarth([lat, long]),
            #         LlToEarth(['latitude', 'longitude'])]))

            # queryset = queryset.annotate(
            #     distance=EarthDistance([
            #         LlToEarth([lat, long]),
            #         LlToEarth(['latitude', 'longitude'])])
            # ).filter(distance__lt=10).order_by('distance').distinct()

            # return queryset

        # return queryset.filter().annotate(
        #     v1=(lat - F('latitude'))**2
        # ).annotate(
        #     v2=(long - F('longitude'))**2
        # ).annotate(
        #     distance= sq(F('v1'), F('v2'))
        # ).order_by('distance').distinct()

        return queryset.filter()
