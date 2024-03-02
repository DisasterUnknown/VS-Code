import random
import string

def crack_pass(password):
    attempts = 0
    while True:
        guess = ''.join(random.choices(string.ascii_letters + string.digits, k=len(password)))
        attempts += 1
        print(guess)
        if guess == password:
            return attempts

password = input("Enter the password to crack: ")

print("Cracking password...")

attempts = crack_pass(password)

print(f"The password was cracked in {attempts} attempts.")