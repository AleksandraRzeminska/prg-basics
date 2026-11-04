###
#Write a program that reads an integer number from the keyboard 
# and prints that value as a binary and hexadecimal number. To convert a decimal number to binary or hexadecimal value, use the available Python functions.

liczba = int(input('Podaj liczbe w systemie dziesietnym: '))
dwujkowy = bin(liczba)
szestanstkowy = hex(liczba)

print(f'Liczba {liczba} w systemie dwójkowym to: {dwujkowy} a w szestnastkowym to {szestanstkowy}')