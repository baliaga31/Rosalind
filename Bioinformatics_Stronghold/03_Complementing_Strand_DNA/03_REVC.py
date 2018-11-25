#!/usr/bin/env python

"""
    Rosalind Python Exercice ID: REVC
    Exercice name: Complementing a Strand of DNA
    URL: http://rosalind.info/problems/revc
"""

# Constants
DNA = "AAAACCCGGT"
Complement = [['A','T'], ['C','G']]

# Fonctions

def complementing(sequence, cDNA):
    """
        blabla
    """

    for s in cDNA:
        onuc = s[0]
        nnuc = s[1]
        sequence = sequence.replace(onuc, nnuc)
        print("Sequence converted = " + sequence)
    print("Exit complementing()")
    return sequence

def reverse():
    return

# Main section
print("Initial sequence:")
print DNA

print("We complementing the sequence.")

new_cDNA = complementing(DNA, Complement)
print("Complemented sequence:")
print new_cDNA

print("Now, we reverse the sequence.")