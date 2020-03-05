from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
from django.http import Http404

startTimeAM = "07:00:00"
endTimeAM = "09:30:00"
startTimePM = "16:00:00"
endTimePM = "19:30:00"


# Create your views here.
class PicoPlacaPredictorView(APIView):

    def predict_pico_placa(self, licenseplate, date, time):
        try:
            # Last digit from a license plate
            currentDay = get_day_from_date(date)
            lastPlateDigit = get_last_digit_licenseplate(licenseplate)
            response = isAllowedToBeOnRoad(time, startTimeAM, endTimeAM, startTimePM, endTimePM, lastPlateDigit,currentDay)
            return response
        except:
            raise Http404


    def get(self, request, licenseplate, date, time):
        try:
            response = self.predict_pico_placa(licenseplate, date, time)
            response_body = {'response': response}
            return Response(response_body, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

"""
class PicoPlacaPredictorView(APIView):

    def predict_pico_placa(self, licenseplate, date, time):
        try:
            # Last digit from a license plate
            currentDay = get_day_from_date(date)
            lastPlateDigit = get_last_digit_licenseplate(licenseplate)
            response = isAllowedToBeOnRoad(time, startTimeAM, endTimeAM, startTimePM, endTimePM, lastPlateDigit,currentDay)
            return response
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, licenseplate, date, time):
        response = self.predict_pico_placa(licenseplate, date, time)
        response_body = {'response': response}
        return Response(response_body, status=status.HTTP_200_OK)
"""

#Get last digit from a license plate
def get_last_digit_licenseplate(str):
    last_digit = int(str[-1])
    return last_digit

#Get day of week according to a date
def get_day_from_date(str):
    year, month, day = (int(x) for x in str.split('-'))
    dayOfWeek = datetime.date(year, month, day).weekday()
    return dayOfWeek

#Determine if current time is between a range of times
def time_is_between(time, time_range):
    if time_range[1] < time_range[0]:
        return time >= time_range[0] or time <= time_range[1]
    return time_range[0] <= time <= time_range[1]

#Determine if a car can be on the road according ranges of times
def isAllowedToBeOnRoadAccordingTimes(time,range1, range2, range3, range4):
    if time_is_between(time, (range1, range2)) or time_is_between(time, (range3, range4)):
        return True
    else:
        return False

#Determine if a car can be on the road according the day of week
def isAllowedToBeOnRoadAccordingDay(lastPlateDigit, plateRangeStart, plateRangeEnd, currentDay, dayOfweek, timeBetweenTimes):
    if lastPlateDigit == plateRangeStart or lastPlateDigit == plateRangeEnd:
        if currentDay == dayOfweek:
            if timeBetweenTimes:
                canBeOnRoad = False
            else:
                canBeOnRoad = True
        else:
            canBeOnRoad = True
    else:
        canBeOnRoad = True
    return canBeOnRoad


#Determine if a car be on the road according Last plate digit, Day of Week and Time
def isAllowedToBeOnRoad(currentTime,range1, range2, range3, range4, lastPlateDigit, currentDay):
    timeBetweenTimes = isAllowedToBeOnRoadAccordingTimes(currentTime,range1, range2, range3, range4)
    picoPlacaDays= []
    picoPlacaDays.append(isAllowedToBeOnRoadAccordingDay(lastPlateDigit, 1, 2, currentDay, 0, timeBetweenTimes))
    picoPlacaDays.append(isAllowedToBeOnRoadAccordingDay(lastPlateDigit, 3, 4, currentDay, 1, timeBetweenTimes))
    picoPlacaDays.append(isAllowedToBeOnRoadAccordingDay(lastPlateDigit, 5, 6, currentDay, 2, timeBetweenTimes))
    picoPlacaDays.append(isAllowedToBeOnRoadAccordingDay(lastPlateDigit, 7, 8, currentDay, 3, timeBetweenTimes))
    picoPlacaDays.append(isAllowedToBeOnRoadAccordingDay(lastPlateDigit, 9, 0, currentDay, 4, timeBetweenTimes))


    if all(item == True for item in picoPlacaDays):
        response = "Can be on the road"
    else:
        response = "Cannot be on the road"
    return response