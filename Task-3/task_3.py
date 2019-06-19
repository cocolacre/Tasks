import numpy as np

#  for each half-hour interval we summarize 
# values from every cashbox.

# Let's assume files for cashboxes are called 1.txt, 2.txt and so on.
files = ['1.txt', '2.txt','3.txt','4.txt','5.txt']
data = []
for fl in files:
    with open(fl, 'r') as f:
        values = [int(x[:-1]) for x in f.readlines()]
        data.append(values)
sums = []
for ind, value in enumerate(data[0]):
    sums.append(data[0][ind]+data[1][ind]+data[2][ind]+data[3][ind]+data[4][ind])
m = max(sums)
max_intervals = [i for i, j in enumerate(sums) if j == m]
print(str(m)+ ': ' + str(max_intervals))