from django.test import SimpleTestCase
from landingpage.models import EmpresDomesticWildHuman

# This class tests the Django models we have created
# It confirms that the datatypes of the data values we upload
# to the model matches the original model attribute's datatypes
class ModelTests(SimpleTestCase):

    def test_EmpresDomesticWildHuman_default_values(self):
        ''' assert default values for the model '''
        testModel = EmpresDomesticWildHuman()

        self.assertEquals(testModel.source , 'SOME STRING')
        self.assertEquals(testModel.latitude , 0 )
        self.assertEquals(testModel.longitude , 0 )
        self.assertEquals(testModel.region , 'SOME STRING')
        self.assertEquals(testModel.country , 'SOME STRING')
        self.assertEquals(testModel.admin1 , 'SOME STRING')
        self.assertEquals(testModel.localityName , 'SOME STRING')
        self.assertEquals(testModel.localityQuality , 'SOME STRING')
        self.assertEquals(testModel.observationDate , 'SOME STRING')
        self.assertEquals(testModel.reportingDate , 'SOME STRING')
        self.assertEquals(testModel.reportingYear , 0)
        self.assertEquals(testModel.serotypes , 'SOME STRING')
        self.assertEquals(testModel.birdType , 'SOME STRING')
        self.assertEquals(testModel.speciesDescription , 'SOME STRING')
        self.assertEquals(testModel.sumAtRisk , 0)
        self.assertEquals(testModel.sumCases , 0)
        self.assertEquals(testModel.sumDeaths , 0)
        self.assertEquals(testModel.sumDestroyed , 0)
        self.assertEquals(testModel.sumSlaughtered , 0)
        self.assertEquals(testModel.humansGenderDesc , 'SOME STRING')
        self.assertEquals(testModel.humansAge , 0)
        self.assertEquals(testModel.humansAffected , 0)
        self.assertEquals(testModel.humansDeaths , 0)
        self.assertIsNone(testModel.geom )

    def test_EmpresDomesticWildHuman_custom_values(self):
        ''' create a model object and assert the attributes '''

        testModel = EmpresDomesticWildHuman( source = 'Test Source',
                                            latitude = 55.55,
                                            longitude = 30.30,
                                            region = 'North Pole',
                                            country = 'Greenland',
                                            admin1 = 'Santa',
                                            localityName = 'Kingdom',
                                            localityQuality = 'Awesome',
                                            observationDate = '10-10-2000',
                                            reportingDate = '25-12-2000',
                                            reportingYear= '2000',
                                            serotypes= 'H5N1',
                                            birdType= 'Domestic',
                                            speciesDescription = 'Magical',
                                            sumAtRisk = 2000,
                                            sumCases = 1000,
                                            sumDeaths = 1,
                                            sumDestroyed = 2,
                                            sumSlaughtered = 0,
                                            humansGenderDesc = 'Elf',
                                            humansAge = 200,
                                            humansAffected = 5,
                                            humansDeaths = 0,
                                            geom = None )


        self.assertEquals(testModel.source , 'Test Source')
        self.assertEquals(testModel.latitude , 55.55 )
        self.assertEquals(testModel.longitude , 30.30 )
        self.assertEquals(testModel.region , 'North Pole')
        self.assertEquals(testModel.country , 'Greenland')
        self.assertEquals(testModel.admin1 , 'Santa')
        self.assertEquals(testModel.localityName , 'Kingdom')
        self.assertEquals(testModel.localityQuality , 'Awesome')
        self.assertEquals(testModel.observationDate , '10-10-2000')
        self.assertEquals(testModel.reportingDate , '25-12-2000')
        self.assertEquals(testModel.reportingYear , '2000')
        self.assertEquals(testModel.serotypes , 'H5N1')
        self.assertEquals(testModel.birdType , 'Domestic')
        self.assertEquals(testModel.speciesDescription , 'Magical')
        self.assertEquals(testModel.sumAtRisk , 2000)
        self.assertEquals(testModel.sumCases , 1000)
        self.assertEquals(testModel.sumDeaths , 1)
        self.assertEquals(testModel.sumDestroyed , 2)
        self.assertEquals(testModel.sumSlaughtered , 0)
        self.assertEquals(testModel.humansGenderDesc , 'Elf')
        self.assertEquals(testModel.humansAge , 200)
        self.assertEquals(testModel.humansAffected , 5)
        self.assertEquals(testModel.humansDeaths , 0)
        self.assertIsNone(testModel.geom )


