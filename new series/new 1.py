import random
import string

# Defining
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

# Get user input and more defining
user_input = input("How many characters should the password be? ")
user_length = int(user_input)
password = generate_password(user_length)

# Save the password to a file
with open("my_passwords.txt", "a") as file:
    file.write(password + "\n")

print(f"✅ Saved to my_passwords.txt: {password}")

input("\nPress Enter to close...")