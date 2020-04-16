from __future__ import unicode_literals
from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

from django.contrib.auth.models import User
from django.db.models import Q, Model
from datetime import date

class model(models.Model):
    class Meta:
        managed = False
        abstract = True

# Initial dataset consisting of AI data of 2017 to 2018 (EMPRES FAO) (not used in final app)
class EmpresTwoYearOutbreakData(models.Model):

    disease = models.CharField(max_length=250,default='SOME STRING')
    geom    = models.PointField(blank = True, null=True,srid=4326)
    serotypes = models.CharField(max_length=250,default='SOME STRING')
    speciesDescription = models.CharField(max_length=250, default='SOME STRING')
    country = models.CharField(max_length=250, default='SOME STRING')
    sumCases = models.FloatField(default=0)
    sumDeaths = models.FloatField(default=0)

    def __str__(self):
        return self.speciesDescription

    class Meta:
        verbose_name_plural = "Empres Two Year Outbreak Data"

# Dataset consisting of AI data of 2014 to 2017 (EMPRES FAO) (not used in final app)
class Avian14to17Data(models.Model):

    source = models.CharField(max_length=250, default='SOME STRING')
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    region = models.CharField(max_length=250, default='SOME STRING')
    country = models.CharField(max_length=250, default='SOME STRING')
    admin1 = models.CharField(max_length=250, default='SOME STRING')
    localityName = models.CharField(max_length=250, default='SOME STRING')
    localityQuality = models.CharField(max_length=250, default='SOME STRING')
    observationDate = models.CharField(max_length=250, default='SOME STRING')
    reportingDate = models.CharField(max_length=250, default='SOME STRING')
    status = models.CharField(max_length=250, default='SOME STRING')
    disease = models.CharField(max_length=250,default='SOME STRING')
    serotypes = models.CharField(max_length=250,default='SOME STRING')
    speciesDescription = models.CharField(max_length=250, default='SOME STRING')
    sumAtRisk = models.CharField(max_length=250, default='SOME STRING')
    sumCases = models.FloatField(default=0)
    sumDeaths = models.FloatField(default=0)
    sumDestroyed = models.FloatField(default=0)
    sumSlaughtered = models.FloatField(default=0)
    humansGenderDesc = models.CharField(max_length=250, default='SOME STRING')
    humansAge = models.FloatField(default=0)
    humansAffected = models.FloatField(default=0)
    humansDeath = models.FloatField(default=0)
    geom    = models.PointField(blank = True, null=True,srid=4326)


    def __str__(self):
        return self.speciesDescription

    class Meta:
        verbose_name_plural = "Avian Data 2014-2017"

# Human cases of AI dataset (not used in final app)
class HumanCasesDataset(models.Model):

    collector_institution = models.CharField(max_length=250, default='SOME STRING')
    host_identifier = models.CharField(max_length=250, default='SOME STRING')
    collection_year = models.FloatField(default=0)
    collection_season = models.CharField(max_length=250, default='SOME STRING')
    country = models.CharField(max_length=250, default='SOME STRING')
    state = models.CharField(max_length=250, default='SOME STRING')
    city = models.CharField(max_length=250, default='SOME STRING')
    age = models.FloatField(default=0)
    gender = models.CharField(max_length=250, default='SOME STRING')
    subtype = models.CharField(max_length=250, default='SOME STRING')
    flu_type = models.CharField(max_length=250, default='SOME STRING')
    strain_name = models.CharField(max_length=250, default='SOME STRING')
    flu_test_status = models.CharField(max_length=250, default='SOME STRING')
    sample_type = models.CharField(max_length=250, default='SOME STRING')

    def __str__(self):
        return self.subtype

    class Meta:
        verbose_name_plural = "Human Cases Data"

# Europe Isolate data taken from GISAID (not used in final app)
class GisaidEpifluEuropeIsolateData(models.Model):

    isolate_id = models.CharField(max_length=250, default='SOME STRING')
    isolate_name = models.CharField(max_length=250, default='SOME STRING')
    subtype = models.CharField(max_length=250, default='SOME STRING')
    passage_history = models.CharField(max_length=250, default='SOME STRING')
    location = models.CharField(max_length=250, default='SOME STRING')
    host = models.CharField(max_length=250, default='SOME STRING')
    collection_date = models.CharField(max_length=250, default='SOME STRING')
    update_date = models.CharField(max_length=250, default='SOME STRING')
    submission_date = models.CharField(max_length=250, default='SOME STRING')
    host_gender = models.CharField(max_length=250, default='SOME STRING')
    animal_specimen_source = models.CharField(max_length=250, default='SOME STRING')
    animal_health_status = models.CharField(max_length=250, default='SOME STRING')
    domestic_status = models.CharField(max_length=250, default='SOME STRING')

    def __str__(self):
        return self.isolate_id

    class Meta:
        verbose_name_plural = "Gisaid Epiflu Europe Isolate Data"

# Flock Outbreak Dataset from OpenFlu DB (not used in final app)
class OpenFluFlockOutbreakData(models.Model):

    ofl_isolate_id = models.CharField(max_length=250, default='SOME STRING')
    name = models.CharField(max_length=250, default='SOME STRING')
    type = models.CharField(max_length=250, default='SOME STRING')
    h5_clade = models.CharField(max_length=250, default='SOME STRING')
    passage = models.CharField(max_length=250, default='SOME STRING')
    collect_date = models.CharField(max_length=250, default='SOME STRING')
    host = models.CharField(max_length=250, default='SOME STRING')
    location = models.CharField(max_length=250, default='SOME STRING')

    def __str__(self):
        return self.ofl_isolate_id

    class Meta:
        verbose_name_plural = "Open-Flu Flock Outbreak Data"

# Dataset used in main map (From EMPRES FAO) Contains all AI cases of 2004 to 2020.
class EmpresDomesticWildHuman(models.Model):

    source = models.CharField(max_length=250, default='SOME STRING')
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    geom = models.PointField(blank=True, null=True, srid=4326)
    region = models.CharField(max_length=250, default='SOME STRING')
    country = models.CharField(max_length=250, default='SOME STRING')
    admin1 = models.CharField(max_length=250, default='SOME STRING')
    localityName = models.CharField(max_length=250, default='SOME STRING')
    localityQuality = models.CharField(max_length=250, default='SOME STRING')
    observationDate = models.CharField(max_length=250, default='SOME STRING')
    reportingDate = models.CharField(max_length=250, default='SOME STRING')
    reportingYear = models.FloatField(default=0)
    serotypes = models.CharField(max_length=250, default='SOME STRING')
    birdType = models.CharField(max_length=250, default='SOME STRING')
    speciesDescription = models.CharField(max_length=250, default='SOME STRING')
    sumAtRisk = models.FloatField(default=0)
    sumCases = models.FloatField(default=0)
    sumDeaths = models.FloatField(default=0)
    sumDestroyed = models.FloatField(default=0)
    sumSlaughtered = models.FloatField(default=0)
    humansGenderDesc = models.CharField(max_length=250, default='SOME STRING')
    humansAge = models.FloatField(default=0)
    humansAffected = models.FloatField(default=0)
    humansDeaths = models.FloatField(default=0)

    def __str__(self):
        return self.speciesDescription

    class Meta:
        verbose_name_plural = "Empres Domestic Wild Human"
