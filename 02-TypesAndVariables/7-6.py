###
#The speed of vehicles on a highway in Poland must be between 40 and 140 km/h. 
# Write a program that checks whether the vehicle speed entered from the keyboard is correct.

predkosc = int(input("Enter vehicle speed: "))
dozwolone = predkosc >= 40 and predkosc <= 140
print(f'Speed is valid: {dozwolone}')