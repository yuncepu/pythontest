import os
import luyu


def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_global()
    print("After global assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)

def filepath():
    print(__file__)

scope_test()
print("importtest.py:",os.getcwd())
filepath()
# luyu.module2test()
# luyu.module3filepath()
luyu.test()
luyu.filepath()
luyu.module2.test()
luyu.module2.filepath()
luyu.module3.test()
luyu.module3.filepath()
# luyu.module2.test()
# luyu.module2.filepath()
# luyu.module3.test()
# luyu.module3.filepath()
# luyu.module1.test()
# luyu.module1.filepath()
# module1.test()
# module1.filepath()
# scope_test()
# print("In global scope:", spam)