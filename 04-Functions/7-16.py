###
#Define the function f(n), which returns the 
# n-th value of the Fibonacci sequence. 
# The sequence is defined as follows: 
# the first value of the sequence is 0, 
# the second value is 1. 
# Each subsequent value is the sum of the previous two.

def f(n):
    x=0
    y=1
    i=2
    while i < n:
        z=x+y
        x=y
        y=z
        i+=1
    return z

if __name__ == '__main__':
    print(f(5))
    print(f(9))