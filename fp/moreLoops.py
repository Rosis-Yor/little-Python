from random import randint

striExa = "myBeautifulString"

def strPrr(exa) :

    for v in range(len(exa)) :

        print(exa[v], end=" ")

strPrr(striExa)

dikiExa = {"rose" : 245, "green": 113, "milkblue": 142,
           "ye": 752,
           "or": 682,
           "lila": 427,
           "llil": 642}

def dikiPrr(diki) :

    for hd, em in diki.items() :

        print(f'{em:10} ==> {hd:30s}')

dikiPrr(dikiExa)


def zipet(tu, diki) :

    for mem, cp in zip(tu, diki) :

        print(mem + "*" + cp, end=" ")

zipet(striExa, dikiExa)

num = []

def fillLi() :

    numi = []
    l = randint(5, 12)
    print(l)

    for v in range(l) :

        numi.append(randint(4, 53))

        if numi[v] % 3 == 0 :
            print(" / ", end="")
        else:
            print(" + ", end="")

    return numi

num  = fillLi()

print(num)


