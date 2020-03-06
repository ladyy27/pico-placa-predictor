from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .services import service
from .serializers import PredictionModelSerializer
from .models import PredictionModel

# Create your views here.
# A class-based-view to control the requests and get a Pico&Placa prediction
class PicoPlacaPredictorView(APIView):

    def predict_pico_placa(self, licenseplate, date, time):
        try:
            # Last digit from a license plate
            lastPlateDigit = service.get_last_digit_licenseplate(licenseplate)

            # Current day from Date
            currentDay =  service.get_day_from_date(date)

            # Get prediction for a car
            response = service.isAllowedToBeOnRoad(time, lastPlateDigit, currentDay)

            #Serialize response
            prediction = PredictionModel(licensePlate=licenseplate, date=date, time=time, prediction=response)
            serializer = PredictionModelSerializer(prediction)
            print(serializer.data)
            return serializer.data
        except:
            raise Http404


    def get(self, request, licenseplate, date, time):
        try:
            response = self.predict_pico_placa(licenseplate, date, time)
            return Response(response, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)