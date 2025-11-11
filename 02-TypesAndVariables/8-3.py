###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#

import math
# Enter temperature in Celsius form the keyboard
celsius = int(input('Enter the cemperature in degrees Celsius: '))
# Convert the temperature in Celsius to Kelvin
kelvin = celsius+ 273.15 
# Convert the temperature in Celsius to Fahrenheit
fahrenheit = (celsius*1.8)+32 
# Print the results
print(f'The temperature in degrees Celsius is: {celsius}, in Kelvin is {kelvin} and in Fahrenheit is {fahrenheit}')