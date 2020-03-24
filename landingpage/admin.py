from django.contrib import admin
from django.contrib.gis.geos import Point
from datetime import datetime
from leaflet.admin import LeafletGeoAdmin
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
from leaflet.admin import LeafletGeoAdmin

from .models import Avian14to17Data, EmpresTwoYearOutbreakData, HumanCasesDataset, GisaidEpifluEuropeIsolateData, \
    OpenFluFlockOutbreakData, EmpresDomesticWildHuman


#
#
#
# #################### Register your models here.#####################


class EmpresTwoYearOutbreakDataAdmin(LeafletGeoAdmin):
    pass

admin.site.register(EmpresTwoYearOutbreakData, EmpresTwoYearOutbreakDataAdmin)

# df_excelReader = pd.read_excel('/Users/anjaliraveendran/Desktop/FYP/csv/empres2yrs.xlsx')
# df_excelReader = df_excelReader.fillna( 0 )
# # df_excelReader = df_excelReader.head(3)
#
# print ( 'I am in the admin page' )
# print ( len( df_excelReader  ) )
#
# for index, row in df_excelReader.iterrows():
#     Disease = row['disease']
#     Serotypes = row['serotypes']
#     SpeciesDescription = row['speciesDescription']
#     Country = row['country']
#     SumCases = row['sumCases']
#     SumDeaths = row['sumDeaths']
#     Longitude = row['longitude']
#     Latitude = row['latitude']
#
#     EmpresTwoYearOutbreakData(  disease=Disease,
#                                 serotypes=Serotypes,
#                                 speciesDescription=SpeciesDescription,
#                                 country=Country,
#                                 sumCases=SumCases,
#                                 sumDeaths=SumDeaths,
#                                 geom= Point(Longitude,Latitude)).save()

class Avian14to17DataAdmin(LeafletGeoAdmin):
    pass

admin.site.register(Avian14to17Data, Avian14to17DataAdmin)
#
# df_excelReader = pd.read_excel('/Users/anjaliraveendran/Desktop/FYP/csv/avianData14to17.xlsx')
#
# print ( 'I am in the admin page' )
# print ( len( df_excelReader  ) )
#
#
# for index, row in df_excelReader.iterrows():
#     try:
#         latitude = row['latitude']
#         longitude = row['longitude']
#         geom = Point(longitude, latitude)
#         # print ( 'Lg {}, Lt {} --- Geom {}'.format(longitude, latitude, geom ))
#         Avian14to17Data( source = row['source'],
#                     latitude = latitude,
#                     longitude = longitude,
#                     region = row['region'],
#                     country = row['country'],
#                     admin1 = row['admin1'],
#                     localityName = row['localityName'],
#                     localityQuality = row['localityQuality'],
#                     observationDate = row['observationDate'],
#                     reportingDate = row['reportingDate'],
#                     status = row['status'],
#                     disease = row['disease'],
#                     serotypes = row['serotypes'],
#                     speciesDescription = row['speciesDescription'],
#                     sumAtRisk = row['sumAtRisk'],
#                     sumCases = row['sumCases'],
#                     sumDeaths = row['sumDeaths'],
#                     sumDestroyed = row['sumDestroyed'],
#                     sumSlaughtered = row['sumSlaughtered'],
#                     humansGenderDesc = row['humansGenderDesc'],
#                     humansAge = row['humansAge'],
#                     humansAffected = row['humansAffected'],
#                     humansDeath = row['humansDeath'],
#                     geom = geom ).save()
#     except Exception as e:
#         print ('!!! ERROR !!! - ROW Index {}, ROW {}'.format(index, row))
#         print (e)
#         print ('-------')

class HumanCasesDatasetAdmin(LeafletGeoAdmin):
    pass

admin.site.register(HumanCasesDataset, HumanCasesDatasetAdmin)
#
# df_excelReader = pd.read_excel('/Users/anjaliraveendran/Desktop/FYP/csv/humancases_world.xlsx')
# df_excelReader = df_excelReader.fillna( 0 )
#
# for index, row in df_excelReader.iterrows():
#     try:
#         HumanCasesDataset(  collector_institution = row['collector_institution'],
#                             host_identifier = row['host_identifier'],
#                             collection_year = row['collection_year'],
#                             collection_season = row['collection_season'],
#                             country = row['country'],
#                             state = row['state'],
#                             city = row['city'],
#                             age = row['age'],
#                             gender = row['gender'],
#                             subtype = row['subtype'],
#                             flu_type = row['flu_type'],
#                             strain_name = row['strain_name'],
#                             flu_test_status = row['flu_test_status'],
#                             sample_type = row['sample_type']).save()
#     except Exception as e:
#         print ('!!! ERROR !!! - ROW Index {}, ROW {}'.format(index, row))
#         print (e)
#         print ('-------')


