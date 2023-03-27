# Write code that asks the user for their name, then opens a file called "name.txt" and writes that name to it.

OUTPUT_FILE = open('name.txt', 'w')
name = input("Enter your name: ")
print(OUTPUT_FILE.write(name))
OUTPUT_FILE.close()

# Write code that opens "name.txt" and reads the name (as above) then prints,
# "Your name is Bob" (or whatever the name is in the file).

FILE_NAME = open('name.txt', 'r')
name = FILE_NAME.read()
print("Your name is: ", name)
FILE_NAME.close()

'''Create a text file called numbers.txt and save it in your prac_02 directory.
Put the following three numbers on separate lines in the file and save it:
17
42
400
Write code that opens "numbers.txt", reads only the first two numbers and adds
them together then prints the result, which should be... 59.'''

NUMBERS_FILE = open('numbers.txt', 'r')
number1 = int(NUMBERS_FILE.readline())
number2 = int(NUMBERS_FILE.readline())
result = number2 + number1
print("The result of line 1 plus line 2 is :",result)
NUMBERS_FILE.close()

# Now write a fourth block of code that prints the total for all lines in
# numbers.txt or a file with any number of numbers.
NUMBERS_FILE = open('numbers.txt', 'r')
Total = 0
for i in NUMBERS_FILE:
    number = int(i)
    Total += number
print("The total number's sum is: ",Total)
NUMBERS_FILE.close()