from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse

client = Client()

class GetPicoPlacaPredictorTest(TestCase):
    """ Test module for GET predictor request """

    def test_get_can_be_on_road_request(self):
        url = reverse('predictor', kwargs={'licenseplate': 'ABC1234','date': '2020-03-03','time': '12:30:00'})
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data, {'licensePlate': 'ABC1234', 'date': '2020-03-03', 'time': '12:30:00', 'prediction': 'Can be on the road'})

    def test_get_cannot_be_on_road_request(self):
        url = reverse('predictor', kwargs={'licenseplate': 'ABC1234','date': '2020-03-03','time': '07:30:00'})
        response = client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data, {'licensePlate': 'ABC1234', 'date': '2020-03-03', 'time': '07:30:00', 'prediction': 'Can not be on the road'})
