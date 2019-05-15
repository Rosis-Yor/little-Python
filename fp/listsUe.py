el4L = ["ax", "ad", "at", "aj"]

l3 = [2, 5 , 6]

l5 = ["stri", 5, "str5", True, 1.52]

print(el4L, l3, l5)

num1 = l3.index(5)
booln = l5.index(True)

print(num1, booln)


l4 = [1, 2, 3]
l4.append(8)
l4[1] = 5
l4[0] = 6
print(l4)

l7 = ["az", "as", "af", "ar", "au", "ak", "ah"]

l7sli1 =l7[:5]
l7sli2 = l7[2:6]
l7sli3 = l7[3:]
print(l7)
print(l7sli1)
print(l7sli2)
print(l7sli3)

inxAr = l7.index("ar")
l7.insert(inxAr, "ay")
print(l7)