import shutil
import os
from os import path

def encrypt():
    

            if path.exists('sdk.md'):
                # rename the original file
                os.rename('sdk.md', 'sdk.zip')
                shutil.unpack_archive('sdk.zip', 'raw')
                os.remove('sdk.zip')
                print("sdk.zip has been removed successfully")


            shutil.make_archive('ek', 'zip', 'raw')
            # os.rename('ek.zip''#atktg.kd')
            if path.exists("ek.zip"):
                # get the path to the file in the current directory
                src = path.realpath("ek.zip")

                # rename the original file
                os.rename('ek.zip', 'sdk.md')


            # Path
            prune()
def decrypt():
    try:
            if path.exists('sdk.md'):
                        # rename the original file
                        os.rename('sdk.md', 'sdk.zip')
                        shutil.unpack_archive('sdk.zip', 'raw')
                        os.rename('sdk.zip','sdk.md')
                        print("Unpacked")
    except:
        print("No file to decrypt")

def prune():
    try:    
         shutil.rmtree('raw')
         print(" raw has been removed successfully" % dir)
    except:
         print("Empty raw")

print("Enter password")
password=input()
if(password=="6969"):
        print("Enter 1 to encrypt")
        print("Enter 2 to decrypt")
        print("Enter 3 to delete raw")
        print("Enter 0 to exit")
        a=int(input("Enter value"))
        if(a==1):
            encrypt()
        elif(a==2):
            decrypt()
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
                encrypt()
            elif(a==2):
                decrypt()
            elif(a==3):
                prune()
            elif(a==0):
                print("Exited")
                exit()
            else:
                print("Option not available")
    
    


    
else:
    exit()


