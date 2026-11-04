###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    char_code = ord(char)
    # add one to the character's code
    zmiana = char_code + 1 
    # replace new character code with its
    # corresponding character (use chr())
    nowa = chr(zmiana)
    # add encrypted character to encrypted text
    encrypted_text = encrypted_text + nowa

print(plain_text)
print(encrypted_text)