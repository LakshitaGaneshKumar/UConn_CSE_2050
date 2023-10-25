import random

def setUpN():
    """Returns a list of numbers to be utilized as list sizes for further testing"""
    return [50, 100, 200, 500, 1000, 2000, 5000, 10000]


def fncs():
    """Returns a list of all the list-making functions in this file"""
    return [reversed_list, sorted_list, o_1_unordered_list_1, random_list, o_1_unordered_list_2, o_1_unordered_list_3]


def test_sorting(n, list_type, method, reversed_list=False):
    """
    Tests if a given sorting method works by taking in a list type and a sorting method,
    testing the sorting on two identical lists (one with the inputed sorting method and another 
    with the Python equivalent), and returning the two lists that are created
    """
    L = list_type(n)
    L_copy = L.copy()
    method(L)
    if reversed_list:
        L_copy.reverse()
    else:
        L_copy.sort()

    return L, L_copy


def random_list(n):
    """Returns a random list of size n"""
    L = [random.randint(0, 100) for i in range(n-1)]
    L.append(-1)
    return L


def sorted_list(n):
    """Returns a sorted list of size n"""
    L = [i for i in range(n)]
    return L


def o_1_unordered_list_1(n):
    """Returns a list where O(1) unordered items are at the end of the list"""
    L = [i for i in range(n-10)]
    for i in range(10): L.append(random.randint(0, n))
    return L


def o_1_unordered_list_2(n):
    """Returns a list where O(1) unordered items are at the beginning of the list"""
    L = [random.randint(n, n+100) for i in range(10)]
    for i in range(n-10): L.append(i)
    return L


def o_1_unordered_list_3(n):
    """Returns a list where O(1) unordered items are sprinkled throughout the list"""
    L = [i for i in range(n)]
    for i in range(10): L[(2+i) % n] = n+i
    return L


def o_1_unordered_lists(n):
    """Returns a list of three lists that have O(1) unordered items at the most"""
    Ls = []
    Ls.append(o_1_unordered_list_1(n))
    Ls.append(o_1_unordered_list_2(n))
    Ls.append(o_1_unordered_list_3(n))
    return Ls


def reversed_list(n):
    """Returns a reversed list of size n"""
    L = [i for i in range(n, 0, -1)]
    return L
