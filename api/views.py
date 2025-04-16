# from django.shortcuts import render

# # Create your views here.
from rest_framework import viewsets
from dashboard.models import (
    ClimateData, AirQualityData, BiodiversityData, 
    OceanHealthData, DeforestationData
)
from .serializers import (
    ClimateDataSerializer, AirQualitySerializer, BiodiversitySerializer,
    OceanDataSerializer, ForestDataSerializer
)

class ClimateDataViewSet(viewsets.ModelViewSet):
    queryset = ClimateData.objects.all()
    serializer_class = ClimateDataSerializer

class AirQualityViewSet(viewsets.ModelViewSet):
    queryset = AirQualityData.objects.all()
    serializer_class = AirQualitySerializer

class BiodiversityViewSet(viewsets.ModelViewSet):
    queryset = BiodiversityData.objects.all()
    serializer_class = BiodiversitySerializer

class OceanDataViewSet(viewsets.ModelViewSet):
    queryset = OceanHealthData.objects.all()
    serializer_class = OceanDataSerializer

class ForestDataViewSet(viewsets.ModelViewSet):
    queryset = DeforestationData.objects.all()
    serializer_class = ForestDataSerializer