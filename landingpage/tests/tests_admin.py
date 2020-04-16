from django.test import SimpleTestCase
from landingpage.admin import  EmpresTwoYearOutbreakDataAdmin
from landingpage.models import EmpresTwoYearOutbreakData
from mock import Mock, patch
import pandas
import psycopg2
import pandas.io.sql as psql

# This class tests database queries and retrievals and ensures
# that retrieved data returns the correct query.

class IntegrationTests( SimpleTestCase ):
    allow_database_queries= True

    def setUp(self):
        # Create test data for EmpresTwoYearOutbreakData model
        self.data = EmpresTwoYearOutbreakData.objects.create(
                                                                disease= '',
                                                                serotypes='H5N1',
                                                                speciesDescription= 'wild',
                                                                country= 'United Kingdom',
                                                                sumCases= 2000,
                                                                sumDeaths= 100,
                                                                geom = None
                                                            )

    # Connect to the test database "testDB"
    def test_admin(self ):

        conn = psycopg2.connect(database="testDB")
        cur = conn.cursor()

        testDf = psql.read_sql("Select * from landingpage_emprestwoyearoutbreakdata", conn)

        resultDict = testDf.to_dict()

        print ( testDf.columns )
        print (testDf.to_dict())

        expectedResult = {'id': {0: 1},
                          'disease': {0: ''},
                          'geom': {0: None},
                          'serotypes': {0: 'H5N1'},
                          'speciesDescription': {0: 'wild'},
                          'country': {0: 'United Kingdom'},
                          'sumCases': {0: 2000.0},
                          'sumDeaths': {0: 100.0}}
        # Assert that the data we queried and retrieved is the same
        for k in expectedResult:
            self.assertEqual ( expectedResult[k], resultDict[k] )
