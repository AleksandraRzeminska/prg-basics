###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter_form_k = input("Enter your letter: ")
print("Your letter: ", letter_form_k)

number = chr(int("20303"))
print(number)

binary = bin(304)
print(f'{binary}')

hexadecimal = hex(304)
print(f'304 in hexadecimal is: {hexadecimal}')

unicode = ord('€')
print(f"€ in Unicode: {unicode}")

absolute_value = abs(-17)
print(f'absolute value of -17 is : {absolute_value}')