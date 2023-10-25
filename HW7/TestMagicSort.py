import unittest
from MagicSort import linear_scan, reverse_list, insertion_sort, quick_sort, merge_sort,  magic_sort
from HelperFunctions import setUpN, fncs, test_sorting, random_list, sorted_list, o_1_unordered_lists, reversed_list


def check_list_sorting(method, reversed_list=False):
    """Tests that a given method sorts the list correctly"""
    ns = setUpN()
    list_fncs = fncs()

    for n in ns:
        for fnc in list_fncs:
            L, L_copy = test_sorting(n, fnc, method, reversed_list)
            assert L == L_copy
            assert len(L) == n


class Test_linear_scan(unittest.TestCase): 
    def setUp(self):
        """Sets up a collection of list sizes for further testing"""
        self.ns = setUpN()


    def test_case_0(self):
        """Tests Case 0, where the inputed list is not sorted, reversed, or have O(n) unsorted pairs"""
        for n in self.ns:
            L = random_list(n)
            self.assertEqual(linear_scan(L), 0)
        print("Linear Scan: Case 0 Tests Complete.")


    def test_case_1(self):
        """Tests Case 1, where the inputed list is sorted"""
        for n in self.ns:
            L = sorted_list(n)
            self.assertEqual(linear_scan(L), 1)
        print("Linear Scan: Case 1 Tests Complete.")
    

    def test_case_2(self):
        """Tests Case 2, where the inputed list has 10 items out of order at most"""
        for n in self.ns:
            Ls = o_1_unordered_lists(n)
            for L in Ls:
                self.assertEqual(linear_scan(L), 2)
        print("Linear Scan: Case 2 Tests Complete.")


    def test_case_3(self):
        """Tests Case 3, where the inputed list is a reveresed list"""
        for n in self.ns:
            L = reversed_list(n)
            self.assertEqual(linear_scan(L), 3)
        print("Linear Scan: Case 3 Tests Complete.")


class Test_reverse_list(unittest.TestCase): 
    def test_reverse(self):
        """Tests sorting of lists with reverse sort"""
        check_list_sorting(reverse_list, True)
        print("Reverse List: Tests Complete.")


class Test_insertionsort(unittest.TestCase):
    def test_insertion(self):
        """Tests sorting of lists with insertion sort"""
        check_list_sorting(insertion_sort)
        print("Insertion Sort: Tests Complete.")


class Test_mergesort(unittest.TestCase): 
    def test_merge_sort(self):
        """Tests sorting of lists with merge sort"""
        check_list_sorting(merge_sort)
        print("Merge Sort: Tests Complete.")


class Test_quicksort(unittest.TestCase): 
    def test_quick_sort(self):
        """Tests sorting of lists with quick sort"""
        check_list_sorting(quick_sort)
        print("Quick Sort: Tests Complete.")


class Test_magicsort(unittest.TestCase): 
    """Tests sorting of lists with magic sort"""
    def test_magic_sort(self):
        """Tests sorting of lists with quick sort"""
        check_list_sorting(magic_sort)
        print("Magic Sort: Tests Complete.") 


unittest.main()