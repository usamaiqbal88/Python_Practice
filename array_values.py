print("Find Largest value in array--------------------------------")
list = [11,22,44,55,78,23,34]
max=list[0]
for i in list:
    if i>max:
        max = i

print("List = ",list)  
print("Max Number = ",max)

# min=list[0]
# for i in list:
#     if i<max:
#         max = i

# print("List = ",list)  
# print("Min Number = ",min)

# list.sort()
# print(list[-1])  

print("Find 2nd largest value in array------------------------")

list = [22,44,55,24,51,63,11,89,67]

list.sort()
print("List = ",list)
print("2nd largest value = ",list[-2])

print("Find 3nd largest value in array---------------------------")

list = [22,44,55,24,51,63,11,89,67]

list.sort()
print("List = ",list)
print("3rd largest value = ",list[-3])


print("Remove duplicate values---------------------------------------")

list = [12,34,56,78,12,35,23,56]

# list= set(list)    converted to set
# print(list)

unique_list=[]

for n in list:
    if n not in unique_list:
        unique_list.append(n)
        
print("Unique list =", unique_list )            
    
    
list = []    