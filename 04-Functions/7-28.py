###
#The sequence of digits contains the number of points
#rolled with a dice. Define a function f(dice) 
# that returns a number specifying 
#the number of dice rolled the most times in a row.

def f(dice):
    c1 = dice.count("1")
    c2 = dice.count("2")
    c3 = dice.count("3")
    c4 = dice.count("4")
    c5 = dice.count("5")
    c6 = dice.count("6")
    najwieksza=max(c1,c2,c3,c4,c5,c6)
    if najwieksza == c1:
        return 1
    elif najwieksza == c2:
        return 2
    elif najwieksza == c3:
        return 3
    elif najwieksza == c4:
        return 4
    elif najwieksza == c5:
        return 5
    elif najwieksza == c6:
        return 6


if __name__ == "__main__":
    print(f("5233165554211"))
    print(f("2133"))