alphabet = 'abcdefghijklmnopqrstuvwxyz'
new_message = ''
message = input('Please enter the secret message: ')
key = input('Enter a secret numeric key between (1-26): ')
key = int(key)
for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        new_position = (position - key) % 26
        new_character = alphabet[new_position]
        new_message += new_character
    else:
        new_message += character
print('Your encrypted message is: ', new_message)
