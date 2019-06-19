#generate numbers for the first task.

import random
N = 100 #number of numbers to generate.
MAX = 9999 #maximum number.
with open('data.txt', 'a+') as f:
    for i in range(N):
        f.write(str(random.randint(0,MAX)) + '\n')
