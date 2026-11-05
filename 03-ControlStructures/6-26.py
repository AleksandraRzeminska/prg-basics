x="0805"
i=1

while i<4:
    y=input("Podaj PIN do karty: ")
    if y!=x:
        print("Incorrect")
        i+=1
    else:
        print("Correct")
        break