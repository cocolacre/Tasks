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
intervals = [
"08:30",
"09:00",
"09:30",
"10:00",
"10:30",
"11:00",
"11:30",
"12:00",
"12:30",
"13:00",
"13:30",
"14:00",
"14:30",
"15:00",
"15:30",
"16:00",
]
for interval in max_intervals:
    print(str(m)+ ' customers at ' + str(intervals[interval]))