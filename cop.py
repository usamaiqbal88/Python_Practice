import copy


# Shallow Copy stores the references of objects to the original memory address.   	
# Deep copy stores copies of the object’s value.
# Shallow Copy reflects changes made to the new/copied object in the original object.	
# Deep copy doesn’t reflect changes made to the new/copied object in the original object.
# Shallow Copy stores the copy of the original object and points the references to the objects.	
# Deep copy stores the copy of the original object and recursively copies the objects as well.

# shallow copy creates copy of object but references each element of object
# deep copy creates a copy of the object and elements of the object


print("Shallow and Deep copy-------------")

li = [10,[20,25],30,40]

li2 = copy.copy(li)

print("After shallow copy.")
print("List 1=",li)
print("List 2=",li2)

# li.append(50)
# print("After Apending")

# print("List 1=",li)
# print("List 2=",li2)

li2[1][1]="a"
print("After replacing element")

print("List 1=",li)
print("List 2=",li2)

# li1 = [1, 2, [3,5], 4]
 
# using copy to shallow copy
# li2 = copy.copy(li1)
 
# # original elements of list
# print ("The original elements before shallow copying")
# print(li1)
# print(li2)
 
# print("\r")
 
# # adding and element to new list
# li2[2][0] = 7
 
# # checking if change is reflected
# print(li1)
# print(li2)


print("--------------------------------------")

li3= [2,4,6,8]

print("After deep copyimg")
li4=copy.deepcopy(li3)

print("List 3=",li3)
print("List 4=",li4)

li4.append(10)
print("After Apending")

print("List 3=",li3)
print("List 4=",li4)

li4[2]=5
print("After replacing element")

print("List 3=",li3)
print("List 4",li4)
