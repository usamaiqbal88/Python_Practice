
from abc import abstractmethod,ABC

class Sound(ABC):
    
    @abstractmethod
    def make_sound(self):
        pass

class Cat(Sound):
    def make_sound(self):
        print("Cat meow.")
        

class Dog(Sound):
    def make_sound(self):
        print("Dog bark.")
        

class Goat(Sound):
    def make_sound(self):
        print("Goat Sound.")
        
c = Cat()
c.make_sound()

d = Dog()
d.make_sound()

g = Goat()
g.make_sound()
