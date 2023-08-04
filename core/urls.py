from django.urls import path
from .views import HomePageView, PopulateDB, PopulateDevices

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page-view'),
    path('core/populate_db/', PopulateDB.as_view(), name='populate-db'),
    path('core/populate_devices/', PopulateDevices.as_view(), name='populate-devices'),
]