# A program that calculates VAT form amount 
#
amonunt_string = input('Enter your amount: ')
amount =float(amonunt_string)
VAT = (0.23*amount)
two_decimal_places = round(VAT, 2) #zaokrąglanie liczby do dwóch miejsc po przecinku
print(f'The VAT in your amount is {two_decimal_places}')