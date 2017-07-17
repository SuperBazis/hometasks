a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[]
lenA = len(a)
lenB = len(b)
for i in range(lenA):
    if (a[i] in b) & (not a[i] in c):
        c.append(a[i])
print(c)