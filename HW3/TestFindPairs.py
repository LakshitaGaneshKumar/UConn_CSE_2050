import unittest
import FindPairs
import random

class TestFindPairs(unittest.TestCase):
   
    def setUp(self):
        self.L1 = [1,2,3,4,5]
        self.L1_result = {(2,5), (3, 4)}

        self.L2 = [1, 1, 2, 3]
        self.L2_result = set()

    def test_find_pairs_naive(self):
        """thoroughly test find_pairs_naive"""
        self.assertEqual(FindPairs.find_pairs_naive(self.L1, 7), self.L1_result)
        self.assertEqual(FindPairs.find_pairs_naive(self.L2, 2), self.L2_result)
        self.assertEqual(FindPairs.find_pairs_naive(self.L2, 30), self.L2_result)
        self.assertEqual(FindPairs.find_pairs_naive(self.L2, 3), {(1, 2)})
        print("Find-Pairs-Naive Tests Passed.")


    def test_find_pairs_opt(self):
        """thoroughly tests find_pairs_opt"""
        self.assertEqual(FindPairs.find_pairs_opt(self.L1, 7), self.L1_result)
        self.assertEqual(FindPairs.find_pairs_opt(self.L2, 2), self.L2_result)
        self.assertEqual(FindPairs.find_pairs_opt(self.L2, 30), self.L2_result)
        self.assertEqual(FindPairs.find_pairs_opt(self.L2, 3), {(1, 2)})
        print("Find-Pairs-Opt Tests Passed.")

    def test_find_pairs_opt_random(self):
        """test find_pairs_opt() with a bunch of random numbers/targets using find_pairs_naive"""
        for i in range(2, 100):
            L = [j for j in range(i)]
            target = random.randint(1, 50)
            self.assertEqual(FindPairs.find_pairs_opt(L, target), FindPairs.find_pairs_naive(L, target))
        print("Find-Pairs-Opt-Random Tests Passed.")


if __name__ == '__main__':
    unittest.main()
