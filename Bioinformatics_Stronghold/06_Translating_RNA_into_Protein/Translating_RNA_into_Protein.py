#!/usr/bin/env python3

"""
    Rosalind Python Exercice ID: PROT
    Exercice name: Translating RNA into Protein
    URL: http://rosalind.info/problems/prot/
"""

__authors__ = ("Benoit Aliaga")
__contact__ = ("benoit-aliaga(at)orange.fr")
__version__ = "0.0.1"
__date__ = "12/17/2019"

# Codon dictionary

Codon = {
    "AUG": "Methionine",
    "UUU": "Phenylalanine",
    "UUC": "Phynylalanine",
    "UUA": "Leucine",
    "UUG": "Leucine",
    "UCU": "Serine",
    "UCC": "Serine",
    "UCA": "Serine",
    "UCG": "Serine",
    "UAU": "Tyrosine",
    "UAC": "Tyrosine",
    "UGU": "Cysteine",
    "UGC": "Cysteine",
    "UGG": "Tryptophan",
    "UAA": "STOP",
    "UAG": "STOP",
    "UGA": "STOP"
}

def proteins(strand):
    protein=[]
    for i in range(0, len(strand), 3):
        aa = Codon[strand[i:i+3]]
        protein.append(aa)
    print(protein)

ARN="AUGUUUUCUUAAAUG"

proteins(ARN)