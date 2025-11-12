###
# a program that checks what number was entered from the keyboard 
# and prints one of the messages: that number is positive, negatieve or 0

number = int(input('Enter the nmber: '))

if number > 0:
    print(f'Number {number} is positive')
elif number == 0:
    print('Number is 0')
elif number <0:
    print(f'Number {number} is negative')

