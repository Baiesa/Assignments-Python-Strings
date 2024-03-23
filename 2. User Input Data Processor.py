'''
Task 1: Input Length Validator
Write a script that checks the length of the user's first name and last name. 
Both should be at least 2 characters long. If not, print an error message.
'''

# def validate_name_length(first_name, last_name):
#     if len(first_name) < 2 or len(last_name) < 2:
#         print("Error: Both first name and last name should be at least 2 characters long.")
#     else:
#         print("First name and last name length are valid.")


# first_name = input("Enter your first name: ")
# last_name = input("Enter your last name: ")
# validate_name_length(first_name, last_name)

'''
Task 2: Password Complexity Checker
Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, 
contain one uppercase letter, one lowercase letter, and one number. 
If the password does not meet these criteria, print a message explaining the complexity requirements.
'''
# def check_password_complexity(password):
   
#     if len(password) < 8:
#         print("Password must be at least 8 characters long.")
#         return False
    
#     has_uppercase = any(char.isupper() for char in password)
#     has_lowercase = any(char.islower() for char in password)
#     has_digit = any(char.isdigit() for char in password)
    
#     if not (has_uppercase and has_lowercase and has_digit):
#         print("Password must contain at least one uppercase letter, one lowercase letter, and one number.")
#         return False
    
  
#     print("Password meets complexity requirements.")
#     return True


# password = input("Enter your password: ")
# check_password_complexity(password)


'''
Task 3: Email Formatter
Implement a script that ensures all user email addresses are in a standard format
'''
import re

def format_email(email):
    # Define a regular expression pattern for validating email format
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Check if the email matches the pattern
    if re.match(email_pattern, email):
        # If the email is already in the standard format, return it
        return email
    else:
        # If the email is not in the standard format, suggest a correction or notify the user
        print("The email address is not in a standard format. Please check and correct it.")
        return None

# Example usage:
email = input("Enter your email address: ")
formatted_email = format_email(email)
if formatted_email:
    print("Formatted email:", formatted_email)
