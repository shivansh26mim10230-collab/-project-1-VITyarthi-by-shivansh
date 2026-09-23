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

def check_password_strength(password):
   
    has_lower = False
    has_upper = False
    has_digit = False
    has_symbol = False

    for character in password:
        if character in LOWER :
            has_lower = True
        elif character in UPPERCASE:
            has_upper = True
        elif character in DIGITSS:
            has_digit = True
        elif character in SYMBOLS:
            has_symbol = True

    score = 0
    feedback = []  # list of tips to show the user

    
    if len(password) >= 12:
        score = score + 2
    elif len(password) >= 8:
        score = score + 1
    else:
        feedback.append("Make it at least 8 characters long (12+ is even better).")

   
    if has_lower:
        score = score + 1
    else:
        feedback.append("Add LOWER  letters.")

    if has_upper:
        score = score + 1
    else:
        feedback.append("Add uppercase letters.")

    if has_digit:
        score = score + 1
    else:
        feedback.append("Add numbers.")

    if has_symbol:
        score = score + 1
    else:
        feedback.append("Add special characters like !@#$%.")

    
    if score >= 6:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, score, feedback



def main():
    print("=== Password Suggestion & Strength Checker ===")
    print("")

   
    print("Here are 3 random password suggestions:")
    suggestions = generate_password_suggestions(12, 3)
    count = 1
    for password in suggestions:
        print("  " + str(count) + ". " + password)
        count = count + 1

    print("")
    print("Now let's test your own password.")
    user_password  = input("Enter a password to check: ")

    strength, score, feedback = check_password_strength(user_password)
    print("")
    print("Strength: " + strength + " (score: " + str(score) + ")")

    if len(feedback) > 0:
        print("Suggestions to improve:")
        for tip in feedback:
            print("  - " + tip)
    else:
        print("Great job! No improvements needed.")
main()