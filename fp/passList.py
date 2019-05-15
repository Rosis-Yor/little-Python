inters = [4, 8, 6, 5, 2]
strins = ["zaz", "xex", "mim", "nun", "pyp"]
flos = [1.52, 8.32, 5.64, 3.15, 2.04]

def same(lies):
    return lies

print(same(inters))
print(same(strins))
print(same(flos))

def picA(li):
    return li[2]

print(picA(inters))
print(picA(strins))
print(picA(flos))

def prod(li):

    prodi = 1
    for els in li :

        prodi *= els

    return prodi

print(prod(inters))

def coni(li) :

    conc = ""
    for els in li :

        conc += " " + els

    return conc

print(coni(strins))

def quoti(li) :

    quo = li[2] ** 2

    for el in li :
        quo /= el

    return quo

print(quoti(flos))

def manip(li) :

    fs = li[2]
    li.append(fs)
    lo = li[2]
    li.remove(lo)
    li.insert(1, lo)
    ls  = li.pop()
    li.insert(0, ls)
    return li

print(manip(strins))