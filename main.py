"""
    Author: Rayhan Hossain
    Date created: 01/02/2024
    Last modified: 01/02/2024
    Python Version: 3.12
"""
import random
from alphanumeric_symbols import letters, numbers, symbols


def generate_password():
    try:
        nr_letters = int(input("How many letters would you like in your password?\n"))
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))
    except ValueError:
        print("Please enter a valid integer.")
        return generate_password()

    password = []

    # Add the letters in the password list
    for letter_amount in range(1, nr_letters + 1):
        password += random.choice(letters)

    # Add the symbols in the password list
    for symbol_amount in range(1, nr_symbols + 1):
        password += random.choice(symbols)

    # Add the numbers in the password list
    for number_amount in range(1, nr_numbers + 1):
        password += random.choice(numbers)

    # Shuffle the position of the password
    random.shuffle(password)

    new_password = ""

    # Add each letter in the password
    for eachPassword in password:
        new_password += eachPassword

    # Print the password to user
    print(f"Your password is: {new_password}")


print("Welcome to the Password Generator!")
generate_password()
