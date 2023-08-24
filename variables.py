# from xml.sax.saxutils import prepare_input_source


print("Welcome to Python.")
print(0)

#variable declaration

x= 20
y=25
y=26
x_1=30

if(x>y):
    print("x is greater")
else:
 print("y is greater.")   

 print(2<6) 

print( float(9))

print(9.2.is_integer())

print((10).bit_length())

order= "Go to Islama'bad"
print(f"order is {order}")
print(order.lower())
print(order.upper())

print("Happy" + " " + "programming!")

print(len("happy"))

name = "sam"
age = 22
print("My name is {0} and I'm {1} years old".format(name, age))
# print(f"My name is {name} and I'm {age}years old")

print(order[11])  #print specific character
print(order[5:11])  #print collection of character

h='''this 
       is 
       some 
       text'''
print(h)   

#reverse string

degree = "Bachelors"
print(degree[::-1])

uni="uog"

print("degree "+"of bachelors")


# Python is a strongly-typed dynamic language in which we don’t have to specify the data type of the function return value and function argument.
# It relates type with values instead of names. 
# The only way to specify data of specific types is by providing explicit datatypes while calling the functions.

def add(num1, num2):
    print("Datatype of num1 is ", type(num1))
    print("Datatype of num2 is ", type(num2))
    return num1 + num2
  
# calling the function without
# explicitly declaring the datatypes
print(add(2, 3))
  
# calling the function by explicitly
# defining the datatype as float
print(add(float(2), float(3)))