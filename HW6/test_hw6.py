import hw6
import unittest

class test_hw6(unittest.TestCase):

    def setUp(self):
        """Initilizes list sizes and sorting methods for further testing"""
        self.ns = [10, 100, 200, 500, 1000, 2000, 5000]
        self.fncs = [hw6.bubble_sort, hw6.insertion_sort, hw6.selection_sort]


    def sort(self, list_type, list_func):
        """Tests a given type of list on all sorting methods of various sizes"""
        for n in self.ns:
            for fnc in self.fncs:
                # Create specified list
                self.L = list_func(n)         
                self.L_copy = self.L.copy()

                # Check initial conditions of list
                self.assertEqual(n, len(self.L))
                self.assertEqual(n, len(self.L_copy))

                # Call sorting method and Python's built-in sorting algorithm for further testing
                fnc(self.L)
                self.L_copy.sort()

                # Check final conditions for list
                self.assertEqual(self.L, self.L_copy)
                self.assertEqual(n, len(self.L))
                self.assertEqual(n, len(self.L_copy))

        print(f"All sorting methods work on a {list_type} list of sizes {self.ns}.")


    def test_random(self):
        """Tests randomly ordered lists"""
        self.sort("Random", hw6.random_list)
        
        
    def test_sorted(self):
        """Tests sorted lists"""
        self.sort("Sorted", hw6.sorted_list)


    def test_reverse(self):
        """Tests reversed lists"""
        self.sort("Revered", hw6.reversed_list)
    
    
    def test_front_to_end(self):
        """Tests a sorted list where 5% of the items in the front are moved to the end of the list"""
        self.sort("Front to End", hw6.front_to_end_list)
    
    
    def test_end_to_front(self):
        """Tests a sorted list where 5% of the items in the end are moved to the front of the list"""
        self.sort("End to Front", hw6.end_to_front_list)        



if __name__ == "__main__":  
    unittest.main()