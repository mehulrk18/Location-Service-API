from rest_framework import serializers

from location.models import City, Location


class CitySerializer(serializers.ModelSerializer):
    """City model serializer"""

    class Meta:
        model = City
        fields = ('id', 'name', 'country', 'ut', 'state')
        read_only_fields = ('id',)

    def create(self, validated_data):
        """Create a city and save it"""
        return City.objects.create(**validated_data)


class LocationSerializer(serializers.ModelSerializer):
    """Location model serializer"""

    class Meta:
        model = Location
        fields = ('id', 'locality', 'pincode', 'city', 'latlng')
        read_only_fields = ('id',)
        extra_kwargs = {'pincode': {'min_length': 6}}

    def create(self, validated_data):
        """Create a city and save it"""
        return Location.objects.create(**validated_data)
