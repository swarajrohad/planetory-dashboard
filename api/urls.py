from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'climate-data', views.ClimateDataViewSet)
router.register(r'air-quality', views.AirQualityViewSet)
router.register(r'biodiversity', views.BiodiversityViewSet)
router.register(r'ocean-data', views.OceanDataViewSet)
router.register(r'forest-data', views.ForestDataViewSet)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
]