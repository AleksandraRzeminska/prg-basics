###
# Sums numbers entered by user
#
total_sum = 0
ilość_liczb = 0
while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    ilość_liczb += 1
mean = total_sum/ilość_liczb
print(f"The total sum of the numbers is: {total_sum} and mean is: {mean}")
