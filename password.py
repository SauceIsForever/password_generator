import random

# Character sets for password generation
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', ',', '.', '<', '>', '/', '?']

new_password = ""

print("Password Generator Options:")
print("1. Lowercase letters (a-z)")
print("2. Uppercase letters (A-Z)")
print("3. Numbers (0-9)")
print("4. Special characters (!@#$%^&*, etc.)")

password_length = int(input("\nChoose your password length: "))
password_options = input("Choose your password options here: ")

options_list = [int(number) for number in password_options]

combined_list = []

for option in options_list:
    if 1 in options_list:
        combined_list.extend(lower_case)
    if 2 in options_list:
        combined_list.extend(upper_case)
    if 3 in options_list:
        combined_list.extend(numbers)
    if 4 in options_list:
        combined_list.extend(special_chars)

for char in range(password_length):
    random_char = random.choice(combined_list)
    new_password += random_char

print(f"\nHere is your randomly generated password: {new_password}")