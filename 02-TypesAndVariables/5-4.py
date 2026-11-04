###
# 23% VAT was paid from an amount.
# Write a program that reads an amount from the keyboard. 
# Then, it calculates and prints both the amount and its VAT. 
# Apply formatting with two decimal places.

kwota = float(input("Podaj kwotę "))
vat = round(0.23*kwota, 2)
print(f'Kwota: {kwota} \nVAT 23%: {vat}')