import string

def count_letters(file):
    """Takes in a file and creates a dictionary and tracks the number of times each letter is used"""

    # Create a dictionary to keep track of how many times a char is in a file
    dict_letters = {}

    with open(file) as f:
        for line in f:
            # Change each line in file to lowercase for comparison with string.ascii_lowercase
            line = line.lower()

            # Check if each char in each line of the file is in string.ascii_lowercase and update dict_letters accordingly
            for char in line:
                if char in string.ascii_lowercase:
                    if char in dict_letters:
                        dict_letters[char] += 1
                    else:
                        dict_letters[char] = 1
    return dict_letters

print(count_letters('frost.txt'))