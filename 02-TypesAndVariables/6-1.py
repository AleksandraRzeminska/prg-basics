###
# A program that calculates the number of characters
# of your name, surname and full name
#
name = 'Aleksandra'   # replace Anna with your name
surname = 'Rzemińska' # replace May with your surname
characters_in_name = len(name)
character_in_full_name = len(name + surname)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} characters')
print(f'Your full name has {character_in_full_name} characters') # with a space between name and surname