# Functions
def message():
    print("This is message.")
    None

message()    

def calculate(num1,num2):
    x=num1+num2
    return x

a=5
b=3
print(calculate(a,b))


# partial function
print("\nPartial functions----")

from functools import partial

def add(a, b, c):
    return 100 * a + b, c
  
pfunction = partial(add, 2,1)
  
print( pfunction(5) )


def email(id,domain,extension):
    return id+domain+extension

pfunc = partial(email,"sam","@gmail")
print( pfunc(".com") )

pfunc = partial(email,"sammmm","@gmail")
print( pfunc(".com") )

#Partial functions can be used to derive specialized functions from general functions and therefore help us to reuse our code.



#  lambda function

print("\nlambda function")

#A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
# Lambda functions reduce the number of lines of code when compared to normal python function defined using def keyword. 
# But this is not exactly true because, even functions defined with def can be defined in one single line. 
# But generally, def functions are written in more than 1 line.
# They are generally used when a function is needed temporarily for a short period of time,
#  often to be used inside another function such as filter, map and reduce.
# Using lambda function, you can define a function and call it immediately at the end of definition. 
# This can’t be done with def functions.

func = lambda a : a*a

print(func(5))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(3)
mytripler = myfunc(4)

print(mydoubler(11))
print(mytripler(11))

# Use lambda functions when an anonymous function is required for a short period of time.


#  recursive functions

print("\nrecursive functions")

# function calling itself

def factorial(n):
    if(n==1):
        return 1
    else:
        # print(n)
        s= n * factorial(n-1)   # factorial caling itself
        # print(s)
        return s

print("Factorial is ",factorial(5))        

def backsum(n):
    if(n>0):
        s = n + backsum(n-1)
        return s
    else:
        return 0

print("backsum is ", backsum(5))            

def fibonacci(n):
    print(n)
    if(n==0):
        return 0
    elif(n==1):
        return 1    
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("fibonacci = ", fibonacci(0))            

#   Monkey patch functions

# replace function
# object behavior changes during run time.

print("\nmonkey functions")

class A:
    def message():
        print("Class Message.")
                                       #change the behavior of code at run-time.
def message2():
    print("Message  outside class.")

A.message= message2                # calling outside class function  by the class object. 
obj=A()

A.message()


class B:
    def square(self,n):
        print("Square of number is ",n**2)

def cube(self,n):
            print("Cube of number is ",n**3)

B.square=cube               # cube is not class function
obj2=B()

obj2.square(4)
