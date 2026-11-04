###
# Calculation of circle area and circumference 
#

# determine radius and PI values
import math 

# calculate area 
r = int(input('Podaj promień: '))
p = round(math.pi*(r**2),2)

# calculate circumference 
d = round(math.pi*2*r,2)

# print results
print(f'For r={r} the circumference is {d} and the area is: {p}')