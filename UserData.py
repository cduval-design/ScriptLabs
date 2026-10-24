# Import all necessary modules
from datetime import date
import getpass
import hashlib
import json


# Define header function
def header():
    # "Clear" the screen (not available in IDLE)
    print("\n" * 100)

    print("Name: LastName, FirstName")
    print("Course: CourseNumber")
    print("Assignment: Final Assessment")
    print("Current Date:", date.today())

    print("\n" * 5)


# Dictionary named 'users' for the user accounts
users = {}


# Function to collect user data with a loop
def create_users():
    while True:
        name = input("Please enter the full name of the user: ")
        while True:
            username = input("Please enter the chosen username of the user: ")
            if username in users:
                print("\nThat username already exists. Please choose another.")
                continue
            break
        password = getpass.getpass("Please enter the password for the user: ")

        add_user(name, username, password)

        while True:
            choice = input("\nWould you like to add another user? (Y/N): ").upper()
            if choice == "Y":
                break
            elif choice == "N":
                return
            else:
                print("\nInvalid choice. Please enter Y or N.")


# Function to add users to the dictionary
def add_user(name, username, password):
    users[username] = {
        "name": name,
        "username": username,
        "password": hash_password(password),
    }
    print("\nUser added successfully!")


# Function to hash the user password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Function to write user data to JSON file
def save_users():
    try:
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)
        print("\nUser data saved successfully!")
    except IOError:
        print("\nError: User data could not be saved.")


# Function to authenticate users through the JSON file
def authenticate_users(username, password):
    try:
        with open("users.json", "r") as file:
            saved_users = json.load(file)
        if username in saved_users:
            hashed_password = hash_password(password)
            if hashed_password == saved_users[username]["password"]:
                return 1
            else:
                return 2
        else:
            return 3
    except FileNotFoundError:
        return 4
    except json.JSONDecodeError:
        return 5


# Main program function
def main():
    header()

    print("\n\n=== User Creation Portal ===\n\n")
    create_users()

    save_users()

    print("\n" * 100)
    print("=== User Authentication ===\n\n")

    while True:
        username = input("Please enter your username: ")
        password = getpass.getpass("Please enter your password: ")

        result = authenticate_users(username, password)
        if result == 1:
            print("\nAuthentication successful!")
        elif result == 2:
            print("\nAuthentication failed. Incorrect password.")
        elif result == 3:
            print("\nAuthentication failed. Username not found.")
        elif result == 4:
            print("\nError: User data file not found.")
        else:
            print("\nError: Unable to authenticate user.")
        while True:
            choice = input(
                "\nWould you like to authenticate another user? (Y/N): "
            ).upper()

            if choice == "Y":
                break
            elif choice == "N":
                print("\n\n=== Exiting ===\n\n")
                return
            else:
                print("\nInvalid choice. Please enter Y or N.")


main()
