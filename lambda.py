#  lambda function
from functools import reduce

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

#All three of these methods expect a function object as the first argument. This function object can be a pre-defined method with a name (like def add(x,y)).

# Though, more often than not, functions passed to map(), filter(), and reduce() are the ones you'd use only once,
#  so there's often no point in defining a referenceable function.
# To avoid defining a new function for your different map()/filter()/reduce() needs - 
# a more elegant solution would be to use a short, disposable, anonymous function that you will only use once and never again - a lambda.

# filter() forms a new list that contains only elements that satisfy a certain condition, i.e. the function we passed returns True

print("filter-----------------")

# def func(n):
#     return n%2==0

num=[5,6,4,6,7,9,2,3]    

evens= list(filter(lambda n: n%2==0 ,num))

print(evens)

# def starts_with_A(s):
#     return s[0] == "A"

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(lambda s : s[0]=="A", fruit)

print(list(filter_object))

print("map-------------------")

#The map() function iterates through all items in the given iterable and executes the function we passed as an argument on each of them.
# change values, perform some function to list

num=[2,5,6,8,9]

double= list(map(lambda n: n*2, num))

print(double)

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
map_object = map(lambda s: s[0] == "A", fruit)

print(list(map_object))


print("reduce -------------------")
# reduce() works differently than map() and filter(). 
# It does not return a new list based on the function and iterable we've passed. Instead, it returns a single value.
# reduce() works by calling the function we passed for the first two items in the sequence.
#  The result returned by the function is used in another call to function alongside with the next (third in this case), element.
# This process repeats until we've gone through all the elements in the sequence.


# def add(x, y):
#     return x + y

nn = [2, 4, 7, 3]
sum=(reduce(lambda x,y: x+y, nn))

print(sum)



