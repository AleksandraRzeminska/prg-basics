###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:

    if char== ' ': ##omijamy spację
        continue
    # read the character's code (use ord())
    char_number = ord(char)
    # add one to the character's code
    char_number =char_number +1
    # replace new character code with its
    # corresponding character (use chr())
    new_char = chr(char_number)
    # add encrypted character to encrypted text
    encrypted_text = encrypted_text + new_char
    

print(plain_text)
print(encrypted_text)