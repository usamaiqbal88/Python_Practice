print("Max increasing order.--------------------------------------------")

array = [1, 3, 6, 2, 5, 0]
count  = 1
max_count = 1

for i in range(1,len(array)):
    if array[i]>array[i-1]:
        count+=1
        print("Count is",count)
    else:
        if count>max_count:
            max_count=count
            count=1
        
print(max_count)

print("Max increasing sequence.--------------------------------------------")

# array = [0,1, 3, 6, 2, 5, 0]
# count = 1
# max_count = 1
# new=[]
# for i in range(1, len(array)):
#     if array[i] > array[i-1]:
#         if count>=max_count:
#             print(new.append(array[i]))
#         count+=1
#     else:
#         print(new)
#         if count > max_count:
#             max_count = count
#             count = 1
#     # if count > max_count:
#     #     print(new.append(array[i]))
# print(max_count)
# print(new)

print("count of elements.------------------------------------")

array = [2,3,6,4,9,7,3,9,9,4]
n = len(array)
dic = {}
for i in range(0,n):
    if array[i] not in dic:
        dic[array[i]] = 1
    else:
        dic[array[i]] += 1
        
print(dic.items())

print("Steps combination.---------------------------------")

steps = 3

def count(steps):
    if steps==1:
        return 1
    elif steps==2:
        return 2
    else:
        return count(steps-1) + count(steps-2)
    
print(count(steps))
    
print("Change denominations-------------------------------------------------")

print("integer to ROman----------------------------------------------------------")

# romans = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
# num = 12
# roman_numeral= ''
# for value,symbol in romans.items():
#     pass
# print(roman_numeral)

print("Balanced Binary Tree.-------------------------------------------------------")

tree = []

print("multiply matrices.----------------------------------------------------------")

m1 = [[3,6,4],
      [4,2,2]]

m2 = [[2,3,7],
      [1,4,3]]

print("Sum of duplicate number and missing number.-------------------------------------")

l = [1,2,3,3,5,6]
n = len(l)
d = {}
duplicate=None
missing=None

for i in range(0,n):
    if l[i] not in d:
        d[l[i]]= 1
    else:
        duplicate=l[i]
        d[l[i]]+=1
        
for i in range(0,n+1):
    if i not in d:
        missing = i
        
print(duplicate+missing)
    
print("Non-palindromic string count.----------------------------------------------------------")

string = "abcgkjdrba"
start=0
end= len(string)-1
count=0
while start < end:
    if string[start]==string[end]:
        count+=2    
    start+=1
    end-=1

non = len(string)-count
print(non)

print("Transpose of a matrix.----------------------------------------------------------------")

m = [[2,4,3],
     [5,3,1]]

rows = len(m)
columns = len(m[0])

# for i in range(0,len(m)):
    
    

