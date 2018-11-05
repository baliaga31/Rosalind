f = open('rosalind_ini5.txt', 'r')

#print a file
#file_content = f.readline()

i = 1

for line in f:
    if i%2 == 0:
        print line
    i += 1
