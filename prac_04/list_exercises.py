
# initialize an empty list to store the numbers
numbers = []

# prompt the user to enter 5 numbers and append them to the list
for i in range(5):
    num = float(input("Enter a number: "))
    numbers.append(num)

# output information about the numbers
print("Numbers:", numbers)
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter your username: ")

if username in usernames:
    print("Access granted")
else:
    print("Access denied")
