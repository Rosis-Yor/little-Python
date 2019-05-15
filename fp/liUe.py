strie = ["zaz", "xux", "cic", "mym", "pep", "mkm"]

def lister(li) :

    for v in range(0, len(li)) :

        print(li[v])

lister(strie)

strops = [

    ["xdx", "ftf", "kok", "lpl"],
    ["gyg", "huh", "jij", "bhb"],
    ["xcx", "klk", "uiu", "dfd"]
]

def listi(li) :

    em  = []
    for v in li:
        for b in v:
            em.append(b)

    return em

emi = listi(strops)

lister(emi)
print(strops)
print(emi)

first = range(5)
second = range(2, 9)
third =  range(3, 58, 7)

#print(first, second, third)
lister(first)
lister(second)
lister(third)