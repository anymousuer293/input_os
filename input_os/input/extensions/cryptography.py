msg = ""

def run():
    print("You are encrpyting not decrypting.")
    print("Options:\n1. Atbash Cipher\n2. Caesar Cipher\n3. Vigenere Cipher")
    inp = input("Your Choice: ")
    if int(inp) == 1:
        lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}
        cipher = ""
        for letter in msg:
            # checks for space
            if(letter.upper() != ' '):
                #adds the corresponding letter from the lookup_table
                cipher += lookup_table[letter.upper()]
            else:
                # adds the letter
                cipher += letter.lower()
        print(cipher)
    if int(inp) == 2:
        shift = int(input("Shift of: "))
        def encrypt(text,s):
            result = ""
        
            # traverse text
            for i in range(len(text)):
                char = text[i]
        
                # Encrypt uppercase characters
                if (char.isupper()):
                    result += chr((ord(char) + s-65) % 26 + 65)
        
                # Encrypt lowercase characters
                else:
                    result += chr((ord(char) + s - 97) % 26 + 97)
        
            return result
        print(encrypt(msg, shift))
    if int(inp) == 3:
        key = input("Key: ")
        def generateKey(string, key):
            key = list(key)
            if len(string) == len(key):
                return(key)
            else:
                for i in range(len(string) -
                            len(key)):
                    key.append(key[i % len(key)])
            return("" . join(key))
            
        # This function returns the
        # encrypted text generated
        # with the help of the key
        def cipherText(string, key):
            cipher_text = []
            for i in range(len(string)):
                x = (ord(string[i.upper()]) +
                    ord(key[i.upper()])) % 26
                x += ord('A')
                cipher_text.append(chr(x))
            return("" . join(cipher_text))
            
        # This function decrypts the
        # encrypted text and returns
        # the original text
        def originalText(cipher_text, key):
            orig_text = []
            for i in range(len(cipher_text)):
                x = (ord(cipher_text[i]) -
                    ord(key[i]) + 26) % 26
                x += ord('A')
                orig_text.append(chr(x))
            return("" . join(orig_text))

        print(cipherText(msg, key))

        # This code is contributed
        # by Pratik Somwanshi   

def run1():
    print("You are decrypting not encrypting.")
    print("Options:\n1. Atbash Cipher\n2. Caesar Cipher\n3. Vigenere Cipher")
    inp = input("Your Choice: ")
    if int(inp) == 1:
        lookup_table = {'A' : 'Z', 'B' : 'Y', 'C' : 'X', 'D' : 'W', 'E' : 'V',
        'F' : 'U', 'G' : 'T', 'H' : 'S', 'I' : 'R', 'J' : 'Q',
        'K' : 'P', 'L' : 'O', 'M' : 'N', 'N' : 'M', 'O' : 'L',
        'P' : 'K', 'Q' : 'J', 'R' : 'I', 'S' : 'H', 'T' : 'G',
        'U' : 'F', 'V' : 'E', 'W' : 'D', 'X' : 'C', 'Y' : 'B', 'Z' : 'A'}
        cipher = ""
        for letter in msg:
            # checks for space
            if(letter.upper() != ' '):
                #adds the corresponding letter from the lookup_table
                cipher += lookup_table[letter.upper()]
            else:
                # adds the letter
                cipher += letter.lower()
        print(cipher)
    if int(inp) == 2:
        shift = int(input("Shift of: "))
        message = msg.upper()
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""

        for letter in message:
            if letter in alpha: #if the letter is actually a letter
                #find the corresponding ciphertext letter in the alphabet
                letter_index = (alpha.find(letter) - shift) % len(alpha)

                result = result + alpha[letter_index]
            else:
                result = result + letter
        print(result)
    if int(inp) == 3:
        key = input("Key: ")
        def generateKey(string, key):
            key = list(key)
            if len(string) == len(key):
                return(key)
            else:
                for i in range(len(string) -
                            len(key)):
                    key.append(key[i % len(key)])
            return("" . join(key))
            
        # This function returns the
        # encrypted text generated
        # with the help of the key
        def cipherText(string, key):
            cipher_text = []
            for i in range(len(string)):
                x = (ord(string[i]) +
                    ord(key[i])) % 26
                x += ord('A')
                cipher_text.append(chr(x))
            return("" . join(cipher_text))
            
        # This function decrypts the
        # encrypted text and returns
        # the original text
        def originalText(cipher_text, key):
            orig_text = []
            for i in range(len(cipher_text)):
                x = (ord(cipher_text[i]) -
                    ord(key[i]) + 26) % 26
                x += ord('A')
                orig_text.append(chr(x))
            return("" . join(orig_text))

        print(originalText(msg, key))
        # This code is contributed
        # by Pratik Somwanshi 