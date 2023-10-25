import Cypher
import unittest


class TestCypher(unittest.TestCase):

    def setUp(self):
        """Sets up values for further testing"""
        self.msg = "Hi, my name is Ash"
        self.expected_out = "B!tj!fnbo!zn!-jIit"

        self.msgRand1 = "Hello, world."
        self.msgRand2 = "This is a message."
        self.msgRand3 = "This is a very random message...."

    def test_cypher_naive(self):
        """should shift letters + message appropriately"""
        self.assertEqual(Cypher.cypher_naive(self.msg, shift=1, offset=2), self.expected_out)
        print("Cypher-Naive Tests Passed.")

    def test_opt_provided(self):
        """should shift letters + message appropriately"""
        self.assertEqual(Cypher.cypher_opt(self.msg, shift=1, offset=2), self.expected_out)
        print("Cypher-Opt Tests Passed.")

    def test_opt_random(self):
        """Tests our optimized algorithm using the naive version"""
        self.assertEqual(Cypher.cypher_opt(self.msg, shift=1, offset=2), Cypher.cypher_naive(self.msg, shift=1, offset=2))
        self.assertEqual(Cypher.cypher_opt(self.msgRand1, shift=4, offset=5), Cypher.cypher_naive(self.msgRand1, shift=4, offset=5))
        self.assertEqual(Cypher.cypher_opt(self.msgRand2, shift=3, offset=4), Cypher.cypher_naive(self.msgRand2, shift=3, offset=4))
        self.assertEqual(Cypher.cypher_opt(self.msgRand3, shift=7, offset=8), Cypher.cypher_naive(self.msgRand3, shift=7, offset=8))
        print("Cypher-Random Tests Passed.")



if __name__ == '__main__':
    unittest.main()