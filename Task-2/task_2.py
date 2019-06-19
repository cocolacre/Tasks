import sys


#read polygon data
print(len(sys.argv))
if len(sys.argv) == 1:
    fname = 'data.txt'
elif len(sys.argv) == 2:
    fname = sys.argv[1]
print(fname)


poly = []
with open(fname, 'r') as f:
    for line in f.readlines():
        poly.append([float(item) for item in line.split(' ')])
print(poly)

x = float(input('X: '))
y = float(input('Y: '))
