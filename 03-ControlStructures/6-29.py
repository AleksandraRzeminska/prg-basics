N=50
i=2
while i<N:
    j=2
    Grzegorz=True
    while j <= i**0.5:
        #print(i, j)
        if i%j==0:
            Grzegorz=False
            break
        j+=1
    #print()
    if Grzegorz:
        print(i)
    i+=1

            
