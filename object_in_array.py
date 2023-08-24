print("Store object in array--------------------------------------------------")

class Product:
    
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def get_price(self):
        return(self.price)

# drink = Product(50)
# egg = Product(20)
# lays = Product(40)

objects = []
# objects.append(drink.get_price())
# objects.append(egg.get_price())
# objects.append(lays.get_price())

# print(objects)
# objects.sort()
# print("Lowest Product Price = " ,objects[0])

objects.append(Product('apple',50))
objects.append(Product('mango',100))
objects.append(Product('apple',20))
print(objects)
min_price=1000
l_object=None
for object in objects:
    if object.name=="apple" and object.price<min_price:
        min_price=object.price
        l_object=object
        
print("The lowest product price is ",l_object.price ,l_object.name)

