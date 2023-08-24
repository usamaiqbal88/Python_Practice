print("Numpy continued---------------")

from cgi import print_directory
import numpy as np

# axis

a= [[1,2,3],
[4,5,6],
[7,8,9]]
arr = np.array(a)

print(arr)
print("The sum along row axis ",arr.sum(axis=0))           # sum of elements on row axis
print("The sum along column axis ",arr.sum(axis=1))           # sum of elements on column axis

print("The transpose is=",arr.T)                       # transpose ( Row <-> column)

arr.flat                                           # print values by iteration
for item in arr.flat:
    print(item)
# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# for x in arr:
#   for y in x:
#     for z in y:
#       print(z)


print("Dimensions=",arr.ndim)
print("Size of this array=",arr.size)

print("The bytes consumed by arrasy=",arr.nbytes)

one= np.array([1,9,5,8])

print("Maximum value index=",one.argmax())              # return index with maximum value
print("Minimum value index=",one.argmin())              # return index with manimum value
print("Sort index=",one.argsort())                     # return sort index, to maximum indexes

aa=np.array([[3,2,1],[6,5,4],[9,8,7]])

print(aa)
print("Minimum value index=",aa.argmin())
print("Maximum value index=",aa.argmax())

print("Minimum value index along row axis=",aa.argmin(axis=0))          # by row axis
print("Maximum value index along column axis=",aa.argmax(axis=1))          # by column axis


# print("Sort index",aa.arg)

