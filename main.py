
from generate import generate_password_suggestions
from suggestion  import check_password_strength
import random

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
        print("Great job No improvements needed.")
main()