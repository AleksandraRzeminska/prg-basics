###
# Dstance to the horizon from a height
#
import math
height = input("Enter height of the observer in meters: ")
height = int(height)
distance = (3.57*(math.sqrt(height)))
print("The distance to the horizon in kilometers is: ", distance)