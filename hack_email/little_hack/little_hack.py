import time

def load_fake_data(file_path):
    with open(file_path, 'r') as file:
        data = {}
        for line in file:
            email, password = line.strip().split(':')
            data[email] = password
        return data


def brute_force(email, correct_password, pass_list):
    print(f"Starting brute-force attack on {email}...")
    for attempt in pass_list:
        attempt = attempt.strip()
        print(f"Trying password: {attempt}")
        if attempt == correct_password:
            print(f"[+] Password cracked for {email}: {attempt}")
            return True
        time.sleep(0.1)  
    print(f"[-] Failed to crack password for {email}")
    return False


def main():
    email_file = "email.txt"  
    passwords_file = "password.txt"  

    email_data = load_fake_data(email_file)
    
    with open(passwords_file, 'r') as file:
        pass_list = file.readlines()

    for email, correct_password in email_data.items():
        brute_force(email, correct_password, pass_list)

if __name__ == "__main__":
    main()

