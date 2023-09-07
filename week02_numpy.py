import numpy as np
import random

#v = np.array([1,3,-9,2])
#v = np.array ([1,3,-9,2], dtype= 'int64')
#v = np.array([[1,3,-9,2],[71,13,-22,7]])#, dtype='int64')
#print(v.ndim, v.shape, v.data, v.dtype, v.strides)

a = int(input())

lst = list()

for i in range(a):
    lst.append(random.randint(1,100))

v=np.array(lst,dtype='int16')


print(lst)

print(v.ndim, v.shape, v.data, v.dtype, v.strides)