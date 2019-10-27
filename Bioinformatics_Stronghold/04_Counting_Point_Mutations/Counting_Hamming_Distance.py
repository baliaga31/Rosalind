#!/usr/bin/python

S1="GAGCCTACTAACGGGAT"
S2="CATCGTAATGACGGCCT"

if len(S1) == len(S2):
  print("It's OK!")
else:
  print("One sequence is too short or too long.")