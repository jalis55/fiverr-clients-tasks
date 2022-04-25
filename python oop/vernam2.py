from vigenere import encrypt, decrypt, random_key


def vernam_encryption(plain_text,key):

    # convert into lower cases and remove spaces
    
    plain_text=plain_text.replace(" ","")
    key=key.replace(" ","")
    plain_text=plain_text.lower()
    key=key.lower()
    
    # conditional statements
    if(len(plain_text)!=len(key)):
        print("Lengths are different")
        
    else:
        cipher_text=""
        
        # iterating through the length
        for i in range(len(plain_text)):
            k1=ord(plain_text[i])-97
            k2=ord(key[i])-97
            s=chr((k1+k2)%26+97)
            cipher_text+=s
        # print("Enrypted message is: ",cipher_text)
        return cipher_text


def vernam_decryption(cipher_text,key):

    # convert into lower cases and remove spaces
    cipher_text=cipher_text.lower()
    key=key.lower()
    cipher_text=cipher_text.replace(" ","")
    key=key.replace(" ","")
    
    plain_text=""
    
    # iterating through the length
    for i in range(len(cipher_text)):
        k1=ord(cipher_text[i])-97
        k2=ord(key[i])-97
        s=chr((((k1-k2)+26)%26)+97)
        plain_text+=s
    # print("Decrypted message is: ",plain_text)
    return plain_text


 

def main():
    while True:
        print("1.Vernam cipher encryption")
        print("2.Vernam cipher decryption")
        print("3.Vingenere cipher encryption")
        print("4.Vingenere cipher decryption")
        print("5.Exit")
        choice=input("Enter choice:")
        if choice == '1':
            print("Vernam Encryption")
            plain_text=input("Enter the message to be encrypted: ")
            key=input("Enter the one time pad: ")
            cipher_text=vernam_encryption(plain_text,key)
            print("Enrypted message is: ",cipher_text)
            continue
        if choice == '2':
            print("Vernam Decryption")
            plain_text=input("Enter the message to be decrypted: ")
            key=input("Enter the one time pad: ")
            plain_text=vernam_decryption(plain_text,key)
            print("Decrypted message is: ",plain_text)
            continue
        if choice =='3':
            print("Vingenere Encryption")
            plain_text = input("Enter the message to be encrypted: ")
            key :str =input("Enter key:")
            # cipher_text=vingenere_decryption(plain_text,key)
            cipher = encrypt(plain_text,key)
            print("Enrypted message is: ",cipher)
            continue

        if choice =='4':
            print("Vingenere Encryption")
            cipher_text = input("Enter the message to be decrypted: ")
            key :str =input("Enter key:")
            # plain_text=vingenere_decryption(cipher_text,key)
            print("Decrypted message is: ",decrypt(cipher, key))
            continue
           


        if choice == '5':
            exit()
        else:
            print("Invalid choice")
main()
