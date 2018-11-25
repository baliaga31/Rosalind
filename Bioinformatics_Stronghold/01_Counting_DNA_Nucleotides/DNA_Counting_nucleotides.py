#!/usr/bin/env python

"""
    Rosalind Python Exercice ID: DNA
    Exercice name: Counting DNA Nucleotides
    URL: http://rosalind.info/problems/dna
"""

DNA = "ATCGGCCTCGTCCTCAACGCGCGGTTGCATTAGTGTTCGTGCCTTTCTGCTTGTGGTACCGTCTAATAAAACGCAAATACCTGCGTGGACAAAGTAGCTTGTACCACCCTCAGTAGCTAATTTTCATATTTCGCTAGACTCACGCCCCAACGGAGCATTAGTGTAAGAAATCAACAACGAGATCGTCTGGCTACATGGGAATACTTGCCTCTAAATGGGTATTAAAATGAACACTCACCGGATAGGCTGTTGTCGCCCTCTAAGCATGTGTCTAAAAGGAGCGGAACGCAGCCACCCGCGCTCTCTTAACAGCGACGTTCAACTACCCCCAGCTCCATTCTACTACGATTCGCGGATGACAAGGAACCGAGCCTTTTATTGGACATAGCTAGACTGACAATCTACCTCATCCTTGAATAGTTGCGATCCGGAATTTAATGAAGGACAACGGGATTATATATCTAACTAGTCGGACACTAAGCCTGAGGGGTCATCAGACTTTGTTCAACTACATCTCGCAACTTGACTGCGATCAAAGCAGGGGATATTCAATTCGCTTAAGGAGGACAACCGATTACTCCTTTATGTGGAGACAATGATGGCTAGGCAAATGGTCATGTAAGCGCTTCAGGGGCCAAGTGCAAAACTAGGGCACTAGTTAGATTCATTCGAACCCTCGCGACCGCGGCTTGCAGTCGGGGCGTGAGGGGGCATCCCGAAACCCTTTACATGGAATCGCTCAACTTAGATCTTGGCATTTCTCACTGGCGATTAAAGACAGCCACTCCGCGGGCATGTTTGATTCGCGCGTTGACGTCTTCTGGTGAGTATGTACGCCCCCAGTCGGGGCGGAAAGAGTGGGCAGCGTTCTGCGTTAGGAACATGAAGGCTAGCAGGCTTTAAAGAAGAATGATTGCC"

print DNA

#count the number of Adenine in DNA sequence
count_A = DNA.count("A")

#count the number of Adenine in DNA sequence
count_C = DNA.count("C")

#count the number of Adenine in DNA sequence
count_G = DNA.count("G")

#count the number of Adenine in DNA sequence
count_T = DNA.count("T")

print count_A, count_C, count_G, count_T