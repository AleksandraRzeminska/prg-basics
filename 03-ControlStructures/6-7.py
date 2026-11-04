###
#Write a program that asks the user 
# for their age and then checks which age group 
# they belong to:
#Child: under 13
#Teen: 13 to 19
#Adult: 20 to 64
#Senior: 65 or older






wiek = int(input("Podaj swój wiek: "))

if wiek < 13:
    print('Jesteś dzieckiem')
elif wiek <=19 and wiek >=13:
    print('Jesteś nastolatkiem')
elif wiek <= 64 and wiek >=20:
    print("Jesteś dorosłym")
elif wiek >= 65:
    print("Jesteś seniorem")