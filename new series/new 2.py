import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

user_input = input("Type a password. ")
user_length = int(user_input)
password = generate_password(user_imput)

with open("my_passwords.txt", "a") as file:
    file.write(password + "\n")

print(f"✅ Saved to my_passwords.txt: {password}")