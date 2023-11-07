import random
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%&amp;*1234567890"
length = int(input("Enter Password length: "))
password = ""
for i in range(length):
    password += random.choice(characters)
print(password)