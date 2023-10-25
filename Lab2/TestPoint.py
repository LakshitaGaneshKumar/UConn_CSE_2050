import unittest
from Point import Point # import class Point from file Point.py

class TestPoint(unittest.TestCase):
    def setUp(self):
        """Create some points for future tests"""
        self.p1 = Point(3, 4)
        self.p2 = Point(5, 6)
        self.p3 = Point(3, 4)
        self.p4 = Point(4, 3)

    def test_init(self):
        """Tests that points are initialied with the correct attributes"""  
        self.assertEqual(self.p1.x, 3)
        self.assertEqual(self.p1.y, 4)
        print("__init__ tests passed!")

    def test_eq(self):
        """Tests that points are compared correctly as equal or as not equal"""
        # Points p1:(3,4) and p3:(3,4) should compare as equal
        self.assertEqual(self.p1.__eq__(self.p3), True)
        # Points p1:(3,4) and p2:(5,6) should compare as NOT equal
        self.assertNotEqual(self.p1.__eq__(self.p2), True)
        print("__eq__ tests passed!")

    def test_equidistant(self):
        """Tests that points are compared correctly as equidistant from the origin or not"""
        # Points p1:(3,4) and p4:(4,3) should compare as equidistant from origin
        self.assertEqual(self.p1.equidistant(self.p4), True)
        # Points p1:(3,4) and p2:(5,6) should compare as NOT equidistant
        self.assertNotEqual(self.p1.equidistant(self.p2), True)
        print("equidistant tests passed!")

    def test_within(self):
        """Tests that points are compared correctly as within a given distance from each other or not"""
        # Points p1:(3,4) and p2:(5,6) are within 3 units of each other, so this should compare to True
        self.assertEqual(self.p1.within(3, self.p2), True)
        # Points p1:(3,4) and p2:(5,6) are within 3 units of each other, so this should NOT compare to True
        self.assertNotEqual(self.p1.within(1, self.p2), True)
        print("within tests passed!")

unittest.main() # This line tells unittest to 
                #    1) create an object for every untitest.TestCase class
                #    2) Run every method that begins with 'test' in those objects