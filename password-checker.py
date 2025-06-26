import re

def check_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1

    if re.search(r'\d', password):
        strength += 1

    if re.search(r'[@$!%*?&]', password):
        strength += 1

    if strength == 4:
        return "Strong"
    elif strength == 3:
        return "Medium"
    else:
        return "Weak"

# Main part
if __name__ == "__main__":
    pwd = input("Enter your password: ")
    result = check_strength(pwd)
    print("Password strength:", result)
