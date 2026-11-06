#Define the function f(n), 
# which returns numbers from 1 to n as a string

def f(n):
    results=""
    i=1
    while i <= n:
        results += str(i)
        i+=1
    return results    
    
   

if __name__ == '__main__':
    print(f(4))
    print(f(9))
    print(f(11))
