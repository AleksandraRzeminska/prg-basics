###
#Define a function f(number) that returns 
# the sum of repeated digits in a number.

def f(number):
    number=str(number)
    suma=0
    for digit in set(number):
        count = number.count(digit)
        if count > 1:
            suma += int(digit) * count
    return suma

if __name__ == '__main__':
    print(f(1027))
    print(f(230335))
    print(f(513553007))