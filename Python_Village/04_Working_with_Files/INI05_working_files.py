#!/usr/bin/env python

"""
    INI5: Working with Files Rosalind.info
"""

# Open the Files
f = open('rosalind_ini5.txt','r')

# On commence avec la premier ligne qui est impaire.
# Python commence a compter a partir de 0.
# Probleme, ca risque de tout decaler. Donc on met 1 comme premiere valeur.
i = 1

# loop
for line in f:
    # Si la ligne est paire, elle est egale a 0. Alors on peut l'afficher.
    if i%2 == 0:
        print line
    i += 1
