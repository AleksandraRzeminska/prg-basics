#In one of the online stores, a 25% discount is charged 
# for each product purchased over two. 
# Write a program that calculates the amount to be paid. 
# Read the number of purchased products and the product price 
# from the keyboard.

ilość=int(input("Number of products purchased: "))
cena=int(input("Product price: "))

if ilość <= 2:
    print(f"No discount! Price to pay {ilość*cena}")
else:
    zapłata = (2*cena)+((ilość-2)*40*0.75)
    print(f"IS DISCOUNT\nAmount to pay: {zapłata}")