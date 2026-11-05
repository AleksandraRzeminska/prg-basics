###
# Write a program that calculates a dog's age 
# in dog's years. For the first two years, 
# a dog's life is equal to 10.5 human years. 
# After that, each dog year is equal to 4 human years.
###

wiek_ludzki=int(input("Enter the dog's age in human years: "))
if wiek_ludzki <= 2:
    wiek_psi=wiek_ludzki*10.5
elif wiek_ludzki >2:
    wiek_psi=(2*10.5)+((wiek_ludzki-2)*4)
print(f"The dog's age in dog's years is {wiek_psi} years" )
