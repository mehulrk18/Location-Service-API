# from django.test import TestCase
#
# from location.models import City, Location
#
#
# def sample_city(name='Test city', country='Test country'):
#     return City.objects.create(name=name, country=country)
#
#
# class ModelTests(TestCase):
#     """Tests for the models"""
#
#     def test_verify_city(self):
#         """Test for City verification"""
#         cityName = 'Test City'
#         stateName = 'Test State'
#         countryName = 'Test Country'
#         c = City.objects.create(
#             name=cityName,
#             ut=False,
#             state=stateName,
#             country=countryName
#         )
#
#         self.assertEqual(c.name, cityName)
#         self.assertEqual(c.state, stateName)
#         self.assertEqual(c.country, countryName)
#         self.assertFalse(c.ut)
#
#     def test_verify_location(self):
#         """Test to verify location"""
#         city = sample_city()
#         payload = {
#                     'locality': 'Test Locality',
#                     'city': city,
#                     'pincode': 000000,
#                     'latlng': {'lat': 00.000, 'long': 00.000}
#         }
#         loc = Location(
#             locality=payload['locality'],
#             city=city,
#             pincode=payload['pincode'],
#             latlng=payload['latlng']
#         )
#
#         # res = self.client.post(LOCATION_URL, payload)
#
#         self.assertEqual(loc.locality, payload['locality'])
#         self.assertEqual(loc.city.name, city.name)
#         self.assertEqual(loc.pincode, payload['pincode'])
#         self.assertEqual(loc.latlng['lat'], payload['latlng']['lat'])
#         self.assertEqual(loc.latlng['long'], payload['latlng']['long'])
#
#     def test_city_str(self):
#         """Test for the string city representation"""
#         city = sample_city()
#         self.assertEqual(str(city), city.name)
#
#     def test_locality_str(self):
#         """Test the locality string representation"""
#         city = sample_city()
#
#         locality = Location.objects.create(
#             locality='Test locality',
#             pincode=000000,
#             city=city,
#             latlng={'lat': 00.000, 'long': 00.000}
#         )
#
#         self.assertEqual(str(locality), locality.locality)
