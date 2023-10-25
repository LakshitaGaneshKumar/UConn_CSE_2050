###############################################################################
# Collaboration                                                               #
# -------------                                                               #
# You can collaborate with up to 3 classmates (for a total of 4 students per  #
# group). If you do so, remember not to share code directly. Discussions are  #
# fine, code sharing is not. Also note that all have to submit individually.  #
#                                                                             #
# Enter any collaborators here:                                               #
# Collaborator 1:                                                             #
# Collaborator 2:                                                             #
# Collaborator 3:                                                             #
###############################################################################

def fizzbuzz(start, finish):
    """Takes in a start and finish number and replace multiples of 3 with 'fizz', 
    multiples of 5 with 'buzz', and multiples of both with 'fizzbuzz'"""

    for num in range(start, finish + 1):
        # Checks if num is divisable by 3 or 5 or if num contains either a 3 or 5 and prints "fizzbuzz" accordingly
        if (num % 3 == 0 and num % 5 == 0) or ("3" in str(num) and "5" in str(num)) or (num % 3 == 0 and "5" in str(num)) or (num % 5 == 0 and "3" in str(num)):
            print("fizzbuzz")
        
        # Checks if num is divisable by 3 or if num contains a 3 and prints "fizz" accordingly
        elif num % 3 == 0 or "3" in str(num):
            print("fizz")

        # Checks if num is divisable by 5 or if num contains a 5 and prints "buzz" accordingly
        elif num % 5 == 0 or "5" in str(num):
            print("buzz")

        # Else, the number itself is printed
        else:
            print(num)

fizzbuzz(1, 15)