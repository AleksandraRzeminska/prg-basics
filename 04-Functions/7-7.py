###
#The binary numerical system uses two symbols to represent a number: 
#0 and 1. Define a function f(binary_number) 
#that returns True if the given string of digits is
#a valid binary number, or False otherwise.

def f(binary_number):
    dozwolone = {'0','1'}
    return set(binary_number).issubset(dozwolone)

if __name__ == "__main__":
    print(f("101101"))
    print(f("1311a10100")) 