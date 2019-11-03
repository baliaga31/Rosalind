#!/usr/bin/python

"""
This script will read fasta sequences and compute the GC percentage.
"""

__authors__ = ("Benoit Aliaga")
__contact__ = ("benoit.aliaga@umontpellier.fr")
__version__ = "0.0.1"
__date__ = "10/27/2019"

import sys, os

def ReadFastaFile(dataFileName):
    """
        This function reads a fasta file.
    """

    # Open fasta file
    f = open(dataFileName, 'r')

    sequences = []
    seq = ''

    # Read fasta file
    for line in f:
        if line.startswith('>'):
            if seq:
                sequences.append(seq)
            seq = ''
        else:
            seq += line.rstrip()

    if seq:
        sequences.append(seq)

    f.close()

    return(sequences)

def ComputeGC():
    """
        This function computes a GC % in each sequences in a fasta file.
    """
    pass

if __name__ == "__main__": # The main programm start here
    
    # Give argument for command line
    pyScriptName = sys.argv[0] # Argument for the script name
    dataFileName = sys.argv[1] # Argument for input file

    # Read the fasta file
    ReadFastaFile(dataFileName)

    # Compute GC percentages
    ComputeGC()