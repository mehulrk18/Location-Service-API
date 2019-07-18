from django.db import models
# from django_earthdistance.models import EarthDistanceQuerySet


class City(models.Model):
    """City Model Class"""

    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255)
    ut = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['name', 'country']

    def __str__(self):
        """String repestation of City"""
        return self.name

    def create(self, name, country, ut, state=None):
        """Create city """
        if not ut:
            return self.create(name, country, ut, state)
        else:
            return self.create(name, country, ut, None)


class Location(models.Model):
    """Location Model Class"""

    locality = models.CharField(max_length=255)
    # pincode = models.DecimalField(max_digits=6, decimal_places=0)
    pincode = models.CharField(max_length=6)
    latitude = models.FloatField()  # (max_digits=8, decimal_places=5)
    longitude = models.FloatField()  # (max_digits=8, decimal_places=5)

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE
    )

    REQUIRED_FIELDS = ['locality', 'pincode', 'latitude', 'longitude']
    # objects = EarthDistanceQuerySet.as_manager()
    #
    # def in_range(self, range_in_meters, **kwargs):
    #     return filter_in_range(
    #         queryset=self.__class__.objects,
    #         latitude=self.latitude,
    #         longitude=self.longitude,
    #         range_in_meters=range_in_meters,
    #         latitude_column_name="latitude",
    #         longitude_column_name="longitude",
    #         **kwargs,
    #         )

    def __str__(self):
        """String represtation of the locality"""
        return self.locality
