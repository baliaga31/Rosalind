#!/usr/bin/env python

"""
    INI5: Working with Files Rosalind.info
"""

#open the file
f = open('texte2.txt', 'r')

#print a file
#file_content = f.readline()

#counter start at 0
sum  = 0

for line in f:
    if i%2 == 0:
        print line
    i += 1

print i    
