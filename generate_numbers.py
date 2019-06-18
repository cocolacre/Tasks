#generate numbers 
import random
N = 100
MAX = 9999
with open('data.txt', 'a+') as f:
    for i in range(N):
        f.write(str(random.randint(0,MAX)) + '\n')
