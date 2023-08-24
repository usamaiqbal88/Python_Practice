

def increment(x):
    x = 6 
    return x


x=5
x=increment(x)
print(x)

class Num:
    def __init__(self,a,b):
        self.a = a
        self.b = b

class Num2:
    def __init__(self,a,b):
        self.a =a
        self.b =b
    
a_obj = Num(4,6)
b_obj = Num2(3,7)

a_obj=b_obj

print(a_obj.a, a_obj.b)
print(b_obj.a, b_obj.b)

print("--------------------------------------")

arr = [2,3,5,6,8,1,3]
n = len(arr)
middle =int(n/2)
if n % 2==0:
    print("even array.")

else:
    print (arr[middle])
    
print("------------------Manual Sort Array---------------------------")

arr = [6,8,2,9,10,9,13]
n = len(arr)

for i in range(0,n+1):    
    for j in range(i+1,n):
        if arr[i] >= arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
            print(arr[i],arr[j])
            
print(arr)


print("Instructor Destructor------------------------------------------")

class Employee:
    def __init__(self):
        print("Creating employee.")
        
    def __init_subclass__(cls):
        pass
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



print("----------------------Even/Odd-----------------")

def Check(n):
    n = n/2
    n = n*2
    return n

num = 7
print(Check(num))

arr = ["Even","Odd"]
n = 9
print(n%2)
print(arr[n%2])
       
       
print("------------0s and 1s----------------")

arr = [1,0,0,1,0,0,1]
n= len(arr)

# for i in range(n):
#     for j in range(i+1,n):
#         if arr[i]>arr[j]:
#             arr[i],arr[j]=arr[j],arr[i]
#             # print(arr[i],arr[j])
            
# print(arr)

for i in range(n):
    for j in range(i+1,n):
        if arr[i]==1 and arr[j]==0:
            arr[i],arr[j]=arr[j],arr[i]
            # print(arr[i],arr[j])
            
print(arr)

arr = [1,0,0,1,0]
n= len(arr)
j=0

while j < n-1:
    if arr[j] > arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp 
        j-=1 
    j+=1
    
print(arr)

print("-----------------------------------------")

arr = [2,3,5,7]
max = arr[0]

for i in arr:
    if i > max:
        max=arr[i]
        
print(max)


print("---------------sort----------------------------")

arr = [7, 8, 4, 5, 2, 9]
length = len(arr)
j = 0

while j < length - 1:
    if (arr[j] > arr[j + 1]):
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp
        j = -1
    j += 1

print("-------------------")

arr = [2,5,3,9]

min1 = float('-inf')
min2 = float('-inf')

for i in arr:
    if i > min1:
        min2 = min1
        min1 = i
        
    elif i > min2 and i!=min1:
        min2  = i
        
print(min2)

print("----------------------------------------")
# Python program to
# demonstrate stack implementation
# using list

stack = []

# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')

print('Initial stack')
print(stack)

# pop() function to pop
# element from stack in
# LIFO order
print('\nElements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print('\nStack after elements are popped:')
print(stack)

# uncommenting print(stack.pop())
# will cause an IndexError
# as the stack is now empty

   

print("----------------------------------------")

# Python program to
# demonstrate queue implementation
# using list

# Initializing a queue
queue = []

# Adding elements to the queue
queue.append('a')
queue.append('b')
queue.append('c')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty


print("---------------------------------------------------------")

class A:
    count  = 0
    
    def __init__(self):
        A.count += 1
        print(f"{A.count} object created.")
        
# print("pppp")
obj = A()
obj = A()


print("----------------------------------------------")

arr = [2,9,6,5,3,4]
target = 20
n = len(arr)-1

for i in range(0,n+1):
    for j in range(i+1,n+1):
        
        if arr[i]+arr[j]==target:
            print(arr[i],"and",arr[j])
            
print("-----------------------------------------------")

arr  = [2,4,5]
n = len(arr)
j = 0 
k=0
while(j<n):
    k = arr[j] + k
    j+=1
print(k)

print("-----------------------------------------------")

