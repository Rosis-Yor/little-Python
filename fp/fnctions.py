def fnc():
    print(" Hello World")

fnc()

def single(a) :
    print(a)

single(9)

def mult(a, b, c) :
    d = a * b
    print(d + c)

mult(2, 3, 4)


def giver(a, b):
    c = a + b
    return c

print(giver(5, 2))

def taker(d, e):
    output = giver(d, e)
    return output

print(taker(1, 5))
