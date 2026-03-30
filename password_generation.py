
import string
import secrets

def aleatory_password_g(length):
    "This function generates a aleatory password"
    #REQUIREMENTS:
    ## minimum length
    ## presence of uppercase letters 
    ## lowercaseletters 
    ## numbers
    ## special characters

    numbers = string.digits # Contains all numeric characters
    uppers = string.ascii_uppercase # Contains all uppercase letters
    special_characters = string.punctuation # Contains special symbols
    lowers = string.ascii_lowercase # Contains all lowercase letters

    aleatory_password = [
                        secrets.choice(numbers), # Ensures at least one number
                        secrets.choice(uppers), # Ensures at least one uppercase letter
                        secrets.choice(special_characters), # Ensures at least one special character
                        secrets.choice(lowers), # Ensures at least one lowercase letter
                        ]
    
    rest = numbers + uppers + special_characters + lowers # Combines all possible characters

    for _ in range(length -4):
        aleatory_password.append(secrets.choice(rest)) # Fills the rest of the password randomly

    secrets.SystemRandom().shuffle(aleatory_password) # Shuffles characters for better randomness

    return ''.join(aleatory_password)  # Converts the list into a final string
