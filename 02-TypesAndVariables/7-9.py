###
# Write a program that prints the number of dice rolled 
# and the value True if the number rolled is 1 or 6.

import random

rzut_kostką = random.randint(1,6)
specjalna_liczba = rzut_kostką == 1 or rzut_kostką == 6
print(f'Dice rolled: {rzut_kostką}\nSpecial number (1 or 6): {specjalna_liczba}')
