from turtle import shape


print("Static variables and methods--------------")

# a static variable is defined inside a class and outside the class methods.

# Static variable and methods are used when we want to define some behaviour or property specific to the class
# And which is something common for all the class objects.
# for a static method we don't provide the argument self because static methods don't operate on objects.

# a static method can neither modify object state nor class state. 
# Static methods are restricted in what data they can access.
# they’re primarily a way to namespace your methods.

class Shape:

    NAME="square"   #static variable
    
    @staticmethod
    def info():
        print("This class is used for representing different shapes.")

# Shape.info = staticmethod(Shape.info)

Shape.info()

s=Shape

print(s.NAME)





