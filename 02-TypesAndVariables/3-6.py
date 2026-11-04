# program that calculates the distance to the horizon from 
# a height given in meters from the keyboard


import math

heigh = float(input("Enter the height of observer in meters: ")) # float pozwala na wprowadzenie liczb niecałkowitych
distance = 3.57*math.sqrt(heigh)

print("The distance to the horizon from the height=",heigh, "is ",distance)