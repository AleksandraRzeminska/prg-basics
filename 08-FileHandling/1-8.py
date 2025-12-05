
def read_from_file(name):
    with open(name, 'r') as file:
        content = file.read()
    return content


text = read_from_file('pets.txt')
print(text)

slowa = text.split()

ilosc_slow = len(slowa)
print("Liczba słów w tekście:", ilosc_slow)
