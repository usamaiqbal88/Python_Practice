from configparser import NoOptionError


print("Inheritance----------")

class Cars:
    def carmethod(self):
        print("This is parent class 'car' method.")
        None

class honda(Cars):

    def hondamethod(self):
        print("This is child class 'honda' method.")   
        None     

class toyota(Cars):

    def toyotamethod(self):
        print("This is child class 'toyota' method.") 
        None 

obj=honda()
obj2=toyota()

obj.carmethod()
obj2.carmethod()


print("\nMultiple inhertance---------------")

# A child can access two or more parents

class sedan:

    def sedanmethod(self):
        print("This is parent class 'sedan' method. ")
        None
class suv:

    def suvmethod(self):
        print("This is parent class 'suv' method. ")
        None

class mg(sedan,suv):

    def mgmethod(self):
        print("This is child class 'mg' method. ")
        None


obj3=mg()

obj3.sedanmethod()
obj3.suvmethod()
obj3.mgmethod()


print("\nMulti-level Inheritnce---------------------")

# child can be a parent class further

class Grandfather:
    def __init__(self,name):
        self.name=name

    def getname(self):
        return self.name
class father(Grandfather):
    def __init__(self, name, age):
        Grandfather.__init__(self,name)
        self.age=age

    def getage(self):
        return self.age

class son(father):
    def __init__(self, name, age, address):
        father.__init__(self,name, age)
        self.address=address

    def getaddress(self):
        return self.address

sons =son("Sam",22,"APK")
print(sons.getname(),sons.getage(),sons.getaddress() )

# print("Son is calling...")
# person=son()
# person.son_age()
# person.father_age()
# person.gf_age()

# print("Father is calling...")
# person2=father()

# person2.father_age()
# person2.gf_age()

print("\nHeirarchical Inheritnce---------------------")

# A parent have many childs

class Vehicle:

    # def __init__(self,type):
    #     self.type=type

    def vehicletype(self):
        print("This is a vehicle."  )
        None

class petrol(Vehicle):

    def petrolcar(self):
        print("This is petrol car.")   
        None

class hybrid(Vehicle):

    def hybridcar(self):
        print("This is hybrid car.")  
        None      
class electric(Vehicle):

    def electriccar(self):
        print("This is electric car.") 
        None

pcar=petrol()
pcar.petrolcar()
pcar.vehicletype()

hcar=hybrid()
hcar.hybridcar()
hcar.vehicletype()

ecar=electric()
ecar.electriccar()
ecar.vehicletype()


print("\nHybrid Inhertance")

#An inheritance is said hybrid inheritance if more than one type of inheritance is implemented in the same code. 
# This feature enables the user to utilize the feature of inheritance at its best. 
# This satisfies the requirement of implementing a code that needs multiple inheritances in implementation.

class A:
    def fun1(self):
        print("This is class A")
        None
class B(A):
    def fun2(self):
        print("This is class B")        
        None
class C(A):
    def fun3(self):
        print("This is class C")
        None
class D(C,A):
    def fun4(self):
        print("This is class D")
        None
fun = D()
fun.fun4()
fun.fun3()
fun.fun1()