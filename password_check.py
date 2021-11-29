"""
Check Login Credentials.

Password Checker. Created by Yue Cao. 24-11-2021
"""


def main():
    """Start Program"""
    password = input("Enter a password: ")
    
    if check_password(password):
        print("Logged in!")
    else:
        print("Password error!")


def check_password(password):
    return password == "Caoyue0000"


main()
