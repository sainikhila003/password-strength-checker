import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Use at least 8 characters.")

    # Uppercase check
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("🔸 Add at least one uppercase letter.")

    # Lowercase check
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("🔸 Add at least one lowercase letter.")

    # Digit check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("🔸 Include at least one number.")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("🔸 Include at least one special character (e.g., !, @, #).")

    # Result
    if score == 5:
        strength = "✅ Strong Password"
    elif 3 <= score < 5:
        strength = "⚠️ Moderate Password"
    else:
        strength = "❌ Weak Password"

    return strength, feedback

# Main script
if __name__ == "__main__":
    print("🔐 Password Strength Checker 🔍")
    password = input("Enter your password: ")
    strength, suggestions = check_password_strength(password)

    print("\nPassword Strength: ", strength)
    if suggestions:
        print("Suggestions to improve your password:")
        for tip in suggestions:
            print(tip)
