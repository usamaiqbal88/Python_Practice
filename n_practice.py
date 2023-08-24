print("Move n elements")

arr = [3, 4, 7, 2, 1, 6, 9, 5]
count = 3

for i in range(count):
    temp = arr[i]
    arr[i] = arr[count]
    arr[count] = temp
    i += 1
    count += 1

print(arr)

arr = [3, 4, 7, 2, 1, 6, 9, 5]
count = 5
n = len(arr)
for i in range(count):
    first_element = arr[0]
    for j in range(n-1):
        arr[j] = arr[j+1]
    arr[-1] = first_element


print(arr)

print("Two sum---------------------------------------")

# arr = [3,4,5,8,10]
# target = 2
# n = len(arr)
# for i in range(0,n):
#     for j in range(0,n):
#         if arr[i] + arr[j] == target:
#             print(arr[i], arr[j])
#             exit()
       
# print("No pair found.")
arr = [3, 4, 5, 8, 10]
target = 10
seen={}
for index,value in enumerate(arr):
    required = target - value
    if required in seen:
        print("Values are = ",index," and ",seen[required])
    else:
        seen[value]=index

arr = [3, 4, 5, 8, 10]
target = 15
seen = {}
for index, value in enumerate(arr):
    required = target - value
    if required in seen:
        print("Values are =", arr[seen[required]], "and", arr[index])
    else:
        seen[value] = index
    
print("sort array-----------------------------")

arr = [2,5,9,3,7,9]
n = len(arr)
i=0
while i < n-1:
    if arr[i]>arr[i+1]:
        temp = arr[i]
        arr[i]=arr[i+1]
        arr[i+1]= temp
        i=-1
    i+=1
    
print(arr)

print("4d to 1d array-----------------------------")

a = [2, 
       [2, 3], [4, 5, 
                [5, 6, 7, 8], [5, 4, 
                               [7, 4]
                               ]
                ]
       ]
# print(a[0])
# print(a[1][0],a[1][1])
# print(a[2][0],a[2][1])
# print(a[2][2])
# print(a[2][3])
# print(a[2][3][2])
new_list= []

def go(arr):
    for i in arr:
        if isinstance(i,list):
            go(i)
        else:
            new_list.append(i)

go(a)
print(new_list)

print("Search K element----------------------------------------------")

array = [2,4,5,7,8,9]
k = 7

for i in range(0,len(array)-1):
    if array[i]==k:
        print(f"The k is at {i} index.")
        
        
print("Move zeros to left.------------------------------------------")

array = [1,0,-4,-3,0,8,0,0,-2,7]
n = len(array)
i=0
while i< n-1:
    if array[i]!=0 and array[i+1]==0:
    # if array[i]>=0 and array[i+1]<0:
        temp = array[i]
        array[i] = array[i+1]
        array[i+1] = temp
        i = -1
    i += 1

print(array)

print("Peak elements-----------------------------------------")
array = [2,4,1,5,7,3]
n = len(array)
if n==1:
    print("No more than 1 element.")
if array[0]>array[1]:
    print(array[0])
if array[n-1]>array[n-1]:
    print(array[n-1])
for i in range(1,n-1):
    if array[i]>array[i-1] and array[i]>array[i+1]:
        print("Peak elements are:", array[i])
        
print("even/odd without loop------------------------------------")
n = 10
n = n%2
arr=['even','odd']
print(arr[n])

