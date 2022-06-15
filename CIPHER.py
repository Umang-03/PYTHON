#MADE BY UMANG DOBHAL
#CONVERTING TEXT INTO DIFFERENT CIPHERS


import math
def mono(txt):
    result =""
    for i in range(len(txt)):
        char = txt[i]
        if(char.isupper()):
            result += chr((ord(char) + 1) % 26 + 65)
        else:
            result += chr((ord(char) + 1) % 26 + 97)
    return result

def generateKeyforPoly(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("" . join(key))
     
def poly(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = ((ord(string[i]) + ord(key[i])) % 26)
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))

def transpositional(txt,key2):
    cipher = ""
    k_indx = 0
  
    msg_len = float(len(txt))
    msg_lst = list(txt)
    key_lst = sorted(list(key2))
    
    col = len(key)

    row = int(math.ceil(msg_len / col))
  
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
  
    matrix = [msg_lst[i: i + col] 
              for i in range(0, len(msg_lst), col)]
  
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] 
                          for row in matrix])
        k_indx += 1
  
    return cipher


a = str(input("Enter string: "))
print("In which cipher you want to convert your text?? ")
print("1. Monoalphabetic Cipher\n"
      "2. Polyalphabetic Cipher\n"
      "3. Transpositional Cipher\n")

choice = int(input("Enter your choice: "))
if (choice == 1):
    print("Monoalphabetic Cipher for the string", a , "is", mono(a))
elif (choice == 2):
    key = str(input("Enter the key for encryption: "))
    print("Polyalphabetic Cipher for the string", a , "and key", key ,"is", poly(a,key))

elif (choice == 3):
    key = str(input("Enter the key for encryption: "))
    print("Transpostional Cipher for the string", a , "and key", key ,"is", transpositional(a,key))
    
else:
    print("Invalid choice!! Please select correct option.")
