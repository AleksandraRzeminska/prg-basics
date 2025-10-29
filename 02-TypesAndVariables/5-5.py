# Program that calculates a discount 
# print the product price, discount, 
# print difference between the product price before and after the discount

price_string= input("Enter the product price: ")
discount_string= input("Enter the discount in % ")
price= float(price_string)
discount= float(discount_string)
price_after_discount= 0.01*(100- discount)*price 
price_after_discount_two_places= round(price_after_discount, 2)
reduction= (price - price_after_discount)
reduction_two_places= round(reduction, 2)
print(f"The product price was {price}, the discount is {discount}%")
print(f"Now the product price is {price_after_discount_two_places} and the reduction is {reduction_two_places}")