from rest_framework import serializers
from .models import PredictionModel

class PredictionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PredictionModel
        fields = ('licensePlate', 'date', 'time', 'prediction')

    def setPredictionParams(self, licensePlate, date, time):
        prediction = PredictionModel (licensePlate=licensePlate, date=date, time=time)
        return prediction

    def setPredictionResult(self, response):
        result = PredictionModel (prediction=response)
