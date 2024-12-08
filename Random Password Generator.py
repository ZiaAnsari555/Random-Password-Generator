import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print(generate_password(15))  # Generates a 12-character random password
