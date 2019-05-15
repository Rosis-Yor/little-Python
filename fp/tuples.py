tuple1 = (5.6, "California", True, 2)
tuple2 = 7, "Star Trek", 9.92, False

emptyTuple = ()

print(tuple1, tuple2, emptyTuple)

tupEx = (1, 2, 3, 4, 5)

print(tupEx[1])
print(tupEx[3])

f3 = tupEx[:3]
m3 = tupEx[1:4]
l3 = tupEx[2:]

print(f3, m3, l3)

list1 = [1, "mk", 45, "ij", "lp"]

tuple1 = 12, "uih", 1.23, "poi", True, list1

for els in list1 :
    print(els)

for its in tuple1:
    print(its)


empty = []
song = ""

for itis in tuple1 :
    empty.append(itis)

for elis in list1 :
    song += str(elis) + " "

print(empty)
print(song)