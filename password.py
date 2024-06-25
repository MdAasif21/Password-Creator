import secrets
import string
import pyperclip

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    """Generate a secure random password."""
    if not (use_uppercase or use_lowercase or use_digits or use_symbols):
        raise ValueError("At least one character set must be selected")

    char_sets = ""
    if use_uppercase:
        char_sets += string.ascii_uppercase
    if use_lowercase:
        char_sets += string.ascii_lowercase
    if use_digits:
        char_sets += string.digits
    if use_symbols:
        char_sets += string.punctuation

    password = ''.join(secrets.choice(char_sets) for _ in range(length))
    return password

def generate_multiple_passwords(count, length, use_uppercase, use_lowercase, use_digits, use_symbols):
    """Generate multiple secure random passwords."""
    return [generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols) for _ in range(count)]

def copy_to_clipboard(text):
    """Copy the given text to the clipboard."""
    pyperclip.copy(text)
    print("Password copied to clipboard!")

def main():
    try:
        # User input
        count = int(input("How many passwords do you want to generate? "))
        length = int(input("Enter the password length: "))
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        # Generate passwords
        passwords = generate_multiple_passwords(count, length, use_uppercase, use_lowercase, use_digits, use_symbols)

        # Display passwords
        print("\nGenerated Passwords:")
        for i, pwd in enumerate(passwords, 1):
            print(f"{i}: {pwd}")

        # Copy the first password to the clipboard if required
        if input("\nCopy the first password to the clipboard? (y/n): ").lower() == 'y':
            copy_to_clipboard(passwords[0])

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
