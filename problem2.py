"""
Name:           problem2.py
Description:    The program will use a while loop to       determind the average distance Tony travels and the days it took to surpass 100

Author:         Lauren M

Created:     03/03/2021
"""
"***** Welcome to the DoorDash Distance Tracker *****"

print = "DISTANCE TRACKER"

#set variables
daily_amount = 0
distance = 0
number_days = 0


#The program will use a while loop to ask the user for the distance travelled for the day
while distance != 100:
  distance_day = float(input("Enter the distance travelled for the day: "))
  distance = distance + distance_day
  number_days = number_days + 1


#The program will output the number of days it took to pass 100 km and the average distance driven per day
average = distance // number_days

print = "it took " + str(number_days) + " days to surpass 100km driven."
print = "the average distance per day is" + str(average) + "km"


