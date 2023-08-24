
class A:
    def a_intro():
        print("Function of class A.")

class B(A):
    def b_intro():
        print("Function of class B.")
        
    # super().print()
    
class C(A):
    def c_intro():
        print("Function of class C.")
        
class D(B,C):
    def d_intro():
        # super().print()
        print("Function of class D.")
        pass

objd = D
objd.a_intro()
