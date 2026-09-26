from generate import generate_one_password, LOWER, UPPERCASE, DIGITSS, SYMBOLS
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