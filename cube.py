import numpy as np 
a = np.array([[1,2,3],[4,5,6]]) 
print (a.shape)

##
a = np.arange(24) 
print (a)

# now reshape it  # r,row,col
b = a.reshape(2,4,3) 
print (b )
# b is having three dimensions


#K-Means Implementation in SciPy

from numpy import vstack,array
from numpy.random import rand

# data generation with three features
data = vstack((rand(100,3) + array([.5,.5,.5]),rand(100,3)))
print(data)


#
#Fast Fourier Transform
#Importing the fft and inverse fft functions from fftpackage
from scipy.fftpack import fft

#create an array with random n numbers
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

#Applying the fft function
y = fft(x)
print (y)


