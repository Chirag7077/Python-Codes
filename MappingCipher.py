def encrypt(table, words):
    cipher = ''
    for ch in words:
        if str.isalpha(ch):
            ch = getOpponent(table, ch)
        cipher += ch
    return cipher


def decrypt(table, words):
    return encrypt(table, words)

def toLower(ch, flag):
    if flag:
        return ch.lower()
    else:
        return ch

def getPosition(table, ch):
    row = -1
    
    if ch in table[0]:
        row = 0
    elif ch in table[1]:
        row = 1

    if row != -1:
        return (row, table[row].index(ch))
    else:
        return (None, None);


def getOpponent(table, ch):
    flag = False
    
    if ch.islower():
        flag = True

    row, col = getPosition(table, ch.upper())

    if row == 1:
        return toLower(table[0][col], flag)
    elif row == 0:
        return toLower(table[1][col], flag)
    else:
        return ch


if __name__ == '__main__':
    table = [
        [ 'K', 'B', 'J', 'H', 'O', 'E', 'S', 'N', 'W', 'Y', 'C', 'V', 'I' ],
        [ 'A', 'P', 'M', 'R', 'Z', 'Q', 'G', 'F', 'X', 'D', 'U', 'L', 'T' ] ]

    text = input("Enter the Plain Text: ")
    ciphertext = encrypt(table, text)
    print("Cipher Text: "+str(ciphertext))
    
    decryptText = input("Enter the Cipher Text: ")
    print(decrypt(table, decryptText))
