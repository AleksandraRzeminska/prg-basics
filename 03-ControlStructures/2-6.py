###
#Write a program that checks what number was entered from the keyboard 
# and prints one of the messages below.

liczba=int(input('Podaj liczbę: '))

if liczba > 0:
    print(f'Number {liczba} is positive')
elif liczba < 0:
    print(f'Number {liczba} is negative')
elif liczba == 0:
    print(f'Number is 0')