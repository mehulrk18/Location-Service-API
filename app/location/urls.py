from django.urls import path, include
from rest_framework.routers import DefaultRouter

from location import views


r = DefaultRouter()

r.register('city', views.CityViewSet)
r.register('location', views.LocationViewSet)

app_name = 'location'

urlpatterns = [
    path('', include(r.urls))
]
#             path('city/', views.CityViewSet,
#                  name='city'),
#             path('location/', views.LocationViewSet,
#                  name='location'),
#             # path('me/', views.ManageUserView.as_view(), name='me'),
# ]
