name = input('Enter name: ')
while name != "Q":
    print('(H)ello')
    print('(G)oodbye')
    print('(Q)uit')

choice = input()

if choice.upper() == 'H':
    print('Hello', name)
elif choice.upper() == 'G':
    print('Goodbye', name)
elif choice.upper() == 'Q':
    print("finished.")
else:
    print('Invalid choice')