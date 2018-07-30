# class C(object):
#     def __new__(cls, *args, **kwargs):
#         obj = object.__new__(C, *args, **kwargs)
#         return obj
        
#     def __init__(self, *args, **kwargs):
#         print ("C Call __init__ from %s" %self.__class__)
        
# class A(C):
#     def __init__(self, *args, **kwargs):
#         print ("A Call __init__ from %s" %self.__class__)
    
#     def __new__(cls, *args, **kwargs):                       
#         obj = object.__new__(cls, *args, **kwargs)
#         print ("A Call __new__ for %s" %obj.__class__)
#         obj.__init__(args,kwargs)
#         return obj   

# class B(A):
#     def __init__(self, *args, **kwargs):
#         print ("B Call __init__ from %s" %self.__class__)
    
#     def __new__(cls, *args, **kwargs):
#         obj = object.__new__(A, *args, **kwargs)
#         print ("B Call __new__ for %s" %obj.__class__)
#         obj.__init__(args,kwargs)
#         return obj      

# #b = B()
# #print (type(b))

# class Parent(object):
#     fooValue = ("Hi, Parent foo value")
#     def foo(self):
#         print ("This is foo from Parent")
#         self.getfoo()

#     def getfoo(self):
#         print("this is parent getfoo")
        
# class Child(Parent):
#     fooValue = ("Hi, Child foo value")
#     def foo(self):
#         print ("This is foo from Child")
#         # use super to access Parent attribute
#         print (super(Child, self).fooValue)
#         super(Child, self).foo()
#         self.getfoo()
#         Parent.getfoo(self)
    
#     def getfoo(self):
#         print("this is child getfoo")


# c = Child()    
# c.foo()

class A:
    def __init__(self, member):
        self._member = member
        pass

    def getmember(self):
        result = self._member
        return result

class X(object):
    def __init__(self):
        self.member = 3
        pass
    pass

# if __name__ == '__main__':
#    d = D()
#    d.foo()

if __name__ == '__main__':
     a = A(1)
     print( a.getmember() )
     a1 = a.getmember()
     a1 = 2
     print( a.getmember())
     
     x = X()
     b = A(x)
     print(b.getmember().member)
     x1 = b.getmember()
     x1.member = 4
     print(b.getmember().member)



     pass
