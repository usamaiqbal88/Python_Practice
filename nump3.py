from __future__ import print_function
from asyncio.subprocess import SubprocessStreamProtocol
from gettext import npgettext
import numpy as np

aa1=np.array([[3,2,1],[6,5,4],[9,8,7]])
aa2=np.array([[2,1,3],[4,6,5],[7,9,8]])

print(aa1+aa2)              # adding arrays

# same for multiply, divide and Subtract

print(np.sqrt(aa1))            # taking square of every element

print("Sum of elements=",aa1.sum())

print("Maximum elements=",aa1.max())
print("Minimum elements=",aa1.min())

print(np.where(aa1>5))          # return undex with element greater than 5


import sys

parray=[3,5,7,9]
nmarray=np.array(parray)

print(sys.getsizeof(1)*len(parray))

print(nmarray.itemsize*nmarray.size)

# concatenate

a= np.array([1, 3, 5, 7])
b= np.array([0, 2, 4, 6])

print("a= ",a)
print("b= ",b)

c = np.concatenate((a,b))
print("a and b concatenate= ",c)

# stack()
# hstack()       along rows
# vstack()       along columns
# dstack()      along heights or depth

d = np.stack((a,b),axis=1)     # default axis is 0
print("a and b stack axis 1",d)

f = np.stack((a,b),axis=0)
print("a and b stack axis 0",f)

g = np.hstack((a,b))
print("a and b row stack",g)

h = np.vstack((a,b))
print("a and b column stack",h)

i = np.dstack((a,b))
print("a and b height stack",i)


# splitting
# the split() method will not adjust elements when elements are less in source.
# array_split() will split and less will go to last array

a= np.array([1, 3, 5, 7, 9])           # spillting by passing arguments

b = np.array_split(a,2)
print(b)

c = np.array([[1,2],[3,4],[5,6],[7,8],[9,0]])
d= np.array_split(c,3)
print(d)

print("------------------------")
# Search elements index
a= np.array([0, 2, 4, 6,8])
b= np.where(a==2)
print("Array= ",a)
print(b)

# searchsorted()
# return index where that value should e inserted to maintain the order
# also we can sort multiple values
# we can specify the side= right or left to search index

c= np.searchsorted(a,3)
print(f"The element should place at index {c} to maintain the order.")


# sort()
# sort the rows accordingly

a= np.array([0, 6, 9, 2, 4])     # 1-d sort
print("Array=",a)
b = np.sort(a)
print("After sorting",b)

c = np.array([[3,2,1],[6,5,4],[9,8,7]])   # 2-d sorting
print("2-D Array= ",c)
print("After sorting 2d=",np.sort(c))

print("--------------------------------")
# filter arrays
# getting elements from existing arrays

a= np.array([0, 6, 9, 2, 4])
b=[True,True,False,False,True]  

c= a[b]
print("True values= ",c)          # return true value, ignore false

d=np.array([10,11,12,13,14,15])

filter_array =  d>12     # create array from d with greater than 12 value
# filter_array =  d%2==0   # for even elements

newfilter= d[filter_array]
print("After filter, new array= ",newfilter)

# another method by iteration
ar= np.array([10,11,12,13,14,15])
filter_array = []

for e in ar:
    if e > 12:
        filter_array.append(True)
    else:
        filter_array.append(False)

newfilter= ar[filter_array]
print("After filter, new array= ",newfilter)             

