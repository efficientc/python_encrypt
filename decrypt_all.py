__author__ = 'Chase Schwab'
# this is a script that will decrypt a message back into the original string enter before it was passed through encryptall.py
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;?@[\\]^_`{|}~
# 56789abcdefghij01234klmnopqwxyzABCDErstuvFGHI$PQR./:;?@[STUVWXYZ!"#%JKLMNO&\'()*+,-\\]^_`{|}
# ~defg 56789ab_`{|}chij01234klmno()*+,-pqwxyzABCDErstuvFGHI$PQR./:;?@[STUVWXYZ!"#%JKLMNO&\'\\]^
import string

# create list of all characters to use:
full_list = []
full_list_string = '~defg 56789ab_`{|}chij01234klmno()*+,-pqwxyzABCDErstuvFGHI$PQR./:;?@[STUVWXYZ!"#%JKLMNO&\'\\]^'
for char in full_list_string:
    full_list.append(char)

# ========================================================================================================
# define the decryption function
def decrypt(message):
    # this array will hold the index number of all string chars and then be converted to new index numbers
    encrypted_list = []
    converted_chars = []
    decrypted_letters = []
    # ----------------------------------------------------------------------------------------------------
    # assign values to letters/char index
    values = dict()
    for index, letter in enumerate(full_list):
        values[letter] = index + 1

    # assign letters to values
    letter_list = dict()
    for index, letter in enumerate(full_list):
        letter_list[index + 1] = letter

    # ----------------------------------------------------------------------------------------------------
    # concatenates the encrypted string back into a list
    for i in message:
        encrypted_list.append(i)

    # ----------------------------------------------------------------------------------------------------
    # assign values to letters
    for i in encrypted_list:
            converted_chars.append(values[i])

    # ----------------------------------------------------------------------------------------------------
    # assign the correct numeric value to each list item
    for n, i in enumerate(converted_chars):
        # for those below 45, add 45
        if int(i) < 46:
            converted_chars[n] = int(i) + 46
        else:
            # subtract 45
            converted_chars[n] = int(i) - 46

    # ----------------------------------------------------------------------------------------------------
    # assign letters to values
    for i in converted_chars:
        # add alpha char to array
        decrypted_letters.append(letter_list[i])

        # print(encrypted_list)
        # print(converted_chars)
        # print(decrypted_letters)

    # function that concatenates a list into a string
    def listtostring(list):
        string = ''
        for i in list:
            string += i
        return string

    decrypted_msg = listtostring(decrypted_letters)
    print('The decrypted message is: ' + decrypted_msg)

# ========================================================================================================

# prompt user for message to decrypt
decrypt(input('Enter an encrypted message to decrypt: '))
