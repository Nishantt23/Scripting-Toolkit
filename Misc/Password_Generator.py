import secrets
import string

def gen_password(password_length):
 
    characters = string.ascii_letters + string.digits

    secure_password = ''.join(secrets.choice(characters) for i in range(password_length))

    return secure_password

def main():

    user_pass_length = int(input("Enter password length: "))

    print("Password: " , gen_password(user_pass_length))

main()