from urllib import request

from landingpage.urls import urlpatterns
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from home.views import home
from landingpage.views import avian14to17data_dataset, empresdomesticwildhuman_dataset


class UrlToViewIntegrationTests(SimpleTestCase):
    ''' Integration test to check if the connection between the template and view is working correctly.
        Given a url name string, reverse match and resolve the url to the right view
    '''

    def test_home_url_to_view_mapping(self):
        ''' reverse match and resolve the view from the url string for homepage '''

        home_url = reverse('user_home')
        self.assertEquals(resolve(home_url).func, home)

    def test_avian_url_to_view_mapping(self):
        ''' reverse match and resolve the view from the url string for avian14to17data '''

        avian14to17data_url = reverse('avian14to17data')
        self.assertEquals(resolve(avian14to17data_url).func, avian14to17data_dataset )

    def test_empres_url_to_view_mapping(self):
        ''' reverse match and resolve the view from the url string for main dataset '''

        empresdomesticwildhuman_dataset_url = reverse('empresdomesticwildhuman')
        self.assertEquals(resolve(empresdomesticwildhuman_dataset_url).func, empresdomesticwildhuman_dataset)

class UrlModuleTests( SimpleTestCase ):

    def test_url_names(self):
        ''' test values returned by url patterns list '''
        self.assertEqual( len(urlpatterns), 3 )

        url1, url2, url3 = urlpatterns

        self.assertEqual( url1.name, 'user_home' )
        self.assertEqual( url2.name, 'avian14to17data' )
        self.assertEqual( url3.name, 'empresdomesticwildhuman' )



