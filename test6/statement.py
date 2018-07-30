x = [0, 1]
i = 0
i, x[i] = 1, 2 # i is updated, then x[i] is updated
print(x)


a = 1
def func():
    try:
        global a
        return print("returned"),2,a
    finally:
        a = 5
        print("finally")
        


a = func()
print(a)