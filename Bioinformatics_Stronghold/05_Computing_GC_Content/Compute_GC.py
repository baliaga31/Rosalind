#!/usr/bin/python

"""
This script will read fasta sequences and compute the GC percentage.
"""

__authors__ = ("Benoit Aliaga")
__contact__ = ("benoit.aliaga@umontpellier.fr")
__version__ = "0.0.1"
__date__ = "11/03/2019"

import sys, os

def ComputeGC_4(DNA):
    """ Computes the GC content of a DNA string of length 4.
    """

    counter = 0
    if DNA[0] == 'G' or DNA[0]=='C':
        counter = counter + 1
    

    return

# The main programm start here
if __name__ == "__main__":
    pass