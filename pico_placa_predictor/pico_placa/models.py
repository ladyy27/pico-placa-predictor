from django.db import models

# Create your models here.
class PredictionModel(models.Model):
    licensePlate = models.CharField(max_length=7)
    date = models.DateField()
    time = models.TimeField()
    prediction = models.CharField(max_length=200)