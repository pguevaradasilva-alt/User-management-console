#!/usr/bin/env python3
"""
User Management Console
-----------------------
This module handles the main flow for user registration and login.
It coordinates data entry, security validations, and password generation.

Usage:
    python3 src/main.py
"""

__author__ = "Pablo Guevara"
__version__ = "1.1.0"
__maintainer__ = "Pablo Guevara"
__status__ = "Development"

# --- Imports ---
import sys
# Importing local modules from the utils package
import utils.validator_usersdata as vu 
import utils.password_generation as pg


usernames = [] # Stores registered usernames
users_data = {} # Stores all user information

def register_user(usernames, users_data):
    "This function will ask the user for his personal data"

    user_name = input("Enter your user name. ")
    valid = vu.username_validartor(user_name, usernames) # Validates the username
#calling the function created
    if valid == True:
        usernames.append(user_name) # Adds the user name to the list of usernames to validate 
        #new entered user names in the future
        users_data[user_name] = {} # Creates a record for the new user
        name = input("Enter your full name: ")
        users_data[user_name]["Full name"] = name

        right_selection = False # Controls the password selection loop

        while right_selection == False:
            password_options = input("Do you want that the program generates a password for you? y/n ").lower()
            if password_options == "n": 
                new_password = input("Create a password, with \
minimum 10 characters, presence of uppercase letters, lowercase \
letters, numbers, and special characters)")
                valid_password = vu.validation_password(new_password) # Checks if the password is secure
                if valid_password == True:
                    print("Valid password")
                    users_data[user_name]["Password"] = new_password # Stores the password
                    right_selection = True
                else:
                    print("Invalid password")
                    print("Suggested password: ", pg.generate_password(length=10)) # Suggests a secure password

            elif password_options == "y":
                new_password = pg.generate_password(length= 10) # Generates a random password
                users_data[user_name]["Password"] = new_password # Stores the password
                print("Your pasword is: ", new_password)
                right_selection = True
            else:
                print("Wrong selection, please try again.")
                
exit = False

while exit == False:
    menu = int(input("Select an option: \n1. Sign in. \n2. Sign up \n3. Show Data base \n4. Exit \n="))

    if menu == 1:
        user_name = input("Enter your user name: ")
        password = input("Enter your password: ")
        valid_login_data = vu.validate_login(user_name, password, users_data) # Validates login credentials
        print("Login", valid_login_data)
    elif menu == 2:
        register_user(usernames, users_data) # Calls the registration function
    elif menu == 3:
        print(users_data) # Displays stored user data
    elif menu == 4:
        sys.exit() # Exits the program




