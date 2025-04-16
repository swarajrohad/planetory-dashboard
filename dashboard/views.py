
# Create your views here.
from django.shortcuts import render
from django.utils import timezone
from .models import (
    ClimateData, AirQualityData, BiodiversityData,
    OceanHealthData, DeforestationData
)
import json


#     api_url = "https://air-quality-api.open-meteo.com/v1/air-quality?latitude=52.52&longitude=13.41&hourly=pm10,pm2_5,ozone,nitrogen_dioxide"

import requests
from datetime import datetime
from .models import AirQualityData

def fetch_and_store_air_quality_data():
      # Fetch data from the API
    response = requests.get("https://air-quality-api.open-meteo.com/v1/air-quality?latitude=52.52&longitude=13.41&hourly=pm10,pm2_5,ozone,nitrogen_dioxide")
    data = response.json()

    # Extract hourly data
    times = data['hourly']['time']
    pm10_values = data['hourly']['pm10']
    pm25_values = data['hourly']['pm2_5']
    ozone_values = data['hourly']['ozone']
    no2_values = data['hourly']['nitrogen_dioxide']

    # Loop through each data point and save it to the model
    for i in range(len(times)):
        time = datetime.fromisoformat(times[i])  # Convert ISO 8601 string to datetime
        date = time.date()  # Get only the date portion

        pm10 = pm10_values[i]
        pm25 = pm25_values[i]
        ozone = ozone_values[i]
        no2 = no2_values[i]

        # Create and save the AirQualityData instance
        AirQualityData.objects.create(
            date=date,
            pm25=pm25,
            pm10=pm10,
            ozone=ozone,
            no2=no2
        )

    print("Data saved successfully.")


def save_deforestation_data():
    url = "https://api.openepi.io/deforestation/basin?lon=30.0619&lat=-1.9441"  # <-- replace with your real API URL
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if data.get("features"):
            yearly_data = data["features"][0]["properties"]["treeloss_per_year"]

            for entry in yearly_data:
                year = entry["year"]
                deforestation_rate = entry["area"]
                relative_deforestation_rate = entry["relative_area"]

                DeforestationData.objects.update_or_create(
                    year=year,
                    defaults={
                        "deforestation_rate": deforestation_rate,
                        "relative_deforestation_rate": relative_deforestation_rate
                    }
                )
            print("Data saved to database.")
        else:
            print("No features found in API response.")
    else:
        print("Failed to fetch data:", response.status_code)


def index(request):

    # get the data from api

    today = timezone.now().date()

    latest_entry = AirQualityData.objects.order_by('-date').first()

    if latest_entry and latest_entry.date >= today:

        print("Latest entry is from today.")
    else:
        fetch_and_store_air_quality_data()
        print("No entry from today.")    

    #deforestation data
    # save_deforestation_data()

    # Get latest data for each category
    latest_climate = ClimateData.objects.order_by('-date').first()
    latest_air = AirQualityData.objects.order_by('-date').first()
    latest_biodiversity = BiodiversityData.objects.order_by('-year').first()
    latest_ocean = OceanHealthData.objects.order_by('-date').first()
    latest_forest = DeforestationData.objects.order_by('-year').first()
    
    # Get data for charts
    climate_data = list(ClimateData.objects.order_by('date').values('date', 'temperature_anomaly', 'co2_concentration')[:100])
    for item in climate_data:
        item['date'] = item['date'].strftime('%Y-%m-%d')
    
    context = {
        'latest_climate': latest_climate,   
        'latest_air': latest_air,
        'latest_biodiversity': latest_biodiversity,
        'latest_ocean': latest_ocean,
        'latest_forest': latest_forest,
        'climate_data_json': json.dumps(climate_data)
    }
    return render(request, 'dashboard/index.html', context)

def air_quality(request):
    from django.shortcuts import render
from .models import AirQualityData

def air_quality(request):
    # Get the latest 100 entries ordered by date
    air_data = AirQualityData.objects.order_by('date')[:100]

    # Prepare data for Chart.js
    chart_labels = [entry.date.strftime("%Y-%m-%d") for entry in air_data]
    pm25_data = [entry.pm25 for entry in air_data]
    pm10_data = [entry.pm10 for entry in air_data]
    ozone_data = [entry.ozone for entry in air_data]
    no2_data = [entry.no2 for entry in air_data]

    context = {
        'air_data': air_data,
        'chart_labels': chart_labels,
        'pm25_data': pm25_data,
        'pm10_data': pm10_data,
        'ozone_data': ozone_data,
        'no2_data': no2_data,
    }

    return render(request, 'dashboard/air_quality.html', context)
    

def climate_change(request):
    # Get climate data for visualization
    climate_data = ClimateData.objects.order_by('date')[:100]
    
    context = {
        'climate_data': climate_data
    }
    return render(request, 'dashboard/climate.html', context)

def biodiversity(request):
    data = BiodiversityData.objects.order_by('year')

    years = [entry.year for entry in data]
    species = [entry.species_count for entry in data]
    endangered = [entry.endangered_count for entry in data]
    extinction = [entry.extinction_rate for entry in data]

    context = {
        'years': years,
        'species': species,
        'endangered': endangered,
        'extinction': extinction,
    }
    return render(request, 'dashboard/biodiversity.html', context)

def ocean_health(request):
    ocean_data = OceanHealthData.objects.order_by('date')

    dates = [data.date.strftime("%Y-%m-%d") for data in ocean_data]
    temperature = [data.ocean_temperature for data in ocean_data]
    acidity = [data.acidity_ph for data in ocean_data]
    plastic_density = [data.plastic_density for data in ocean_data]
    coral_health = [data.coral_health_index for data in ocean_data]

    context = {
        'dates': dates,
        'temperature': temperature,
        'acidity': acidity,
        'plastic_density': plastic_density,
        'coral_health': coral_health,
    }
    return render(request, 'dashboard/ocean_health.html', context)

def deforestation(request):
    # Get deforestation data
    # Get all deforestation data ordered by year
    data = DeforestationData.objects.order_by('year')

    years = [entry.year for entry in data]
    deforestation_rates = [entry.deforestation_rate for entry in data]
    relative_deforestation_rates = [entry.relative_deforestation_rate for entry in data]

    context = {
        'years': years,
        'deforestation_rates': deforestation_rates,
        'relative_deforestation_rates': relative_deforestation_rates,
    }

    return render(request, 'dashboard/deforestation.html', context)
    # forest_data = DeforestationData.objects.order_by('-year')
    
    # context = {
    #     'forest_data': forest_data
    # }
    # return render(request, 'dashboard/deforestation.html', context)