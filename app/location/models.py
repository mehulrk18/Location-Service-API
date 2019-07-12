from django.db import models
from django.contrib.postgres.fields import JSONField


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
    pincode = models.CharField(max_length=6, unique=True)
    latlng = JSONField()
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE
    )

    REQUIRED_FIELDS = ['locality', 'pincode', 'latlng']

    def __str__(self):
        """String represtation of the locality"""
        return self.locality
