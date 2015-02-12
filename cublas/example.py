import numpy
from pycublas import CUBLASMatrix
A = CUBLASMatrix( numpy.mat([[1,2,3]],[[4,5,6]],numpy.float32) )
B = CUBLASMatrix( numpy.mat([[2,3]],[4,5],[[6,7]],numpy.float32) )
C = A*B
print C.np_mat()