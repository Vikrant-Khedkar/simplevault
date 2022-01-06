import shutil
import os
from os import path
from cryptography.fernet import Fernet

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
      # read all file data
      file_data = file.read()
          # encrypt data
      encrypted_data = f.encrypt(file_data)
        # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_data)

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename, "wb") as file:
        file.write(decrypted_data)

def compress():
    

            if path.exists('sdk.md'):
                
                file = "sdk.md"
                key = load_key()
                decrypt(file,key)
                os.rename('sdk.md', 'sdk.zip')
                shutil.unpack_archive('sdk.zip', 'raw')
                os.remove('sdk.zip')
                print("sdk.zip has been removed successfully")


            shutil.make_archive('ek', 'zip', 'raw')
            
            if path.exists("ek.zip"):
                                              
                os.rename('ek.zip', 'sdk.md')                            
                key = load_key()
                file = "sdk.md"
                encrypt(file, key)
            prune()
def decompress():
    try:
            if path.exists('sdk.md'):
                      
                        file = "sdk.md"
                        key = load_key()
                        decrypt(file,key)
                        os.rename('sdk.md', 'sdk.zip')
                        shutil.unpack_archive('sdk.zip', 'raw')
                        os.rename('sdk.zip','sdk.md')
                        encrypt(file,key)
                        print("Unpacked")
    except:
        print("No file to decrypt")

def prune():
    try:    
         shutil.rmtree('raw')
         print(" raw has been removed successfully" % dir)
    except:
         print("Empty raw")
# uncomment this if it's the first time you run the code, to generate the key
#write_key()
print("Enter password")
password=input()
if(password=="6969"):
        print("Enter 1 to encrypt")
        print("Enter 2 to decrypt")
        print("Enter 3 to delete raw")
        print("Enter 0 to exit")
        a=int(input("Enter value"))
        if(a==1):
            compress()
        elif(a==2):
            decompress()
        elif(a==3):
            prune()
        elif(a==0):
            print("Exited")
            exit()
        else:
            print("Option not available")
        while(a!=0):
            print("Enter 1 to encrypt")
            print("Enter 2 to decrypt")
            print("Enter 3 to delete raw")
            print("Enter 0 to exit")
            a=int(input("Enter value"))
            if(a==1):
                compress()
            elif(a==2):
                decompress()
            elif(a==3):
                prune()
            elif(a==0):
                print("Exited")
                exit()
            else:
                print("Option not available")
    
    


    
else:
    exit()


