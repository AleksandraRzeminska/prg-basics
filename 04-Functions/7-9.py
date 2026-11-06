###
#Create a function f(number, even) that computes 
# the sum of the digits of a number. 
# When the value of the even parameter is True, 
# the function returns the sum of the even digits. 
# When the value of the even parameter is False, 
# the function returns the sum of the odd digits.

def f(number, even):
    suma = 0
    number=str(number)
    if even:
        for char in number:
            if int(char)%2 == 0:
                suma += int(char)
    elif not even:
        for char in number:
            if int(char)%2 != 0:
                suma += int(char)
    return suma

if __name__=='__main__':
    print(f(3124,True))
    print(f(3124,False)) 
    print(f(20576,False)) 
    print(f(20576,True)) 
    print(f(13115,True))


