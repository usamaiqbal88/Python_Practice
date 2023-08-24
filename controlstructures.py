#conditional statemets

if(5>10):
    print("5 is greater")
elif(5>9):    
        print("5 is greater")
elif(5>7):    
        print("5 is greater")
elif(5>6):    
        print("5 is greater")
else:
    print("5 is smaller than all.")

 #loops

number = 3

for i in (1, 2, 3, 4):
     if i == number:
         print("Number found:", i)
         break
else:
     print("Number not found")    

# for i in (1, 2, 3, 4, 5):
#      if i == 3:
#         continue
#         print(i)      

for i in (1,2,3,4,6,7,8):
    print(i)           

for i in range(1, 5):
    for j in range(i):
        print(i, end=' ')
    print()

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)        

#while loop

count = 1
while count < 5:
     print(count)
     count = count + 1
     print("while loop")
else:
    print("The loop wasn't interrupted")     


#         for loops

print("for loop")

print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
 
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
 
# Iterating over a String
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)
 
# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))
 
# Iterating over a set
print("\nSet Iteration")
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i),

#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
  pass

for name in ('John', 'Kate'):
    print("Hello", name)
    
    
dics = {"name" :"sam","age":22}
dics["marks"]=20
for i in dics:
    print(i,dics[i])
