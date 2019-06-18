import sys, os

try:
    import numpy as np
except Exception as _e:
    print(_e)
    import pip
    pip.main(['install', 'numpy'])
try:
    import numpy as np
except Exception as _e:
    print(str(_e))
    sys.exit()

#load data
data = []
if len(sys.argv) == 1:
    with open('data.txt', 'r') as f:
        data = f.readlines()
    data = np.array([int(item[:-1]) for item in data])
    #print(data)
elif len(sys.argv) == 2:
    datafile = sys.argv[1]
    with open(datafile, 'r') as f:
        data = f.readlines()
    data = np.array([int(item[:-1]) for item in data])
else:
    print('Too many arguments.')
    sys.exit()
# 90 percentile
print('90 percentile ' + str(np.percentile(data,90)))
print('median ' + str(np.percentile(data,50)))
print('average ' + str(np.average(data)))
print('max ' + str(np.max(data)))
print('min ' + str(np.min(data)))
