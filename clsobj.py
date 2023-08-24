

from unicodedata import name

print("Class of car")

class car:
    # model = 2005
    # colour = "white"

    def __init__(self,model,colour):
        print("I am new object.")
        self.model=model
        self.colour=colour 

    def description(self):
        return "The car details are:",honda.model,honda.colour

    def __str__(self):
        return f"hiiii {self.model} {self.colour}"  
        
honda=car(2006,"blue")

# print(honda.colour,honda.model)
# print(honda.description())
print(honda)
print("----------------------------------------------------------------")
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name} is {self.age}"

p1 = Person("John", 36)

print(p1)

# del p1 delete an object

print("Class method------------------------------------------------------")

class fruit:

    # name = "Grape"
    @classmethod
    def fruitname(cls,name):
        print( "Fruit name is ", name)

# fruit.fruitname = classmethod(fruit.fruitname)
fruit.fruitname("grapess")


print("static methods------------------------------------------------")

# a static method can neither modify object state nor class state. 
# Static methods are restricted in what data they can access
# they’re primarily a way to namespace your methods.

class bike:

    @staticmethod
    def name():
        print ("The static method of bike class.")

obj=bike
obj.name()

print("------------------------------------------------------------")

class Grandfather:
    def __init__(self, name):
        self.name = name

    def getname(self):
        print("Grandfather ",self.name)

class Father(Grandfather):
    def __init__(self, name):
        # Grandfather.__init__(self, name)
        self.name = name

    def getname(self):
        print("Father ",self.name)

class Son(Father):
    def __init__(self, name):
        # father.__init__(self, name, age)
        self.name = name

    def getname(self):
        super().getname()
        print("Son ",self.name)

son1 = Son("sam")
father1 = Father("sam father")
gf1 = Grandfather("sam grandfather")

son1.getname()
father1.getname()
gf1.getname()
