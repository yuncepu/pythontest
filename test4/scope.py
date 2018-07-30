def myfunc(a):
    print(a)

class A:
    a = 42
    def print(self):
        b = list(self.a + i for i in range(10))
        print("A init b:",b)
        c = list(A.a + i for i in range(10))
        print("A init c:",c)
    def setInstanceVar(self, value):
        self.a = value
    def selfMethod(self):
        return self.print
    def classMethod(self):
        return A.print
    def userfunc(self):
        return myfunc
    def test():
        print("test")
c = 1
class B:
    e = 42
    # d = list(B.e + i for i in range(9)) #error
    # print(d)
    # d = list(e + i for i in range(9)) #error
    # print(d)

a = A()
a.print()
print("a.a:",a.a)
print("A.a:",A.a)
a.setInstanceVar(1)
print("after setclassvar a.a:",a.a)
print("after setclassvar A.a:",A.a)
a.print()
selfmethod = a.selfMethod()
classme = a.classMethod()
func = a.userfunc()
selfmethod()
b = A()
b.a = 3
classme(b)
func(1)
A.test()
a.func1 = A.test
a.func1()



