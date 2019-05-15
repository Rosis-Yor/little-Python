fn = input("My first number : ")
sn = input(" My second number : ")

try :

    assert isinstance(fn, int)
    assert isinstance(sn, int)
    dev = int(fn) / int(sn)
    print(dev)

except ZeroDivisionError :

    print(" Why are You inputing 0 as second nuber ?")
    print(" We are dividing here !")
except TypeError :

    print(" Must be a num")

except AssertionError :

    print(" Must be an int")

except :

    print(" You are messing things up, ")
    print(" in a ways I cannot even suppose")