###
#Each month of a calendar year can be expressed by 
# its name or by a number that indicates the position 
# of the month in year. In a separate module, define
# a function month(n) that returns a month name based on
# the month number (values from 1 to 12).

def month(n):
    n=str(n)
    if n == "1":
        return "Styczeń"
    elif n == "2":
        return "Luty"
    elif n == "3":
        return "Marzec"
    elif n == "4":
         return "Kwiecień"
    elif n == "5":
        return "Maj"
    elif n == "6":
        return "Czerwiec"
    elif n == "7":
        return "Lipiec"
    elif n == "8":
        return "Sierpień"
    elif n == "9":
        return "Wrzesień"
    elif n == "10":
        return "Padźniernik"
    elif n == "11":
        return "Listopad"
    elif n == "12":
        return "Grudzień"


if __name__ == "__main__":
    # This block will only execute when the script is run directly
    
    
    print(f"The name of month is: {month(9)}")