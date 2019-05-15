lc1 = [num for num in range(8, -2, -2)]

lc2 = [num**num for num in range(2, 5)]

lc3 = [num**2 - 1 for num in range(4, 8)]

lc4 = [num for num in range(2, 9) if num < 5 or num > 6]

lc5 = [num for num in range(10, 0, -1) if num > 7 or num < 4]

lc6 = [num for num in range(1, 11) if num != 2 and num != 3
       and num != 7 and num != 8]

print(lc1)
print(lc2)
print(lc3)
print(lc4)
print(lc5)
print(lc6)