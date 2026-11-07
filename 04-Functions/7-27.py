###
#Products are marked with a special code 
# consisting of 3 digits and afourth control digit. 
# The forth digit is determined by calculating the 
# remainder of dividing the sum of the first three 
# digits by 7. Define a function f(product_code) 
# that returns True 
# if the product code is correct or False otherwise

def f(product_code):
    pierwsza=int(product_code[0])
    druga=int(product_code[1])
    trzecia=int(product_code[2])
    czwarta=int(product_code[3])
    if czwarta == (pierwsza+druga+trzecia)%7:
        return True
    else:
        return False


if __name__ == "__main__":
    print(f("1082")) 
    print(f("2035"))
    print(f("1114")) 
    print(f("7071")) 