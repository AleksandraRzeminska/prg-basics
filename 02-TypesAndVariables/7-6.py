###
# The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. 
# Write a program that checks whether the vehicle speed entered from the keyboard is correct.

speed = int(input('Enter vehicle speed in km/h: '))
valid_speed = speed <=140 and speed >=40
print(f'Speed is valid: {valid_speed}')