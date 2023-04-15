"""
Time estimate: 45 minutes
"""

def count_words(string):
    # Create an empty dictionary to store word counts
    word_count = {}

    # Split the string into a list of words
    words = string.split()

    # Loop through the words and update the word count dictionary
    for word in words:
        # Convert the word to lowercase to ignore case
        word = word.lower()
        if word in word_count:
            # If the word is already in the dictionary, increment its count
            word_count[word] += 1
        else:
            # If the word is not in the dictionary, add it with a count of 1
            word_count[word] = 1

    # Find the length of the longest word for formatting
    max_length = max(len(word) for word in word_count)

    # Sort the word count dictionary by keys in alphabetical order
    sorted_word_count = sorted(word_count.items())

    # Print the word counts with aligned columns
    for word, count in sorted_word_count:
        print(f"{word:{max_length}} : {count}")

# Ask the user for a string and count the words
user_input = input("Enter a string: ")
count_words(user_input)
