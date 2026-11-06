###
#Define the function f(x,y) that returns the 
#number of negative even numbers in the range <x,y>.

def f(x,y):
    i=0
    for cyfra in range(x, y+1):
        if cyfra <0:
            if cyfra%2 == 0:
                i +=1
    return i

if __name__ == '__main__':
    print(f(-7,8))
    print(f(-1,11))
    print(f(-12,9))
