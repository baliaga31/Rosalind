#!/usr/bin/python

S1="GAGCCTACTAACGGGAT"
S2="CATCGTAATGACGGCCT"

if len(S1) == len(S2):

  Hamming_Distance = 0

# hamming_distance = [i for i in range(len(strand_a)) if strand_a[i] != strand_b[i]]

  for n in range(len(S1)):
    if S1[n] != S2[n]:
      Hamming_Distance += 1
      print(Hamming_Distance)
else:
  print("One sequence is too short or too long.")