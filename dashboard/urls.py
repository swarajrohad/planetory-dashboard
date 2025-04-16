from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('air-quality/', views.air_quality, name='air_quality'),
    path('climate-change/', views.climate_change, name='climate_change'),
    path('biodiversity/', views.biodiversity, name='biodiversity'),
    path('ocean-health/', views.ocean_health, name='ocean_health'),
    path('deforestation/', views.deforestation, name='deforestation'),
]