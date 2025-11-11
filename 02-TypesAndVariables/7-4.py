## program który mówi czy można ściać drzewo
# na podstawie jego obwodu wprowadzonego z klawiatury
# jeżeli drzewo ma średnicę mniejszą niż 50 cm nie wolno go ściąć
# Tree 1: 160 Tree 2: 90 Tree 3: 230 Tree 4: 120

import math
obwód = int(input('Podaj obwód drzewa w cm: '))
średnica = obwód/math.pi
ściąć = średnica >= 50
print(f'Drzewo można ściać: {ściąć}')