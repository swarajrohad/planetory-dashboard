from django.contrib import admin
from .models import (
    ClimateData, AirQualityData, BiodiversityData,
    OceanHealthData, DeforestationData
)

admin.site.register(ClimateData)
admin.site.register(AirQualityData)
admin.site.register(BiodiversityData)
admin.site.register(OceanHealthData)
admin.site.register(DeforestationData)