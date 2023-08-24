from tkinter import N

# Simply speaking, a generator is a function that returns an object (iterator) which we can iterate over (one value at a time).
# yield statement pauses the function saving all its states and later continues from there on successive calls.\
# Once the function yields, the function is paused and the control is transferred to the caller.
# Local variables and their states are remembered between successive calls.
# Finally, when the function terminates, StopIteration is raised automatically on further calls.

print("Generators---------")

def gen():
    n=1
    print("1st iteration")
    yield n

    n += 1
    print("2nd iteration")
    yield n

    n += 1
    print("3rd iteration")
    yield n

a=gen()

print(next(a))    
print(next(a))    
print(next(a))    
# print(next(a))    


# for i in gen():
    # print(i)

print("fibonacci series-------")

def fib(limit):
     
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1
 
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
 
# Create a generator object
x = fib(5)
 
# Iterating over the generator object using next
print(next(x)) 
print(next(x))
print(next(x))
print(next(x))
print(next(x))
 
# Iterating over the generator object using for
# in loop.
print("\nUsing for in loop")
for i in fib(5): 
    print(i)    