#!/usr/bin/python3 

import sys, os

# Give argument for command line
pyScriptName = sys.argv[0]
dataFileName = sys.argv[1]

# Read fasta file

fasta_dict = {}

with open(dataFileName, "r") as fasta_file:
    
    sequence_id = ""

    for line in fasta_file:
        if line.startswith(">"):
            sequence_id = line
            fasta_dict[sequence_id] = ""
        else:
            fasta_dict[sequence_id] += line.strip()

    # Compute GC
    for id in fasta_dict:
        testseq = fasta_dict[id]
        
        # calculate C
        C_count = testseq.count("C") 
    
        # calculate G
        G_count = testseq.count("G")

        # calculate the length of the sequence
        seq_length = len(testseq)

        # Calculate the GC percentage
        GC_percent = ((C_count + G_count) * 100) / float(seq_length)
        print(id)
        print(round(GC_percent, 6))
        
fasta_file.close()
