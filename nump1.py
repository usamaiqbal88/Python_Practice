from re import M
import numpy as np

# Below is a list of all data types in NumPy and the characters used to represent them.

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )


# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
# The array object in NumPy is called ndarray
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

myarr = np.array([1, 2, 3, 4, 5])
# myarr = np.array([1, 2, 3, 4, 5],np.int16)

print(myarr)

print(myarr[2])            # access elements

myarr[0]=0                 # change elements
print(myarr)

print(np.__version__)      # display version

print(myarr.shape)         # rows and columns

print(myarr.dtype)         # display int64,  bits

# arrays  creation

# 1. conversion from python structures

listarr=np.array([[0,1,2,3,],[2,4,6,8],[4,5,7,9]])
print(listarr)   # dtype, shape, size

# 2. intinsic numpy array creation objects

zeros=np.zeros((2,3))          # create zero valued array with given rows and columns(row,coulmn)
print(zeros)

num= np.arange(10)            # craete numbers starting from 0 upto given argument range
print(num)

lp = np.linspace(1,10,7)      # create equivalent values from range, (range,range,no. of elements)
print(lp)                     # display equal spaces elements

emp=np.empty((3,3))           # create random valued array
print(emp)

ide= np.identity(5)           # create given argument matrix 
print(ide)                   # 5x5 matrix

ar= np.arange(30)            # creating 30 elements array 

ar=ar.reshape(3,10)          # reshape array intp given argument matrix
                            # elementsrequired for reshaping must be equal to both shapes
                            # reshape(-1)  is used to convert 2d to 1d.

print(ar)
ar=ar.ravel()                   # back to original shape 
print(ar)

#An array can have any number of dimensions.
# When the array is created, you can define the number of dimensions by using the ndmin argument.

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)




