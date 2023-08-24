import numpy as np

print("Numpy-------------------")

# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
# The array object in NumPy is called ndarray
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
# Numpy array is a collection of similar data-types that are densely packed in memory. 
# A Python list can have different data-types, which puts lots of extra constraints while doing computation on it.
# Numpy is able to divide a task into multiple subtasks and process them parallelly.
# Numpy functions are implemented in C. Which again makes it faster compared to Python Lists.
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

a= [[[1,2,3],[3,4,5]],
     [[4,5,6],[6,7,8]]]

aa= np.array(a)
print(aa[1][1][2])

print("Dimensions= ",aa.ndim)                       # return 3 as 3d array

b= np.array([1,2,3,4,5],ndmin=5)    # 5D array
print(b)

c = np.array([1,2,3,4,5])
print(c[0:2])                        # slicing  [start,stop,step(2,1)]

d=np.array([[1,2,5],[6,8,9]])   
print("D array=",d[1,1:4])                       # 2d slicing

e=np.array([3,5,6,8,9],dtype="i")     # defining datatype in argument
print("dataype of e array= ",e.dtype)

f=np.array([1.2,4.5,6.7],dtype="f") 
print("F array",f)   
print("F array datatype= ")   
ff= f.astype("i")                   # changing datatype
print("New F array= ",ff)
print("Array after changing datatype float to integer= ",ff.dtype)

fff=ff.astype(bool)               # change to bolean
print("FFF array= ",fff)                        # false on 0, true on 1
print("ff datatype= ",fff.dtype)

# The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
# The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
# The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

ar = np.array([1, 2, 3, 4, 5])

x = ar.copy()
y = ar.view()

ar[0]=0

print(x)
print(y)

print(x.base)
print(y.base)

#Every NumPy array has the attribute base that returns None if the array owns the data.
# Otherwise, the base  attribute refers to the original object.


a1= np.array([1, 2, 3, 4, 5])
a2=np.array([[1,2,5],[6,8,9]]) 
a3= [[[1,2,3],[3,4,5]],
    [[4,5,6],[6,7,8]]]

print("Iterate array-----------")
print("1-d array elements= ")
for i in a1:                        # 1-D iterator
    print(i)

print("2-d array elements= ")
for i in a2: 
    for j in i:                       # 2-D iterator
        print(j)

print("3-d array elements= ")
for i in a3: 
    for j in i:
        for k  in j:                       # 3-D iterator
           print(k)

print(" By nditer() function.")             # shortcut itertor

for i in np.nditer(a3):
    print(i)

print("----------------------")












