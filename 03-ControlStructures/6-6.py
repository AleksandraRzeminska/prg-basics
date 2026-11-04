###
#The parking meter calculates the parking fee based on the number of hours 
# the car was parked according to the following rules:
#1-2 hours: 5 PLN
#3-6 hours: 15 PLN
#Over 6 hours: 20 PLN
#Write a program that asks for the number of hours of parking, 
# then calculates and prints the correct fee.

czas = int(input("Ile godzin wynosi twój czas parkowania? "))

if czas > 6:
    print('Do zapłaty 20 PLN')
elif czas <=6 and czas >=3:
    print('Do zapłaty 15 PLN')
elif czas < 2 and czas >=1:
    print("Do zapłaty 5 PLN")