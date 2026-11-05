aktualna=140
poprzednia=200

redukcja= 100-((aktualna/poprzednia)*100)

if redukcja > 10:
    print(f'Buy the product!!\nProduct price reduced by {redukcja}')
else:
    print("Do not buy, the reduce is low")