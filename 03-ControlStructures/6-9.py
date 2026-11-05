# Most female names in Polish end with the letter "a".
# Write a program that prints the name entered from 
# the keyboard, provided it is a female name. Sample result:
# Enter name: Anna
# Anna -- Polish female name

imie=input('Podaj imie: ')
if imie[-1]=="a":
    print(f'{imie} -- Polish female name')
else:
    print("It's not polish female name")