kod=input("Enter EAN-13 article number: ")

if len(kod) == 13:
    print("Article number is correct")
    if kod[0:3] == "590":
        print("Article manufactured in Poland")