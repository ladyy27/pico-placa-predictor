import datetime

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
def isAllowedToBeOnRoadAccordingTimes(time, range1, range2, range3, range4):
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
def isAllowedToBeOnRoad(currentTime, lastPlateDigit, currentDay):

    startTimeAM = "07:00:00"
    endTimeAM = "09:30:00"
    startTimePM = "16:00:00"
    endTimePM = "19:30:00"

    timeBetweenTimes = isAllowedToBeOnRoadAccordingTimes(currentTime, startTimeAM, endTimeAM, startTimePM, endTimePM)
    picoPlacaDays= []
    picoPlacaDays.append(isAllowedToBeOnRoadAccordingDay(lastPlateDigit, 1, 2, currentDay, 0, timeBetweenTimes))
    picoPlacaDays.append(isAllowedToBeOnRoadAccordingDay(lastPlateDigit, 3, 4, currentDay, 1, timeBetweenTimes))
    picoPlacaDays.append(isAllowedToBeOnRoadAccordingDay(lastPlateDigit, 5, 6, currentDay, 2, timeBetweenTimes))
    picoPlacaDays.append(isAllowedToBeOnRoadAccordingDay(lastPlateDigit, 7, 8, currentDay, 3, timeBetweenTimes))
    picoPlacaDays.append(isAllowedToBeOnRoadAccordingDay(lastPlateDigit, 9, 0, currentDay, 4, timeBetweenTimes))


    if all(item == True for item in picoPlacaDays):
        response = "Can be on the road"
    else:
        response = "Can not be on the road"
    return response