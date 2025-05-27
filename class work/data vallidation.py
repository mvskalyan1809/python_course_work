import re
from datetime import datetime
def validate_name(name):
    pattern=r'^[a-Za-z]{2,25} ([A-Za-z]{2,25})+$'
    return bool(re.fullmatch(pattern,name))

def validate_email(email):
    pattern=r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.fullmatch(pattern, emial))

def validate_phone(phone):
    pattern=r'^(?:\+91|0)?[6-9]\d{9}$'
    return bool(re.fullmatch(pattern, phone))

def validate_password(password):
    pattern=r'^(?=.*[A-Z]) (?=.*[a-z]) (?=.*\d) (?=.*[@$!%*?&]) [A-Za-z\d@$!%*?&] {8,}$'
    return bool(re.fullmatch(pattern, password))

def validate_username(username):
    pattern=r'^[a-zA-Z0-9] {5,15}$'
    return bool(re.fullmatch(pattern, username))

def validate_dob(dob):
    try:
        datetime.strptime(dob,"%Y-%m-%d")
        return True
    except ValueError:
        return False

def get_valid_input(prompt, validation_func):
    while True:
        user_input=input(prompt)
        if validation_func(user_input):
            return user_input
        else:
            print("Invalid input.Please try again.")

def main():
    print("\nFROM VALIDATION PROGRAM USING REGULAR EXPRESSIONS\n")
    name=get_valid_input("enter your full name(e.g., John Doe): ", validate_name)
    email=get_valid_input("enter your email: ",validate_email)
    phone=get_validate_input("enter your phone number:",validate_phone)
    username=get_validate_input("Create a username (5-15 alphanumeric characters):",validate_username)
    password=get_validate_input("Create a password (min 8chars,1 uppercase,1number,1 speacial char",validate_password)
    dob=get_validate_input("enter a dob(YYYY-MM-DD):",validate_dob)

    print("\nAll fields validated successfully.")
    print("form submitted successfully.")

if __name__=="__main__":
    main()
    
    
    
