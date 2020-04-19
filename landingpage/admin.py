from django.contrib import admin
from django.contrib.gis.geos import Point
from datetime import datetime
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

from leaflet.admin import LeafletGeoAdmin

from .models import Avian14to17Data, EmpresTwoYearOutbreakData, HumanCasesDataset, GisaidEpifluEuropeIsolateData, \
    OpenFluFlockOutbreakData, EmpresDomesticWildHuman

class EmpresTwoYearOutbreakDataAdmin(LeafletGeoAdmin):
    pass
admin.site.register(EmpresTwoYearOutbreakData)


class Avian14to17DataAdmin(LeafletGeoAdmin):
    pass
admin.site.register(Avian14to17Data)


class HumanCasesDatasetAdmin(LeafletGeoAdmin):
    pass
admin.site.register(HumanCasesDataset)


class GisaidEpifluEuropeIsolateDataAdmin(LeafletGeoAdmin):
    pass
admin.site.register(GisaidEpifluEuropeIsolateData)


class OpenFluFlockOutbreakDataAdmin(LeafletGeoAdmin):
    pass
admin.site.register(OpenFluFlockOutbreakData)


# Main map dataset
class EmpresDomesticWildHumanAdmin(LeafletGeoAdmin):
    pass

# Register model in admin page
admin.site.register(EmpresDomesticWildHuman)

# Pandas excelReader reads data spreadsheet
# and uploads the data to the model in the database:

df_excelReader = pd.read_excel('./empresDomesticWildHuman.xlsx')
df_excelReader = df_excelReader.fillna( 0 )

# # The below for-loop will help filter out corrupt rows of data, if present in the dataset
for index, row in df_excelReader.iterrows():
    try:
        latitude = row['latitude']
        longitude = row['longitude']
        geom = Point(longitude, latitude)
        # print ( 'Lg {}, Lt {} --- Geom {}'.format(longitude, latitude, geom ))
        EmpresDomesticWildHuman( source = row['source'],
                    latitude = latitude,
                    longitude = longitude,
                    region = row['region'],
                    country = row['country'],
                    admin1 = row['admin1'],
                    localityName = row['localityName'],
                    localityQuality = row['localityQuality'],
                    observationDate = row['observationDate'],
                    reportingDate = row['reportingDate'],
                    reportingYear=row['reportingYear'],
                    serotypes=row['serotypes'],
                    birdType=row['birdType'],
                    speciesDescription = row['speciesDescription'],
                    sumAtRisk = row['sumAtRisk'],
                    sumCases = row['sumCases'],
                    sumDeaths = row['sumDeaths'],
                    sumDestroyed = row['sumDestroyed'],
                    sumSlaughtered = row['sumSlaughtered'],
                    humansGenderDesc = row['humansGenderDesc'],
                    humansAge = row['humansAge'],
                    humansAffected = row['humansAffected'],
                    humansDeaths = row['humansDeaths'],
                    geom = geom ).save()

    except Exception as e:
        print ('!!! ERROR !!! - ROW Index {}, ROW {}'.format(index, row))
        print (e)
        print ('-------')

