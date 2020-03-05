from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

startTimeAM = "07:00:00"
endTimeAM = "09:30:00"
startTimePM = "16:00:00"
endTimePM = "19:30:00"

weekDays =["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

# Create your views here.
class PicoPlacaPredictorView(APIView):
    def predict_pico_placa(self, licenseplate, date, time, day):
        #Last digit from a license plate
        lastPlateDigit = get_last_digit_licenseplate(licenseplate)
        response = isAllowedToBeOnRoad(time, startTimeAM, endTimeAM, startTimePM, endTimePM, lastPlateDigit, day)

        return response

    def get(self, request, licenseplate, date, time, day):
        try:
            response = self.predict_pico_placa(licenseplate, date, time, day)
            response_body = {'response': response}
            return Response(response_body, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

#Get last digit from a license plate
def get_last_digit_licenseplate(str):
    last_digit = int(str[-1])
    return last_digit

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
    picoPlacaDays.append(isAllowedToBeOnRoadAccordingDay(lastPlateDigit, 1, 2, currentDay, weekDays[0], timeBetweenTimes))
    picoPlacaDays.append(isAllowedToBeOnRoadAccordingDay(lastPlateDigit, 3, 4, currentDay, weekDays[1], timeBetweenTimes))
    picoPlacaDays.append(isAllowedToBeOnRoadAccordingDay(lastPlateDigit, 5, 6, currentDay, weekDays[2], timeBetweenTimes))
    picoPlacaDays.append(isAllowedToBeOnRoadAccordingDay(lastPlateDigit, 7, 8, currentDay, weekDays[3], timeBetweenTimes))
    picoPlacaDays.append(isAllowedToBeOnRoadAccordingDay(lastPlateDigit, 9, 0, currentDay, weekDays[4], timeBetweenTimes))


    if all(item == True for item in picoPlacaDays):
        response = "can be on the road"
    else:
        response = "cannot be on the road"
    return response