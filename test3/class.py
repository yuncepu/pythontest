class Next:
  List = []

  def __init__(self,low,high) :
    self._List = []
    for Num in range(low,high) :
      self.List.append(Num ** 2)
      self._List.append(Num ** 2)

  def getList(self,Nu):
      return self.List[Nu]
  
  def get_List(self,Nu):
      return self._List[Nu]

  def __call__(self,Nu):
    return self.List[Nu]

a = Next(1,7)
print (a.List)
print (a(2))
print (a.get_List(2))
print (Next.List)

b = Next(7,10)
print (b.List)
print (b(2))
print (b.get_List(2))
