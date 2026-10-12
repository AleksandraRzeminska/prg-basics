
import math
obwod = int(input('Enter tree circumference in cm: '))
srednica = obwod/math.pi
sciac = srednica >= 50
print(f'Tree can be cut down: {sciac}')