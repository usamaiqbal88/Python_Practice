#operators

#    Arithmetic operators
from re import A


x=2
y=4

print("x+y=",x+y)
print("x-y=",x-y)
print("x*y=",x*y)
print("x/y=",x/y)
print("x**y=",x**y)
print("x%y=",x%y)
print("x // y=",x//y)  #ignore point value, return 

#     Assignment operators

a=2      
a += 3      # same for subtraction, mutliplication, division
print(a)


#   comparison operators

b=5
c=6
if(b==c):
    print("equal")
elif(b!=c):
    print("not equal")   
elif(b>c):
    print("B is greater")    
elif(b<c):
    print("C is greater")    
elif(b>=c):
    print("B is greater and equal")    
else:
    print("B is greater and equal")    

#         Logical Operators

if(b==c and b>c):
    print("equal and b greater")
if(b<c or b>c):
    print("equal")
if(not(b<c and b>c)):       #Reverse the result, returns False if the result is true
    print("not equal")

#     Identity Operators
print("Identity Operators")

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)   # returns True because z is the same object as x

print(x is y)   # returns False because x is not the same object as y, even if they have the same content

print(x is not y) # return true

#         Membership Operators

print("Membership Operators")

print("banana" in y)   # return true because y have banana
print("banana" not in y)   # return flase because y does not have banana

#          bitwise operators
