
print("Function overloading and overriding-----")

# In the method overloading, methods or functions must have the same name and different signatures.	
# Whereas in the method overriding, methods or functions must have the same name and same signatures.
# 2.	Method overloading is a example of compile time polymorphism.	
# Whereas method overriding is a example of run time polymorphism.
# 3.	In the method overloading, inheritance may or may not be required.	
# Whereas in method overriding, inheritance always required.
# 4.	Method overloading is performed between methods within the class.	
# Whereas method overriding is done between parent class and child class methods.
# 5.	It is used in order to add more to the behavior of methods.
# 	Whereas it is used in order to change the behavior of exist methods.
# 6.	In method overloading, there is no need of more than one class.	Whereas in method overriding, there is need of at least of two classes.

class Car:
    def name(self):
        print("this is a car.")

class truck:
    def name(self):
        print("This is a truck.")        

c=Car()
t=truck()

c.name()
t.name()

print("-------------")

class brand:

    def name(self):
        print("this is a brand.")

    def brandtype(self):
        print("This is a clothes brand.")

class outfitter(brand):
    def name(self):
        print("This is outfitter brand.")   

class jj(brand):
    def name(self):
        print("This is Junaid Jamshed brand.")    

out=outfitter()
j=jj()

out.brandtype()
out.name()

j.brandtype()
j.name()

    