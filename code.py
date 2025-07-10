import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Total score
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = 5 - sum(errors)

    # Feedback
    print("\nPassword Strength Check:")
    if score == 5:
        print("✅ Very Strong Password")
    elif score >= 4:
        print("🟢 Strong Password")
    elif score >= 3:
        print("🟡 Moderate Password")
    else:
        print("🔴 Weak Password")

    # Detailed suggestions
    if length_error:
        print("❗ Use at least 8 characters.")
    if digit_error:
        print("❗ Add at least one digit (0–9).")
    if uppercase_error:
        print("❗ Add at least one uppercase letter (A–Z).")
    if lowercase_error:
        print("❗ Add at least one lowercase letter (a–z).")
    if symbol_error:
        print("❗ Add at least one special character (!@#$...).")

# User input
user_password = input("Enter your password: ")
check_password_strength(user_password)
