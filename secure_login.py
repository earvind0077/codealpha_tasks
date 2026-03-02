import hashlib

# Store hashed password instead of plain text
stored_username = "admin"

# Hash of "StrongPass123"
stored_password_hash = hashlib.sha256("StrongPass123".encode()).hexdigest()

attempts = 3

while attempts > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    password_hash = hashlib.sha256(password.encode()).hexdigest()

    if username == stored_username and password_hash == stored_password_hash:
        print("Login Successful!")
        break
    else:
        attempts -= 1
        print("Invalid Credentials")
        print("Attempts left:", attempts)

if attempts == 0:
    print("Account Locked. Too many failed attempts.")
