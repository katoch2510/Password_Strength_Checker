def check_password_strength(password):
    strength = 0

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        print(" Password must be at least 8 characters long.")

    # Check uppercase
    if any(char.isupper() for char in password):
        strength += 1
    else:
        print("Please add at least one uppercase letter.")

    # Check lowercase
    if any(char.islower() for char in password):
        strength += 1
    else:
        print("Please add at least one lowercase letter.")

    # Check digit
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        print("Please add at least one digit.")

    # Check special character
    if any(char in "!@#$%^&*()_+-=[]{}|;:',.<>?/`~" for char in password):
        strength += 1
    else:
        print(" Please add at least one special character.")

    # Final evaluation
    if strength == 5:
        print("Password is Strong.")
    elif strength >= 3:
        print(" Password is Moderate.")
    else:
        print("Password is Weak.")

# Example usage
password = input("Enter your password: ")
check_password_strength(password)
