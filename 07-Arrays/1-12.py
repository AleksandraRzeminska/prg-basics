categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]


drogie = expenses.index(max(expenses))
for item in categories:
    if categories.index(item)==drogie:
        print("The most expesive is", item)

