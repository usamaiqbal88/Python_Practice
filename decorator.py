print("Decorators-----------")

# change the behavior of function

def decfunc(func):
    def message():
        print("This is a message.")
        func()
        print("Message ended.")

    return message

# @decfunc             
def text():
    print("How are you?")

text= decfunc(text)         # creating a decorator
text()

print("-------------------hhhhhhhhhhhh---------------------------------------------------------------")

def hello_decorator(func):
 
    def inner1():
        print("Hello, this is before function execution")

        func()
 
        print("This is after function execution")
         
    return inner1
 
@hello_decorator
def function_to_be_used():
    print("This is inside the function !!")
 
# function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()

print("------------------------")
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

# ordinary= make_pretty(ordinary)
ordinary()

print("----------------")

def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)

divide(4,2)    