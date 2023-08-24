

print("Collection Arrays")

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.

# un-order means when we display the elements of a set, it will come out in a random order. 
# Unindexed means, we cannot access the elements of a set using the indexes like we can do in list and tuples.


#     list

numbers=[10,20,30]           
numbers[2]=40
print(numbers)

mixed_types = ["Hello World", [4, 5, 6], False]
print(mixed_types[2])

new_list = numbers[0:2]               # new list from existing [starting index, final index]
print("new list", new_list)

print(mixed_types[1][2])              # inner items usi7ng multiple indices

# print(order ,new_list ,numbers)  #multiple outputs

numbers2=[50,100]
numbers2.append(200)                   #add item
numbers.insert(0,"numberlist")          #add item ( index, value )
numbers2.pop(1)                        # drop item
numbers2.extend([300,400])             # extend items
del mixed_types                       # delete list
print(numbers + numbers2)             # 2 list concatenate

# append()	adds an element to the end of the list
# extend()	adds all elements of a list to another list
# insert()	inserts an item at the defined index
# remove()	removes an item from the list
# pop()	returns and removes an element at the given index
# clear()	removes all items from the list
# index()	returns the index of the first matched item
# count()	returns the count of the number of items passed as an argument
# sort()	sort items in a list in ascending order
# reverse()	reverse the order of items in the list
# copy() 	returns a shallow copy of the list





#    tuples


fruits=("banana", "apple", "grapes")   # Tuple, cant change, static

print( fruits.count("apple"))
print(fruits.index("grapes"))

thistuple = ("apple", "banana", "cherry")
thislist = list(thistuple)
thislist.remove("apple")
thistuple = tuple(thislist)

#       dictionary

print("dictionary")

person={"name":"sam", "age":22, "degree":"IT"}   
person1=dict(name="sam", age=22, degree="IT")   #dictionary can by implemented by this method.

person["program"]="BS"        # add item
person.pop("program")

print(person)
print(person["degree"])  #specofic item

print(person.items())   # whole items
print(person.keys())    # keys
print(person.values())   # values


# clear() – Remove all the elements from the dictionary
# copy() – Returns a copy of the dictionary
# get() – Returns the value of specified key
# items() – Returns a list containing a tuple for each key value pair
# keys() – Returns a list containing dictionary’s keys
# pop() – Remove the element with specified key
# popitem() – Removes the last inserted key-value pair
# update() – Updates dictionary with specified key-value pairs
# values() – Returns a list of all the values of dictionary

# demo for all dictionary methods

 #        Set

id=set([22,44,77])  
 # id2={22,44,88}   # also a Set  removoes duplicate items 

id.add(99)            #add elements
id.discard(77)        # remove elements

print("id is", id)

primes = {2, 3, 5, 7}
evens = {2, 4, 6, 8}

primes.add(6) #add elemnts
primes.remove(6)  #remove elements

 # Union
print( primes | evens)

# Intersection
print( primes & evens)

# Difference
print( primes - evens)

# Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
 
# for d in Days:
#    print("Days:",d)

