### program that reads an integer number from the keyboard 
# prints that value as a binary and hexadecimal number. 
# To convert a decimal number to binary or hexadecimal value, use the available Python functions.

decimal = int(input('Enter the number: '))
binary = bin(decimal)
hexadecimal = hex(decimal)

print(f'The {decimal} in binary is: {binary} and in hexadecimal is: {hexadecimal}')