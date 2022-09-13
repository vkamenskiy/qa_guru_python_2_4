l = [1, 2, 3, 4, 5]
l[0]
l[0:4]
l[::-1]

ll = [1, 2, 3, "4", ["five", 12345]]
print(ll[4][1])


[1, 2, 3].append(2)
[1, 2, 3].extend([3, 2, 1])
a = [1, 2, 3].pop(0)

s = {1, 2, 3}
s2 = {3, 4, 5}

print(s & s2)
print(s | s2)

l = [1, 2, 3, 3, 4, 4, 5, 5, 6]
l= list(set(l))
print(l)



