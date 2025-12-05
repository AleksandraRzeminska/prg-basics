###Displays name
#Displays hobby
#Displays the entire contents of the dictionary
#Changes surname to 'Nowak'
#Changes person's marriage status
#Adds gender: 'male'
#Adds a new hobby: 'bicycle'
#Adds work phone to existing phones: '313131444'
#Displays the entire contents of the dictionary (iterate over dictionary items)


person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

# Display name
print(person["name"])

# Display hobby
print(person["hobby"])

# Display entire dictionary
print(person)

# Change surname to 'Nowak'
person["surname"] = "Nowak"
print(person['surname'])

# Change marriage status
person["married"] = not person["married"]
print(person["married"])

# Add gender: 'male'
person["gender"] = "male"
print(person["gender"])

# Add new hobby: 'bicycle'
person["hobby"].append("bicycle")
print(person["hobby"])

# Add work phone
person["phone"]["work"] = "313131444"
print(person["phone"])

print("\n--- Updated dictionary ---")
for key, value in person.items():
    print(f"{key}: {value}")