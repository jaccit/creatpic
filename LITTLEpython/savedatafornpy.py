import re
import numpy as np
origdata=open(r'C:\LITTLEpython\mixgasprinttxt.txt')
epoch='epoch'
lines=origdata.readlines()
A=[]
for line in lines:
    # print(line)
    if epoch in line:
        adddata=re.findall(r"\d+\.?\d*",line)
        # print(adddata)
        adddata = list(map(float, adddata))
        A.append(adddata)
        # print(A)
numpyarray=np.array(A)
np.save('fornp.npy',numpyarray)