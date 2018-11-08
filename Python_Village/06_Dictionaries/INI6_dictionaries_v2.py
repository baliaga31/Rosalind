#!/usr/bin/env python

"""
    INI6: Dictionaries Rosalind.info
"""

# Open the files
data = open('dic_test.txt', 'r')
print data.read()

# Separate the words in the file
words = data.read().strip().split()
print words

# Create a dictionnary
dict = {}

# Count the word in the file
for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1

for word in dict:
    print word + " " + str(dict[word])


with open('Correction_benoit.txt', 'w') as output_data:
    output_data.write(''.join(word_count))