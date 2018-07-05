#Q.1 - Create a numpy array with 10 elements of the shape(10,1) using np.random and find out the mean of the elements using basic numpy functions.

import numpy as np
a=np.random.random(10).reshape(10,1)
print(np.mean(a))

#Q.2 - Create a numpy array with 20 elements of the shape(20,1) using np.random find the variance and standard deviation of the elements.

import numpy as np
b=np.random.random(20).reshape(20,1)
print(np.nanvar(b))
print(np.std(b))

#Q.3 - Create a numpy array A of shape(10,20) and B of shape (20,25) using np.random. Print the matrix which is the matrix multiplication of A and B.
# The shape of the new matrix should be (10,25). Using basic numpy math functions only find the sum of all the elements of the new matrix.

import numpy as np
c=np.random.random((10,20))
d=np.random.random((20,25))
e=np.matmul(c,d)
print(e)
print(e.shape)
print(e.sum())

#Q.4 - Create a numpy array A of shape(10,1).Using the basic operations of the numpy array generate an array of shape(10,1) such that each element is the following function applied on each element of A.
#f(x)=1 / (1 + exp(-x))
#Apply this function to each element of A and print the new array holding the value the function returns
#Example:

#a=[a1,a2,a3]
#n(new array to be printed )=[ f(a1), f(a2), f(a3)]

import numpy as np
from math import *
x=np.full((10,1),2)
def f(x):
    return 1/(1+exp(-x))
f_v=np.vectorize(f)
sc=np.array(x)
n= f_v(sc)
print(n)