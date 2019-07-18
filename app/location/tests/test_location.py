# from django.test import TestCase
# from django.urls import reverse
#
# # from rest_framework import status
# from rest_framework.test import APIClient
#
# from location.models import City, Location
# from location.serializers import LocationSerializer
#
# LOC_URL = reverse('location:location-list')
#
#
# def sample_city(name='Test city', country='Test country'):
#     return City.objects.create(name=name, country=country)
#
#
# def sample_location(locality='Test Locality', pincode='000000',
#                     latlng={'lat': 00.000, 'long': 00.000}, city=None):
#     """Sample Location"""
#     if not city:
#         city = sample_city()
#
#     return Location.objects.create(
#         locality=locality, pincode=pincode, city=city, latlng=latlng
#     )
#
#
# class LocationTests(TestCase):
#     """Location Tests"""
#
#     def setUp(self):
#         self.client = APIClient()
#
#     # def test_filter_location_by_name(self):
#     #     """Test to filter location by name"""
#     #     city1 = sample_city(name='City1')
#     #     city2 = sample_city(name='City2')
#     #
#     #     loc1 = sample_location(
#     #         locality='Loc1',
#     #         pincode='000001',
#     #         city=city1,
#     #         latlng={'lat': 00.001, 'long': 00.001}
#     #     )
#     #
#     #     loc2 = sample_location(
#     #         locality='Loc2',
#     #         pincode='000002',
#     #         city=city2,
#     #         latlng={'lat': 00.002, 'long': 00.002}
#     #     )
#     #
#     #     loc3 = sample_location()
#     #
#     #     res = self.client.get(
#     #         LOC_URL,
#     #         {'locality': f'{loc1.locality},{loc2.locality}'}
#     #     )
#     #
#     #     serializer1 = LocationSerializer(loc1)
#     #     serializer2 = LocationSerializer(loc2)
#     #     serializer3 = LocationSerializer(loc3)
#     #
#     #     self.assertIn(serializer1.data, res.data)
#     #     self.assertIn(serializer2.data, res.data)
#         # self.assertNotIn(serializer3.data, res.data)
