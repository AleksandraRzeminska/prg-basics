###
#Define the function f(number1,number2,number3),
#  which returns the difference between 
# the largest and smallest numbers.

def f(number1,number2,number3):
    najmniejsza=min(number1,number2,number3)
    najwieksza=max(number1,number2,number3)
    różnica=najwieksza-najmniejsza
    return różnica


if __name__=="__main__":
    print(f(7,4,9))
    print(f(2,12,8))
