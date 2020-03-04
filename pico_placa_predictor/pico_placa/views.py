from django.shortcuts import render
from django.utils import timezone
import pytz
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class PicoPlacaPredictorView(APIView):
    def predict_pico_placa(self, licenseplate, datetime):

        #Last digit from a license plate
        lastDigit = get_last_digit_licenseplate(licenseplate)

        #currentDate = convert_to_currentTime(datetime)

        return lastDigit

    def get(self, request, licenseplate, datetime):
        try:
            response = self.predict_pico_placa(licenseplate, datetime)
            response_body = {'response': response}
            return Response(response_body, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#Get last digit from a license plate
def get_last_digit_licenseplate(str):
    last_digit = int(str[-1])
    return last_digit

def convert_to_currentTime(str):
    fmt = "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'"
    fmt1 = '%d/%m/%Y %H:%M'
    utc = str.replace(tzinfo=pytz.UTC)
    localtz = utc.astimezone(timezone.get_current_timezone())
    return localtz.strftime(fmt)