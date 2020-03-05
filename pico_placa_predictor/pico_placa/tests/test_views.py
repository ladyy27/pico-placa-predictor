from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

client = Client()

class GetPicoPlacaPredictorTest(TestCase):
    """ Test module for GET predictor request """

    def setUp(self):
        return

    def test_get_can_be_on_road_request(self):
        url = reverse('predictor', kwargs={'licenseplate': 'ABC1234','date': '2020-03-03','time': '14:30:00'})
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, {'response': 'Can be on the road'})

    def test_get_cannot_be_on_road_request(self):
        url = reverse('predictor', kwargs={'licenseplate': 'ABC1234','date': '2020-03-03','time': '07:30:00'})
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data, {'response': 'Cannot be on the road'})

    def test_get_invalid_predictor_request(self):
        response = self.client.get('/predictor/ABCDEF4/2020-03-02/14:30:00/',format='json')
        #url = reverse('predictor', kwargs={'licenseplate': 'ABCDEF4', 'date': '2020-03-02', 'time': '14:30:00'})
        #response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(len(response.data), 0)