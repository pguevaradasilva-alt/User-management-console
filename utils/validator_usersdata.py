def username_validartor(username, usersnames):
    "This function will search in the user data base and check if the new user name is allready take it"
    valid = False
    if username not in usersnames: # Checks if the username is available
            valid = True
    else:
        print("The username is already taken, try anothe one.")
        valid = False

    return valid

import string

def validation_password(new_password):
    "This function validates if the password that the user has created meets the requirements"
    #REQUIREMENTS:
    ## minimum length
    ## presence of uppercase letters 
    ## lowercaseletters 
    ## numbers
    ## special characters
    digits = False
    uppers = False
    lowers = False
    special_characters = False
    valid_pass = False

    digits = False 
    special_characters = False

    if len(new_password) < 10: # Checks if the password is shorter than 10 characters 
        valid_pass = False
    
    for i in new_password:
        if i.isdigit(): # Checks if the character is a number
            digits = True
        elif i.isupper(): # Checks if the character is an uppercase letter
            uppers = True
        elif i.islower(): # Checks if the character is a lowercase letter
            lowers = True
        else: 
            special_characters = True # Assumes the character is a special symbol

    if all([digits and uppers and lowers and special_characters]): # Validates that all password requirements are met
        valid_pass = True
    
    return valid_pass

def validate_login(user_name, password, users_data):
    if user_name in users_data: # Checks if the username exists in the database
        correct_nickname = True # Confirms that the username is correct
    else:
        print("User name doesnt match.")
        correct_nickname = False
    
    if password == users_data[user_name]["Password"]: # Checks if the entered password matches the stored one
        correct_password = True # Confirms that the password is correct
    else:
        print("Wrong password. ")
        correct_password = False

    if correct_nickname and correct_password: # Verifies that both username and password are correct
        print("Welcome", users_data[user_name]["Full name"])# Displays a welcome message with the user's full name
        login = True
    else:
        login = False
    
    return login