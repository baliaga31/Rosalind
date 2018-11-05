a = 4031
b = 8905

c = filter(lambda i: i % 2 == 1, range(a,b))
print c
d = sum (c)
print d
