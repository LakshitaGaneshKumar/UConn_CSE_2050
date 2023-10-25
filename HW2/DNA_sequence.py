class Sequence:
    
    def __init__(self, sequence):
        """Initializes a Sequence object"""
        self.sequence = sequence

    def get_sequence(self):
        """Returns the DNA sequence"""
        return self.sequence

    def calculate_length(self):
        """Calculate and return the length of the sequence"""
        return len(self.sequence)
    
    def count_nucleotides(self):
        """Count and return a dictionary that contains the number of each nucleotide(A, T, C, G) in the sequence"""
        # Create empty dictionary to store counts of nucleotides
        dictionary_nucleotides = {'A': 0, 'T': 0, 'C': 0, 'G': 0}

        # Iterate through each nucleotide in sequence
        for nucleotide in self.sequence:
            # Increase the count by one for each nucleotide found
            dictionary_nucleotides[nucleotide] += 1

        return dictionary_nucleotides

class DNA(Sequence):
    
    def __init__(self, sequence):
        super().__init__(sequence)
    
    def reverse_complement(self):
        """Returns the reverse complement of the DNA sequence. 
        The reversecomplement is obtained by reversing the sequence and replacing 
        each nucleotide with its complement(A with T, T with A, C with G, and G with C)"""
        # Create empty string for reversed sequence
        reversed_sequence = ""

        # Loop through each nucleotide in sequence and add its complement to the reversed_sequence
        for index in range(len(self.sequence) - 1, -1, -1):
            if self.sequence[index] == "A":
                reversed_sequence += ("T")
            elif self.sequence[index] == "T":
                reversed_sequence += ("A")
            elif self.sequence[index] == "C":
                reversed_sequence += ("G")
            elif self.sequence[index] == "G":
                reversed_sequence += ("C")

        return reversed_sequence

    def find_pattern(self, pattern):
        """Returns the starting indices of all occurrences of a given pattern in the DNA sequence"""
        pattern_len = len(pattern)
        indices_of_pattern = []

        # Loop through each index to determine if the pattern is found and add the starting index to the indices list
        for index in range(len(self.sequence)):
            if self.sequence[index:index + pattern_len] == pattern:
                indices_of_pattern.append(index)

        return indices_of_pattern

    def calculate_gc_content(self):
        """Calculates and returns the GC content of the DNA sequence as a percentage"""
        # Calculates the number of GC segments found in the sequence
        num_GCs = len(self.find_pattern("GC"))

        return round((((num_GCs * 2) / len(self.sequence)) * 100), 2)


if __name__ == "__main__":
    # Testing
    dna_sequence = "ATCCACGGATCAGGC"

    # Create an instance of the DNA class
    dna = DNA(dna_sequence)

    # Test the implemented methods
    seq_length = dna.calculate_length()
    count_nucleotid = dna.count_nucleotides()
    reverse_complement = dna.reverse_complement()
    pattern_indices = dna.find_pattern("GG")
    gc_content = dna.calculate_gc_content()

    print("Original sequence:", dna.get_sequence())
    print("sequence length: ", seq_length)
    print("sequence nucleotides: ", count_nucleotid)
    print("Reverse complement:", reverse_complement)
    print("Pattern indices:", pattern_indices)
    print("GC content:", gc_content)
