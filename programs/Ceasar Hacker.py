""" Ceser Cipher Hacker by Isaack Joshua, isaackjoshua23@gmail.com
    This program hacks messages encrypted with the ceaser cipher by doing 
    a brute fore attack against every possible key."""

print('Caesar Cipher Hacker by Isaack Joshua, isaackjoshua23@gmail.com')

#Let the user specify the message to hack:
print('Enter the encrypted Caeser cipher message to hack.')
message = input('> ')

#Every possible symbol that can be encrypted/Decrypted:
# (This must match the SYMBOLS used when encrypting the message.)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)): #Loop through every possible key.
    translated = ''

    #Decrypt each symbol in the message:
    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)  # Get the number of the symbol
            num = num - key # Decrypt the number.

            #Handle the Wrap arounf if num is less than 0:
            if num < 0:
                num = num + len(SYMBOLS)

            #Add decrypted number's symbol to translated:
            translated = translated + SYMBOLS[num]
        else:
            # Just add the symbol without decrypting:
            translated = translated + symbol
    #Display the Key being tested, along with its decrypted text:
    print('Key #{}: {}'.format(key, translated))