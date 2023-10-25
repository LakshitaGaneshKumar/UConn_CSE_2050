from solve_puzzle import solve_puzzle as puzzle
import unittest

class TestSolvePuzzle(unittest.TestCase):
        def testClockwise(self):
                """Tests a board solveable using only CW moves"""
                self.assertEqual(puzzle([3, 6, 4, 1, 3, 4, 2, 0]), True)
                print("CW Tests Completed.")

        def testCounterClockwise(self):
                """Tests a board solveable using only CCW moves"""
                self.assertEqual(puzzle([1, 2, 3, 4, 0]), True)
                print("CCW Tests Completed.")

        def testMixed(self):
                """Tests a board solveable using only a combination of CW and CCW moves"""
                self.assertEqual(puzzle([1, 2, 0]), True)
                print("Mixed Tests Completed.")
        
        def testUnsolveable(self):
                """Tests an unsolveable board"""
                self.assertEqual(puzzle([3, 4, 1, 2, 0]), False)
                print("Unsolvable Tests Completed.")


unittest.main()