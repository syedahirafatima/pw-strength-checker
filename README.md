# 🔐 Password Strength Checker


This is a simple Python script that checks the strength of a user's password based on key rules such as length, use of digits, uppercase/lowercase letters, and special characters.


#🚀 Features:

1. Checks if password is at least 8 characters long  
2. Detects presence of:
  - Digits (0-9)
  - Uppercase letters (A-Z)
  - Lowercase letters (a-z)
  - Special characters (!@#$%^&*(), etc.)
3. Gives a strength rating: **Very Strong**, **Strong**, **Moderate**, or **Weak**
4. Provides improvement suggestions


# 🧠 How It Works:

The program uses **Python's `re` (regular expressions)** to analyze the password and then gives feedback based on how many rules it satisfies.


# ✅ Sample Output:

Enter your password: Hello123
Password Strength Check:
🟡 Moderate Password
❗ Add at least one special character (!@#$...).


# 🔧 Requirements
Python 3+
No external libraries required (only uses built-in re module)


# 📘 License
This project is licensed under the MIT License.
