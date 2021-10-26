class A:
    def method(self):
        print('This is the mehod from class A')

class B(A):
    def method(self):
        print('This is the mehod from class B')


class C(A):
    pass


class D(B,C):
    pass


a = A()
b = B()
c = C()
d = D()

d.method()