###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math
a = input('Enter first side: ')
b = input('Enter second side: ')
c = input('Enter third side: ')
def triangle_area(a,b,c):
    s = 0.5*(a+b+c)
    result= math.sqrt((s-a)*(s-b)*(s-c))
    return result

print(f'The area of ​​a triangle with sides {a}, {b}, {c} is: {triangle_area} ',)
