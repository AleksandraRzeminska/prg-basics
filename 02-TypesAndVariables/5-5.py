###
# The price of the product on the price tag is given before and after the discount is applied. 
# Write a program that allows you to enter the product price and discount. 
# Print the product price, discount, discounted product price, and the difference between the product price before and after the discount. 
# Print all prices with two decimal places.

kwota = float(input("Podaj kwotę: "))
zniżka = int(input("Podaj zniżke w %: "))
zniżka_po_przecinku = (100-zniżka)/100
cena_ze_zniżką = round(kwota*zniżka_po_przecinku,2)
różnica = round(kwota-cena_ze_zniżką,2)

print(f'Enter price: {kwota} \nEnter discount %: {zniżka}\nPrice with discount: {cena_ze_zniżką}\nReduction: {różnica}')