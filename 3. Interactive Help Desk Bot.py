'''
Objective:
The aim of this assignment is to create an interactive help desk bot that processes user queries and responds appropriately for
 a SaaS application.

Task 1: Command Parser
Write a script that takes a user's text input and identifies if it contains one of the predefined 
commands (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.

'''

# def parse_command(text):
#     # Predefined commands and their corresponding responses
#     commands = {
#         "help": "Sure, I can help you with that!",
#         "issue": "Please describe the issue you're facing.",
#         "contact support": "You can contact our support team at support@example.com."
#     }
    
#     # Check if the text contains any predefined command
#     for command, response in commands.items():
#         if command in text.lower():
#             return response
    
#     # If no command is found
#     return "No valid command found."

# # Example usage:
# user_input = input("Enter your text: ")
# response = parse_command(user_input)
# print(response)


'''
Task 2: Issue Categorizer
If the user's input contains the word "issue", further categorize the issue based on 
keywords such as "login", "performance", "error", etc. 
Print out the category of the issue for the support team.
'''

def categorize_issue(text):
    # Keywords for issue categorization
    categories = {
        "login": ["login", "signin", "sign in", "authentication"],
        "performance": ["performance", "slow", "lag", "speed"],
        "error": ["error", "bug", "crash", "issue"],
        "other": ["other", "general"]
    }
    
    # Check if the text contains the word "issue"
    if "issue" in text.lower():
        # Check for keywords in the text to categorize the issue
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword in text.lower():
                    return category
        
        # If no specific category is found, categorize as "other"
        return "other"
    else:
        return None

# Example usage:
user_input = input("Describe the issue you're facing: ")
category = categorize_issue(user_input)
if category:
    print("Category:", category)
else:
    print("No issue identified.")
