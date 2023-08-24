print("Polymorphism")

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()



print("----------------------------")  

class shape:

    def fact(self):
        print("This is a shape.")
        
class circle(shape):

    def fact(self):
        print("This is a circle.")

class square(shape):
    

    def fact(self):
        print("This is a square.")

cir=circle()
sqr=square()

cir.fact()
sqr.fact()


print("--------------------")

class Bird:
     def intro(self):
       print("There are different types of birds")
 
     def flight(self):
       print("Most of the birds can fly but some cannot")
 
class parrot(Bird):
     def flight(self):
       print("Parrots can fly")
 
class penguin(Bird):
     def flight(self):
       print("Penguins do not fly")
 
obj_bird = Bird()
obj_parr = parrot()
obj_peng = penguin()
 
obj_bird.intro()
obj_bird.flight()
 
obj_parr.intro()
obj_parr.flight()
 
obj_peng.intro()
obj_peng.flight()

# Operator Overloading
print("Operator Overloading-------------------------")

class A:
    def __init__(self,a):
        self.a= a 
        
    def __add__(self,other):
        return self.a+other.a
        
        
        
obj1 = A(2)        
obj2 = A(6) 
print(obj1+obj2)       

obj3 = "strong "
obj4 = "Weak"
print(obj3+obj4)
