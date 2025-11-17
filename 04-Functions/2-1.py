###
# Program for testing built-in functions
#the largest number: 7,5,6,3,8,2
#the smallest number: 4,7,2,3,9,8
#length of the phrase: "computer science"
#letter read from the keyboard
#number representing the string "20303"
#binary string representing decimal number 304
#hexadecimal string representing decimal number 304
#integer representing the Unicode code of the € sign
#absolute value of -17
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter_read = input("Enter the number: ")
print('Your letter is: ', letter_read)

present_string = chr(20303)
print('The cone presents: ',present_string)

binary = bin(304)
print('The number 304 is: ',binary)

heximal = hex(204)
print('The number 304 is: ',heximal)

unicode = ord('€')
print('The € in unicode is: ',unicode)

absolute_value =abs(-17)
print('The absolute value of -17 is; ',absolute_value)
