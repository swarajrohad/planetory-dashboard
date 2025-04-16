from django.db import models

class ClimateData(models.Model):
    date = models.DateField()
    temperature_anomaly = models.FloatField(help_text="Temperature anomaly in Celsius")
    co2_concentration = models.FloatField(help_text="CO2 concentration in PPM")
    sea_level_rise = models.FloatField(help_text="Sea level rise in mm")
    
    def __str__(self):
        return f"Climate data for {self.date}"
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Climate Data"

class AirQualityData(models.Model):
    date = models.DateField()
    # location = models.CharField(max_length=100)
    pm25 = models.FloatField(help_text="PM2.5 concentration")
    pm10 = models.FloatField(help_text="PM10 concentration")
    ozone = models.FloatField(help_text="Ozone concentration")
    no2 = models.FloatField(help_text="NO2 concentration")
    
    def __str__(self):
        # return f"Air quality data for {self.location} on {self.date}"
        return f"Air quality data for {self.date}"    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Air Quality Data"

class BiodiversityData(models.Model):
    year = models.IntegerField()
    region = models.CharField(max_length=100)
    species_count = models.IntegerField(help_text="Number of species")
    endangered_count = models.IntegerField(help_text="Number of endangered species")
    extinction_rate = models.FloatField(help_text="Extinction rate")
    
    def __str__(self):
        return f"Biodiversity data for {self.region} in {self.year}"
    
    class Meta:
        ordering = ['-year']
        verbose_name_plural = "Biodiversity Data"

class OceanHealthData(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=100)
    ocean_temperature = models.FloatField(help_text="Ocean temperature in Celsius")
    acidity_ph = models.FloatField(help_text="Ocean acidity (pH)")
    plastic_density = models.FloatField(help_text="Plastic density (particles/km²)")
    coral_health_index = models.FloatField(help_text="Coral health index (0-100)")
    
    def __str__(self):
        return f"Ocean health data for {self.location} on {self.date}"
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Ocean Health Data"

class DeforestationData(models.Model):
    year = models.IntegerField()
    # region = models.CharField(max_length=100)
    # forest_area = models.FloatField(help_text="Forest area in km²")
    deforestation_rate = models.FloatField(help_text="Deforestation rate in km²/year")
    relative_deforestation_rate = models.FloatField(help_text="Reforestation area in km²")
    
    def __str__(self):
        return f"Deforestation data {self.deforestation_rate} sq.km in {self.year}"
    
    class Meta:
        ordering = ['-year']
        verbose_name_plural = "Deforestation Data"