import unittest
from DNA_sequence import Sequence, DNA

class TestSequence(unittest.TestCase):

    def setUp(self):
        """Sets up sequences for further testing"""
        self.sequence1 = Sequence("ATGGAGGC")
    
    def test_get_sequence(self):
        """Tests if the correct sequence is returned by get_sequence"""
        self.assertEqual(self.sequence1.get_sequence(), "ATGGAGGC")
        print("get_sequence tests passed!")

    def test_calculate_length(self):
        """Tests if the length of the sequence is calculated correctly"""
        self.assertEqual(self.sequence1.calculate_length(), 8)
        print("calculate_length tests passed!")

    def test_count_nucleotides(self):
        """Tests if the right number of nucleotides are counted"""
        self.assertEqual(self.sequence1.count_nucleotides(), {'A': 2, 'T': 1, 'G': 4, 'C': 1})
        print("count_nucleotides test passed!")


class TestDNA(unittest.TestCase):
    
    def setUp(self):
        """Sets up DNA for further testing"""
        self.dna = DNA("ATGGAGGC")
    
    def test_reverse_complement(self):
        """Tests if the sequence is reversed correctly"""
        self.assertEqual(self.dna.reverse_complement(), "GCCTCCAT")
        print("reverse_complement tests passed!")
    
    def test_find_pattern(self):
        """Tests if the correct indices of the pattern are returned"""
        self.assertEqual(self.dna.find_pattern("GG"), [2, 5])
        print("find_pattern tests passed!")

    def test_calculate_gc_content(self):
        """Tests if the correct percentage of GC content is returned"""
        self.assertEqual(self.dna.calculate_gc_content(), 25)
        print("calculate_gc_content tests passed!")

unittest.main()