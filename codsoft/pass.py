import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

print("\nChoose Password Complexity")
print("1. Letters")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Special Characters")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    characters = string.ascii_letters

elif choice == "2":
    characters = string.ascii_letters + string.digits

elif choice == "3":
    characters = string.ascii_letters + string.digits + string.punctuation

else:
    print("Invalid choice!")
    exit()

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:", password)