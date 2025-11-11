###
# program that prints the number of dice rolled
# the value True if the number rolled is 1 or 6

import random 

dice_roll = random.randint(1,6)
print(f'Dice number: {dice_roll}')

special_number = dice_roll==1 or dice_roll==6
print(f'Special number (1 or 6): {special_number}')