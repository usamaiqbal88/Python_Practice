print("-------Linked List Creation---------------")

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList:
    
    def __init__(self):
        self.head = None
        
    def push1(self,data):
        new_node= Node(data)
        new_node.next=self.head
        self.head = new_node
        
    def print(self):
        value = self.head
        while value != None:
            print(value.data)
            value = value.next
    def push(self,data):
        new_node = Node(data)
        last = self.head
        while last.next !=None:
            last = last.next
        last.next = new_node
            
    # def b_push(self,prev_node,data):
    #     new_node = Node(data)
    #     new_node.next = prev_node.next
    #     prev_node.next = new_node
    def reverse(self):
        print("Reverse-")
        Prev = self.head.next
        Current = self.head
        self.head.next = None
        
        while(Current is not None):
            Prev.next = Current
            Current = Prev
            Prev = Prev.next
            # Next = Current.next
            # Current.next = Prev
            # Prev = Current
            # Current = Next
        self.head = Prev
          
    def delete(self,P):
        current  = self.head
        
                
        
one = Node(4)
two = Node(2)
one.next=two
two.next= None
head = one

ll = LinkedList()
ll.head=one

print("-------Linked List Insertion---------------")

ll.push(7)

zero = Node(0)
ll.head = zero
zero.next=one

# ll.b_push(4,9)

ll.print()

ll.reverse()
        
ll.print()