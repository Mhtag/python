class A:
    classvar1 = 'I am a class variable in class A'
    def __init__(self):
        self.var1 = 'I am inside Class A constructor'
        self.classvar1 = 'Instance variable of class A'
        self.special = 'special'

class B(A):
    classvar1 = 'I am in class B'
    def __init__(self):
                                # Super is to call the Super class methods here
        self.var1 = 'I am inside Class B constructor'
        self.classvar1 = 'Instance variable of class B'
        super().__init__()
            

a = A()
b = B()

print(b.classvar1)

# Here the class B will search its construcor and look for classvar1.
# Then it will search Class A's constructor and look for classvar1.
# Then it will look at Class B variable to look for classvar1.
# then it will look at the Class variable of class A.
