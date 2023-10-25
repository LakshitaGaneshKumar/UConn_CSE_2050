def find_pairs_naive(lst, target):
    """ A naive function that finds all pairs of integers in the input list that add up to the target integer.
    Time complexity: O(n^2)
    """
    pairs = set()                           # 1
    for i in range(len(lst)):               # n
        for j in range(i+1, len(lst)):      #   n
            if lst[i] != lst[j] and lst[i] + lst[j] == target:   #     2 (add, then compare)
                pairs.add((lst[i], lst[j])) #     1
    return pairs                            # 1
                                            #-------------------------
                                            # 1 + n * (n *(2+1)) + 1 = 3n^2 + 2 = O(n^2)
                                            # Hint - searching a list is expensive! Use a data structure
                                            # with a O(1) search cost instead

def find_pairs_opt(lst, target):
    """Uses a set for O(1) membership testing
    Time complexity: O(n)"""
    pairs = set()

    # Creates a set of numbers that have already been iterated over
    found_nums = set()

    for num in lst:
        # Finds the opposite number for each value in list that adds to the target value
        opposite = target - num

        # Checks that num and opposite are not the same value and checks if the opposite 
        # value is in the list by checking if it has already been added to the found_nums set
        if num != opposite and opposite in found_nums:
            pairs.add((opposite, num))
        found_nums.add(num)

    return pairs
    