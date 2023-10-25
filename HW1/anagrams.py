def is_anagram(word1, word2):
    """Takes in two Strings and prints 'True' if they are anagrams or 'False' if not"""

    # Checks if both strings are the same length. If not, they are not anagrams
    if len(word1) != len(word2):
        return False

    # Else, checks if both Strings have the same number of each character to check if they are anagrams
    else:
        dict_letters1 = create_dictionary(word1)
        dict_letters2 = create_dictionary(word2)
        if dict_letters1 == dict_letters2:
            return True
        else:
            return False

def create_dictionary(word):
    """Creates a dictionary with key value pairs that record the number of times each character is present in a given String"""
    dict_letters = {}
    for char in word:
        # if char is already a key in dictionary, increase it's value by 1
        if char in dict_letters:
            dict_letters[char] += 1

        # else if char not already in dictionary, create a new key 'char' and set its value to 1
        else:
            dict_letters[char] = 1
    return dict_letters

print(is_anagram('rat', 'tar'))
print(is_anagram('rat', 'hat'))