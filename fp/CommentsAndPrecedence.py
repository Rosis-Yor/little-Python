"""

It is not read by the compiler
"""
comments = "Comments"
print(comments)

print(" ")

precedence = "Precedence of Operators"
print(precedence)

oper = 7 + 6 + 9 - 4 * ((9 - 2) ** 2) / 7

print(oper)

othOper = (6 % 4 * (7 + (7 + 2) * 3)) ** 2

print(othOper)

assert isinstance(othOper, int)
print(oper, othOper, precedence)