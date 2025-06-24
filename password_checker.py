import re
def analyze_password(password):
    suggestions = []
    score = 0
    length = len(password)

    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add special symbols (e.g., !@#$%).")

    if score >= 6:
        strength = "Very Strong"
    elif score >= 4:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, suggestions

def main():
    print("Password Strength Checker\n--------------------------")
    password = input("Enter your password: ")
    strength, suggestions = analyze_password(password)
    print(f"\nStrength: {strength}")
    if suggestions:
        print("Suggestions:")
        for s in suggestions:
            print(f"- {s}")
    else:
        print("Your password is strong!")

if __name__ == "__main__":
    main()
