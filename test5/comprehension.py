# (x*y for x in range(10) for y in range(x, x+10))
# {x*y for x in range(10) for y in range(x, x+10)}
# [x*y for x in range(10) for y in range(x, x+10)]



def gen(test):
    print("yield1")
    yield 111
    print("yield2")
    yield 222
    if test:
        print("yield3")
        yield 333
        pass
    else:
        print("yield4")
        yield 444
        pass

for iter in gen(1):
    print(iter)
for iter in gen(0):
    print(iter)

iter = gen(1) 


def echo(value=None):
    print("Execution starts when 'next()' is called for the first time.")
    a = True
    value = 100
    try:
        while True:
            try:
                if a:
                    print("a is true")
                    value = (yield value)
                    a = False
                else:
                    print("a is false")
                    value = (yield value)
                    a = True
            except Exception as e:
                value = e
    finally:
        print("Don't forget to clean up when 'close()' is called.")

