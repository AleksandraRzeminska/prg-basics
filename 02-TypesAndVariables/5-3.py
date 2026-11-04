###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))

objętość = a*b*c
pole_powierzchni = 2*(a*b + a*c + b*c)

print(f'Objetośc dla prostopadłościonau o bokach a= {a} b= {b} c= {c} wysosi {objętość}, a pole powierzchni {pole_powierzchni}')