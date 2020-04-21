__author__ = 'EfficientC'
# this is a script that will encrypt all characters a message into an illegible string of characters
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;?@[\\]^_`{|}~
# 56789abcdefghij01234klmnopqwxyzABCDErstuvFGHI$PQR./:;?@[STUVWXYZ!"#%JKLMNO&\'()*+,-\\]^_`{|}
# ~defg 56789ab_`{|}chij01234klmno()*+,-pqwxyzABCDErstuvFGHI$PQR./:;?@[STUVWXYZ!"#%JKLMNO&\'\\]^
import string

# this array will hold the index number of all string chars and then be converted to new index numbers
msg_index_array = []
converted_chars = []

# ========================================================================================================
# define the encryption function
def encrypt(message):
    # create list of all characters to use:
    full_list = []
    full_list_string = '~defg 56789ab_`{|}chij01234klmno()*+,-pqwxyzABCDErstuvFGHI$PQR./:;?@[STUVWXYZ!"#%JKLMNO&\'\\]^'
    for char in full_list_string:
        full_list.append(char)

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
    # append an index number for each char in the message passed (only lowercase with spaces)
    for char in message:
        # add numeric value to new array
        msg_index_array.append(values[char])

    # ----------------------------------------------------------------------------------------------------
    # change new index array values for encryption process
    for n, i in enumerate(msg_index_array):
        # to prevent an index from going above 92, the index no. is subtracted by 46 to start at 1 again
        if i > 46:
            msg_index_array[n] = i - 46
        else:
            # each index increases by 46
            msg_index_array[n] = i + 46

    # ----------------------------------------------------------------------------------------------------
    # assign values to letters
    for n, i in enumerate(msg_index_array):
        # if i == 91:
        #     converted_chars.append('~')
        # else:
            converted_chars.append(letter_list[i])

# ----------------------------------------------------------------------------------------------------
    # function that concatenates a list into a string
    def listtostring(list):
        string = ''
        for i in list:
            string += i
        return string

    # create and print newly encrypted string
    cryptostring = listtostring(converted_chars)
    print('Here is your encrypted message: ' + cryptostring)

# prompt user for message to encrypt
encrypt(input('Type a message to encrypt: '))
