import re
import random
import string

def strong_password(password):
    if len(password) < 12:
        return False
    if not re.search(r'[A-Z]', password):
        return False
    if not re.search(r'[a-z]', password):
        return False
    if not re.search(r'\d', password):
        return False
    if not re.search(r'[!@#$%^&*()-=_+[{}|;:",.<>/?]', password):
        return False
    return True

def strengthen_password(password):
    while not strong_password(password):
        position = random.randint(0, len(password))
        new_character = random.choice(string.ascii_letters + string.digits + '!@#$%^&*()-=_+][}{|;:",.<>/?]')
        password = password[:position] + new_character + password[position:]
    return password

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    password = input('Enter Your Password: ')
    if strong_password(password):
        print("Password is strong.")
    else:
        print("Password is weak. Modifying...")
        password = strengthen_password(password)
        print("Modified Password:", password)

    generate_new = input("Would you like to generate a new password? (yes/no): ")
    if generate_new.lower() == "yes":
        length = int(input("Enter the length of the new password: "))
        new_password = generate_password(length)
        print("Generated Password:", new_password)

if __name__ == "__main__":
    main()
