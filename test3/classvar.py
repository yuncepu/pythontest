class TEST(object):
    a='1'
    pass
    def adda(self):
        self.a = 'a'

    def addb(self):
        self.b = 'b'

obj=TEST()
print(obj.a)
obj.adda()
print(obj.a)
#error:'TEST' object has no attribute 'b'
# print(obj.b)
obj.c='c'
print(obj.c)

print(TEST.a)
TEST.a = 'aa'
print(TEST.a)
print(obj.a)