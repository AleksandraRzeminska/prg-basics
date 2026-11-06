###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    całkowita = abs(any_number)
    string = str(całkowita)
    i=0
    suma=0
    while i < len(string):
        liczba = int(string[i])
        i+=1
        suma += liczba
    
    return suma

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')