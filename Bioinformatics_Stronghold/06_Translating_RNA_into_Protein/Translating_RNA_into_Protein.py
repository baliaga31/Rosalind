#!/usr/bin/env python3

"""
    Rosalind Python Exercice ID: PROT
    Exercice name: Translating RNA into Protein
    URL: http://rosalind.info/problems/prot/
"""

__authors__ = ("Benoit Aliaga")
__contact__ = ("benoit.aliaga(at)umontpellier.fr")
__date__ = "12/17/2019"

import sys, os

# Give argument for command line
pyScriptName = sys.argv[0]
dataFileName = sys.argv[1]

# Read Fasta file

with open(dataFileName, "r") as sequence_file:

    sequence_id = ""

    for line in sequence_file:
        sequence_id += line
    
# Codon dictionary

Codon = {
    "AUG": "M", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUU": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUC": "F", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUA": "L", "CUG": "L", "GUG": "V",
    "UUG": "L", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCU": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCC": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCA": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UCG": "S", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAU": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAC": "Y", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UGU": "C", "CAG": "Q", "AAG": "K", "GAG": "E", 
    "UGC": "C", "CGU": "R", "AGU": "S", "GGU": "G", 
    "UGG": "W", "CGC": "R", "AGC": "S", "GGC": "G",
    "UAA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "UAG": "Stop", "CGG": "R", "AGG": "R", "GGG": "G",
    "UGA": "Stop"
}


def proteins(strand):
    protein=''
    for i in range(0, len(strand), 3):
        aa = Codon[strand[i:i+3]]
        if aa == "Stop":
            break
        protein += aa
    print(protein)

proteins(sequence_id)
