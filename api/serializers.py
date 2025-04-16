from rest_framework import serializers
from dashboard.models import (
    ClimateData, AirQualityData, BiodiversityData, 
    OceanHealthData, DeforestationData
)

class ClimateDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClimateData
        fields = '__all__'

class AirQualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = AirQualityData
        fields = '__all__'

class BiodiversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BiodiversityData
        fields = '__all__'

class OceanDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = OceanHealthData
        fields = '__all__'

class ForestDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeforestationData
        fields = '__all__'