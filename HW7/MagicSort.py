from math import log2

def linear_scan(L): 
    """Performs a linear scan on an inputed list and returns the type of list it is"""
    count = 0
    n = len(L)

    # Traverse through list and count the number of unsorted items
    for i in range(n-1):
        if L[i] > L[i+1]: count += 1
    
    # Case 1: List is already sorted
    if count == 0: return 1
    
    # Case 2: List has O(1) unsorted pairs (i.e. L[j] > L[j+1]). 10 pairs is the upper limit for this case.
    if count <= 10: return 2

    # Case 3: List is reverse sorted
    if count == n-1: return 3

    # Case 0: List doesn't fall under other cases
    return 0


def reverse_list(L):
    """Reverses an inputed list"""
    n = len(L)
    i, j = 0, n-1

    # switches the places of the last items and the first items until list is reversed
    while i < n // 2 and i != j:
        L[i], L[j] = L[j], L[i]
        i += 1
        j -= 1


def insertion_sort(L, left=0, right=None): 
    """Sorts an inputed list with insertion sort"""
    if right is None: right = len(L)
    
    for i in range(left, right):
        j = right - i - 1
        while j < right - 1 and L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
            j+=1


def merge_sort(L, left=0, right=None):
    """Sorts an inputed list with merge sort"""
    if right == None: right = len(L)
    if len(L) < 2: return
    elif len(L) <= 20: insertion_sort(L, left, right)
    else:
        mid = (left + right) // 2
        left_half = L[left:mid]
        right_half = L[mid:right]

        merge_sort(left_half)
        merge_sort(right_half)

        merge(left_half, right_half, L)
    

def merge(left, right, list):
    """Merges the left half and the right half of a list"""
    i, j = 0, 0
    while i < len(left) and j < len(right): 
        if left[i] < right[j]:
            list[i+j] = left[i]
            i += 1
        else:
            list[i+j] = right[j]
            j += 1
    list[(i+j):] = left[i:] + right[j:]


def quick_sort(L, left=0, right=None, n=0, depth=0):
    """Sorts an inputed list with quick sort"""
    depth += 1
    if depth == 1: n = len(L)
    if depth > 3 * (log2(n) + 1): return merge_sort(L)

    if right is None: right = len(L)

    if right - left <= 1: return None

    pivot = right - 1
    i, j = left, pivot - 1

    while i < j:
        while L[i] < L[pivot]: i += 1
        while i < j and L[j] >= L[pivot]: j -= 1
        if i < j: L[i], L[j] = L[j], L[i]

    if L[i] >= L[pivot]:
        L[pivot], L[i] = L[i], L[pivot]
        pivot = i
    
    quick_sort(L, left, pivot, n, depth)
    quick_sort(L, pivot+1, right, n, depth)


def magic_sort(L): 
    """Sorts an inputed list with a certain sorting method based on the type of list that is inputed"""
    case = linear_scan(L)
    if case == 1: return L
    elif case == 2: return merge_sort(L)
    elif case == 3: return reverse_list(L)
    else: return quick_sort(L)