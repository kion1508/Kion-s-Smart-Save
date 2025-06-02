import os
import platform
import re # For regular expressions to validate password

# --- Console Clearing Function ---
def clear_console():
    """Clears the terminal screen."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

# --- Password Strength Checker ---
def check_password_strength(password):
    """
    Checks the strength of a password based on common criteria.
    Returns a list of criteria met.
    """
    criteria_met = []
    if len(password) >= 8:
        criteria_met.append("✔ At least 8 characters")
    else:
        criteria_met.append("✖ At least 8 characters")

    if re.search(r"[A-Z]", password):
        criteria_met.append("✔ One uppercase letter")
    else:
        criteria_met.append("✖ One uppercase letter")

    if re.search(r"[a-z]", password):
        criteria_met.append("✔ One lowercase letter")
    else:
        criteria_met.append("✖ One lowercase letter")

    if re.search(r"\d", password):
        criteria_met.append("✔ One number")
    else:
        criteria_met.append("✖ One number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        criteria_met.append("✔ One special character")
    else:
        criteria_met.append("✖ One special character")

    return criteria_met

# --- Sign-Up Form Function ---
def run_signup_form():
    """
    Displays and handles the console-based sign-up form.
    """
    clear_console()

    print("=" * 60)
    print(f"{'BANK APP - CREATE NEW ACCOUNT':^60}")
    print("=" * 60)
    print("\nPlease provide the following details to create your account.")
    print("-" * 60)

    # --- Input Fields ---
    while True:
        email = input(f"{'Email Address':<20}: ").strip()
        if "@" in email and "." in email: # Simple email validation
            break
        print("Invalid email format. Please try again.")

    while True:
        username = input(f"{'Choose Username':<20}: ").strip()
        if len(username) >= 3:
            break
        print("Username must be at least 3 characters long.")

    password = ""
    confirm_password = ""
    while True:
        password = input(f"{'Create Password':<20}: ").strip()
        strength_criteria = check_password_strength(password)
        print("Password Requirements:")
        for criterion in strength_criteria:
            print(f"  {criterion}")

        all_criteria_met = all("✔" in c for c in strength_criteria)

        if not all_criteria_met:
            print("Password does not meet all requirements. Please try again.")
            continue

        confirm_password = input(f"{'Confirm Password':<20}: ").strip()

        if password == confirm_password:
            print("\nPasswords match!")
            break
        else:
            print("Passwords do not match. Please try again.")

    # --- Terms and Conditions (Simulated) ---
    print("\n" + "-" * 60)
    print("Terms and Conditions:")
    print("By creating an account, you agree to our Terms of Service")
    print("and Privacy Policy. (Full text not displayed in console demo)")
    print("-" * 60)

    while True:
        agree = input("Do you agree to the Terms and Conditions? (yes/no): ").lower().strip()
        if agree == 'yes':
            break
        elif agree == 'no':
            print("You must agree to the terms to create an account. Exiting sign-up.")
            return False # Indicate sign-up was not completed
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

    # --- Final Confirmation / Submission ---
    clear_console()
    print("=" * 60)
    print(f"{'REVIEW YOUR DETAILS':^60}")
    print("=" * 60)
    print(f"{'Email':<20}: {email}")
    print(f"{'Username':<20}: {username}")
    print(f"{'Password':<20}: {'*' * len(password)}") # Mask password for display
    print("-" * 60)
    print("\nYour account is ready to be created!")

    final_confirm = input("Press Enter to create account, or 'q' to cancel: ").lower().strip()
    if final_confirm == 'q':
        print("Account creation cancelled.")
        return False
    else:
        print("\n" + "=" * 60)
        print(f"{'ACCOUNT CREATED SUCCESSFULLY!':^60}")
        print("=" * 60)
        print(f"Welcome, {username}! You can now log in to your Bank App.")
        print("Redirecting to login (simulated)...")
        time.sleep(3) # Simulate redirection
        return True # Indicate sign-up was successful

# --- Main Execution ---
if __name__ == "__main__":
    if run_signup_form():
        print("\nSign-up process completed.")
    else:
        print("\nSign-up process aborted or failed.")

