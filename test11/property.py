# @property 把一个方法 伪装成一个属性 
# 1.属性的值 是这个方法的返回值 
# 2.这个方法不能有参数了 
# 3.类不能调用，只能对象调用

class Person:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight
    @property
    def bmi(self):
        return self.weight / (self.height**2)

    @property
    def methdd(self):
        print("getter method")
    
    @methdd.deleter
    def methdd(self):
        print("delete methdd")
    
    @methdd.setter
    def methdd(self, Value):
        print("setter methdd")

per = Person("safly",1.73,75)
print(per.bmi)
per.methdd
print(Person.methdd)
print(type(Person.methdd))
#error:
per.methdd = 1
del per.methdd
##override methdd attribute, it seems that the old AAA is removed
Person.methdd =1
print(Person.methdd)
print(type(Person.methdd))



#######################################
class Foo:
    def __init__(self):
        self.bbb = None

    def get(self):
        print('get的时候运行我啊')
        return self.bbb

    def set(self,value):
        print('set的时候运行我啊',value)
        self.bbb = value

    def delet(self):
        print('delete的时候运行我啊')
        del self.bbb
        #def __init__(self, fget=None, fset=None, fdel=None, doc=None)
    AAA=property(get,set,delet) #内置property三个参数与get,set,delete一一对应

f1=Foo()
print(f1.AAA)
f1.AAA='aaa'
print(f1.AAA)
print(type(f1.AAA))
print(Foo.AAA)
print(type(Foo.AAA))
del f1.AAA
print(Foo.AAA)
print(type(Foo.AAA))
#del Foo.AAA
#if not del, AAA attribute is overrided (it seems that the old AAA is removed)
Foo.AAA = 'bbb'
print(Foo.AAA)
print(type(Foo.AAA))
print(f1.AAA)
print(type(f1.AAA))
#error:the instance f1 has no attribute AAA
#del f1.AAA
del Foo.AAA