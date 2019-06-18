# lets generate cashbox data.
# there must be 17 values for each cashbox.
# 08:00 08:30 ... 16:00
import random
N = 5 #cashboxes amount.
M = 17 #measurements for each cashbox.
P = 10 #maximum visitors in line
for i in range(N):
    filename = str(i+1) + '.txt'
    with open(filename, 'w') as f:
        for j in range(M):
            data = random.randint(0,P)
            f.write(str(data) + '\n')
