"""
Password Generator
-------------------
Generates strong, random passwords based on user-specified length
and complexity (character types to include).
"""

import random
import string


def get_password_length():
    """Prompt the user for a valid password length."""
    while True:
        try:
            length = int(input("Enter desired password length (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4 for decent security. Try again.")
                continue
            return length
        except ValueError:
            print("Please enter a valid whole number.")


def get_complexity_options():
    """Ask the user which character types to include in the password."""
    print("\nChoose password complexity (press Enter to include, type 'n' to exclude):")
    use_upper = input("Include uppercase letters (A-Z)? [Y/n]: ").strip().lower() != "n"
    use_lower = input("Include lowercase letters (a-z)? [Y/n]: ").strip().lower() != "n"
    use_digits = input("Include numbers (0-9)? [Y/n]: ").strip().lower() != "n"
    use_symbols = input("Include symbols (!@#$%^&*)? [Y/n]: ").strip().lower() != "n"

    # Make sure at least one character type is selected
    if not any([use_upper, use_lower, use_digits, use_symbols]):
        print("\nNo character types selected. Defaulting to lowercase letters only.\n")
        use_lower = True

    return use_upper, use_lower, use_digits, use_symbols


def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    """Generate a random password using the selected character sets."""
    character_pool = ""
    guaranteed_chars = []

    if use_upper:
        character_pool += string.ascii_uppercase
        guaranteed_chars.append(random.choice(string.ascii_uppercase))
    if use_lower:
        character_pool += string.ascii_lowercase
        guaranteed_chars.append(random.choice(string.ascii_lowercase))
    if use_digits:
        character_pool += string.digits
        guaranteed_chars.append(random.choice(string.digits))
    if use_symbols:
        character_pool += string.punctuation
        guaranteed_chars.append(random.choice(string.punctuation))

    # Fill the rest of the password length with random choices from the pool
    remaining_length = length - len(guaranteed_chars)
    random_chars = [random.choice(character_pool) for _ in range(remaining_length)]

    # Combine guaranteed chars (ensures every selected type appears at least once)
    # with the rest, then shuffle so it's not predictable
    password_chars = guaranteed_chars + random_chars
    random.shuffle(password_chars)

    return "".join(password_chars)


def main():
    print("=" * 40)
    print("      RANDOM PASSWORD GENERATOR")
    print("=" * 40)

    length = get_password_length()
    use_upper, use_lower, use_digits, use_symbols = get_complexity_options()

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

    print("\nYour generated password is:")
    print(f">>> {password} <<<")


if __name__ == "__main__":
    main()
