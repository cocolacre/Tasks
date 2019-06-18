import sys, os
data = []


#if there is no numpy module installed - let's try installing it.
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
    #we could not install or import numpy. So - exiting.
    sys.exit()

#if we do not pass data file as argument - let's try and read data.txt
#within the same folder
if len(sys.argv) == 1: 
    with open('data.txt', 'r') as f:
        data = f.readlines()
    data = np.array([int(item[:-1]) for item in data])

#if we pass data file as argument:
elif len(sys.argv) == 2:
    datafile = sys.argv[1]
    with open(datafile, 'r') as f:
        data = f.readlines()
    data = np.array([int(item[:-1]) for item in data])
#if there are too many arguments passed - exit.
else:
    print('Too many arguments.')
    sys.exit()

#make desired output:
print('90 percentile ' + str(np.percentile(data,90)))
print('median ' + str(np.percentile(data,50)))
print('average ' + str(np.average(data)))
print('max ' + str(np.max(data)))
print('min ' + str(np.min(data)))
