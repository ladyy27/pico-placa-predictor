from django.test import TestCase
from ..services import service

class GetPicoPlacaPredictorTest(TestCase):
    """ Test bussines logic for predictor app"""
    def test_getPicoPlacaPrediction_correct(self):
        result = service.isAllowedToBeOnRoad("07:45:00", 1, 0)
        self.assertEqual(result, "Can not be on the road")

    def test_getPicoPlacaPrediction_incorrect(self):
        result = service.isAllowedToBeOnRoad("12:45:00", 1, 0)
        self.assertEqual(result, "Can be on the road")