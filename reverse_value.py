
list = [10,20,30,40,50]
print("List = ",list)

start = 0
end = len(list)-1

while start < end: 
    list[start],list[end]= list[end],list[start]
    start += 1
    end -=1
    
print("Reversed list = ",list)    


# list.reverse()
# print("Again Reversed = ",list) 

list = [11,22,33,44,55]
r_list = []
l = len(list)
for i in range(l-1,-1,-1):
    r_list.append(list[i])
    
print("Reversed list 2 = ",r_list)