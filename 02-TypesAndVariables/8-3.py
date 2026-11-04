###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
total_inches = int(cm/2.54)
feet = total_inches//12
inches = total_inches%12
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')