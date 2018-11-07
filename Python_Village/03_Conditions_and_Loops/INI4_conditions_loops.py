#!/usr/bin/env python

"""
    INI4: Conditions and Loops Rosalind.info
"""

#variables
a = 4941
b = 9894

#counter start at 0
sum = 0

#loop for calculate the odd number between a and b
for i in range (a, b+1):
    if i % 2 ==1:
        sum+=i

print (sum)