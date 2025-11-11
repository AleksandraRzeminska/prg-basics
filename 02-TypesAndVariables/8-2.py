###
# Calculation of circle area and circumference 
#

# determine radius and PI values
import math
pi_number= round(math.pi, 2) # zaokrąglenie do dówch miejs po przecinku
r = int(input('Enter radius: '))
# calculate area 
area= pi_number*(r**2)
# calculate circumference 
circumference= 2*pi_number*r
# print results
print(f'For r={r}, the area of circle is: {area} and circumrefence of circle is: {circumference}')