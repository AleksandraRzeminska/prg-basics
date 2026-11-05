x=12
r=""

while x >0:
    y=x%2
    x=x//2
    r+=str(y)

print(r[::-1])