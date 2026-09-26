from builtins import range
import random

LOWER  = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGITSS = "0123456789"
SYMBOLS = "!@#$%^&*"

ALL_CHARACTERS = LOWER  + UPPERCASE + DIGITSS + SYMBOLS

def generate_one_password(L):
   
    password = ""  # start with an empty string
    for i in range(L):
        random_character = random.choice(ALL_CHARACTERS)
        password = password + random_character  # add it to the end
    return password

def generate_password_suggestions(L, count):
   
    suggestions = []
    for i in range(count):
        new_password = generate_one_password(L)
        suggestions.append(new_password)
    return suggestions