class GisaidEpifluEuropeIsolateDataAdmin(LeafletGeoAdmin):
    pass

admin.site.register(GisaidEpifluEuropeIsolateData, GisaidEpifluEuropeIsolateDataAdmin)
#
# df_excelReader = pd.read_excel('/Users/anjaliraveendran/Desktop/FYP/csv/gisaid_epiflu_europe_isolates.xls')
# df_excelReader = df_excelReader.fillna( 0 )
#
# for index, row in df_excelReader.iterrows():
#     try:
#         GisaidEpifluEuropeIsolateData(  isolate_id = row['isolate_id'],
#                             isolate_name = row['isolate_name'],
#                             subtype = row['subtype'],
#                             passage_history = row['passage_history'],
#                             location = row['location'],
#                             host = row['host'],
#                             collection_date = row['collection_date'],
#                             update_date = row['update_date'],
#                             submission_date = row['submission_date'],
#                             host_gender = row['host_gender'],
#                             animal_specimen_source = row['animal_specimen_source'],
#                             animal_health_status = row['animal_health_status'],
#                             domestic_status = row['domestic_status']
#                             ).save()
#     except Exception as e:
#         print ('!!! ERROR !!! - ROW Index {}, ROW {}'.format(index, row))
#         print (e)
#         print ('-------')

class OpenFluFlockOutbreakDataAdmin(LeafletGeoAdmin):
    pass

admin.site.register(OpenFluFlockOutbreakData, OpenFluFlockOutbreakDataAdmin)

# df_excelReader = pd.read_excel('/Users/anjaliraveendran/Desktop/FYP/csv/openflu_flock_outbreak_data.xls')
# df_excelReader = df_excelReader.fillna( 0 )
#
# for index, row in df_excelReader.iterrows():
#     try:
#         OpenFluFlockOutbreakData(   ofl_isolate_id = row['ofl_isolate_id'],
#                                     name = row['name'],
#                                     type = row['type'],
#                                     h5_clade = row['h5_clade'],
#                                     passage = row['passage'],
#                                     collect_date = row['collect_date'],
#                                     host = row['host'],
#                                     location = row['location']
#                                     ).save()
#     except Exception as e:
#         print ('!!! ERROR !!! - ROW Index {}, ROW {}'.format(index, row))
#         print (e)
#         print ('-------')



class EmpresDomesticWildHumanAdmin(LeafletGeoAdmin):
    pass

admin.site.register(EmpresDomesticWildHuman, EmpresDomesticWildHumanAdmin)
#
# df_excelReader = pd.read_excel('/Users/anjaliraveendran/Desktop/FYP/csv/empresfinaltry.xlsx')
# df_excelReader = df_excelReader.fillna( 0 )
#
# for index, row in df_excelReader.iterrows():
#     try:
#         latitude = row['latitude']
#         longitude = row['longitude']
#         geom = Point(longitude, latitude)
#         # print ( 'Lg {}, Lt {} --- Geom {}'.format(longitude, latitude, geom ))
#         EmpresDomesticWildHuman( source = row['source'],
#                     latitude = latitude,
#                     longitude = longitude,
#                     region = row['region'],
#                     country = row['country'],
#                     admin1 = row['admin1'],
#                     localityName = row['localityName'],
#                     localityQuality = row['localityQuality'],
#                     observationDate = row['observationDate'],
#                     reportingDate = row['reportingDate'],
#                     reportingYear=row['reportingYear'],
#                     serotypes=row['serotypes'],
#                     birdType=row['birdType'],
#                     speciesDescription = row['speciesDescription'],
#                     sumAtRisk = row['sumAtRisk'],
#                     sumCases = row['sumCases'],
#                     sumDeaths = row['sumDeaths'],
#                     sumDestroyed = row['sumDestroyed'],
#                     sumSlaughtered = row['sumSlaughtered'],
#                     humansGenderDesc = row['humansGenderDesc'],
#                     humansAge = row['humansAge'],
#                     humansAffected = row['humansAffected'],
#                     humansDeaths = row['humansDeaths'],
#                     geom = geom ).save()
#
#     except Exception as e:
#         print ('!!! ERROR !!! - ROW Index {}, ROW {}'.format(index, row))
#         print (e)
#         print ('-------')
#
