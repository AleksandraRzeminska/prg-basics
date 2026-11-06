###
#Define a function f(n) that returns a string of n asterisks,
#separated by a slash sign

def f(n):
    if n <= 0:
        return ""
    
    wynik = ""
    i = 1
    while i <= n:
        wynik += "*"
        if i < n:
            wynik += "/"
            
        i += 1  
        
    return wynik   
          
    

if __name__ == '__main__':
    print(f(4))
    print(f(1))
    print(f(0))
    print(f(9))