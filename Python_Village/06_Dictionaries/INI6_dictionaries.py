#!/usr/bin/env python

"""
    INI6: Dictionaries Rosalind.info
"""

# Open the files
f = open('dic_test.txt', 'r')

print f.read()

for word in str.split(' '):
    print word

dic = {}

for key, value in dict.items():
    print key
    print value

