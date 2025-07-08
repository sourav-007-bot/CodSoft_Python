import string
import secrets
import sys

import time
def myfun():
    print("=" * 50)
    print("🔐  CUSTOM PASSWORD GENERATOR".center(50))
    print("=" * 50)
def get_password_length():
    while True:
        try:
            length = int(input(" ENTER THE LENGTH OF PASSWORD (min 6): "))
            if length < 6:
                print("⚠️  Password should be at least 4 characters long.")
                continue
            return length
        except ValueError:
            print("❌ Please enter a valid number.")

def choice():
    print("\nChoose password ch:")
    print("1 - Letters only (a-z, A-Z)")
    print("2 - Letters and numbers (a-z, A-Z, 0-9)")
    print("3 - Strong (letters, numbers, symbols)")

    while True:
        choice = input(" YOUR CHOICE (1/2/3): ").strip()
        if choice in ['1', '2', '3']:
            return int(choice)
        print("❌ Invalid choice. Please select 1, 2, or 3.")

 #Password character setting
def Function_pass(choice):
    x = string.ascii_letters
    if choice == 1:
        return x
    elif choice == 2:
        return x + string.digits
    elif choice == 3:
        return x + string.digits + string.punctuation

 #      Generating password 
def generating_p(length, c):
    return ''.join(secrets.choice(c) for _ in range(length))

#   output 
def pass_show(password):
    print("\n🔄 Generating your password...")
    time.sleep(1)
    print("✅ Strong password generated:\n")
    print("#" * 50)
    print("GENERATED PASSWORD : ", password)
    print("#" * 50) 
    print("\nKeep it safe and don’t share it recklessly!")

def main():
    myfun()
    length = get_password_length()
    ch = choice()
    c = Function_pass(ch)
    password = generating_p(length, c)
    pass_show(password)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n Operation cancelled by user.")
        sys.exit(0)