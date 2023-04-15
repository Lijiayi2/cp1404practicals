# Time estimate: 30 minutes

def extract_name(email):
    """Given an email, returns the name."""
    # Split the email address by '@' and get the first part
    name = email.split('@')[0]
    # Split the name by '.' and join it with ' ' to capitalize each word
    name = ' '.join(name.split('.')).title()
    return name

# Initialize an empty dictionary
users = {}

# Loop until the user enters a blank email
while True:
    email = input("Email: ")
    if not email:
        break
    # Extract the name from the email
    name = extract_name(email)
    # Ask the user to confirm the name
    confirmation = input(f"Is your name {name}? (Y/n)").lower()
    if confirmation in {'n', 'no'}:
        name = input("Name: ").title()
    # Store the email and name in the dictionary
    users[email] = name

# Print out the dictionary in the format "Name (email)"
for email, name in users.items():
    print(f"{name} ({email})")
