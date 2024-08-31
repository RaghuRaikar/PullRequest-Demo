# random_password_generator.py

import random
import string
#ADDING COMMENT FOR PULL REQUEST

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("Random Password Generator")
    
    try:
        length = int(input("Enter the length of the password: "))
        
        if length < 6:
            print("Password length should be at least 6 characters.")
        else:
            password = generate_password(length)
            print(f"Generated passwords1: {password}")
    
    except ValueError:
        print("Please enter a valid number for the length.")

if __name__ == "__main__":
    main()
