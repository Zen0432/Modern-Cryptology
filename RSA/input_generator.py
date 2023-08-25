import numpy as np
import random
import sympy as sp
from numpy.linalg import matrix_rank
np.set_printoptions(threshold=np.inf)

mapping = {}
for i in range(16):
    num = '{:0>4}'.format(format(i,"b"))
    numi = int(num[3]) + 2*int(num[2]) + int(num[1])*4 + int(num[0])*8
    mapping[num] = chr(ord('f')+numi)

file = open("inputs_cleaned.txt","w+")
for i in range(8):
    for j in range(128):
        curr_ip_j = np.binary_repr(j, width=8)
        strr = 'ff'*i + mapping[curr_ip_j[:4]] + mapping[curr_ip_j[4:]] + 'ff'*(8-i-1)
        file.write(strr)
        file.write(" ")
    file.write("\n")
file.close()
