###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b = input('b=')
c = input('c=')
side_a = int(a)
side_b= int(b)
side_c= int(c)

volume = (a*b)*c
suface_area = 2*(a*b + a*c + b*c)

print(f'The volume of a cuboid with sides {side_a}, {side_b} and {side_c} is {volume}')
print(f'The surface area of a cuboid is {suface_area}')
