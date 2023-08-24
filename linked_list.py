
class Node:
    
    def __init__(self):
        self.value=0
        self.next = None
        
one = None
two = None
three = None
head = None

one = Node()
two = Node()
three = Node()

one.value = 1
two.value = 2
three.value = 3

one.next= two
two.next = three
three.next = None

head = one

while(head!=None):
    print(head.value)
    head=head.next