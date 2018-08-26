import random

def encrypt(table, words):
	cipher = ''
	for ch in words:
		if str.isalpha(ch):
			ch = getOpponent(table, ch)
		cipher += ch
	return cipher


def decrypt(table, words):
    return encrypt(table, words)

def encryptStageTwo(binaryString,ciphertext,randomInt):
	ciphertext = list(ciphertext)
	for alpha in ciphertext:
		cipherInt = ord(alpha)
		intermediateInt = cipherInt + randomInt
		finalInt = intermediateInt % 4
		binaryValue = format(finalInt,"b")
		if len(binaryValue) == 4:
			binaryString = binaryString + binaryValue
		else:
			while(len(binaryValue) < 4):
				binaryValue = '0'+ binaryValue
			binaryString = binaryString + binaryValue
	return binaryString
	
def decryptStageZero(decryptText,randomInt,stringValue):
	listText = [decryptText[k:k+4] for k in range(0,len(decryptText),4)]
	for numer in listText:
		print (numer)
		decimalValue = int(numer,2)
		intermediateDecimal = decimalValue - randomInt
		finalDecimal = intermediateDecimal % 4
		cipherAlpha = chr(finalDecimal)
		stringValue = stringValue + cipherAlpha
	return stringValue


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
    randomInt = random.randint(0,100)
    binaryString = ''
    stringValue = ''
    encryptText = input("Enter the Plain Text: ")
    ciphertext = encrypt(table, encryptText)
    finalCipher = encryptStageTwo(binaryString,ciphertext,randomInt)
    print("Cipher Text: "+str(finalCipher))
    
    decryptText = input("Enter the Cipher Text: ")
    intermediateDecrypt = decryptStageZero(decryptText,randomInt,stringValue)
    finalDecrypt = decrypt(table, intermediateDecrypt)
    print("Decrypted Text: "+finalDecrypt)
