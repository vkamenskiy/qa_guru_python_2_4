import copy

l = [1, 2, 3, ["abc", "def"]]

l2 = copy.deepcopy(l)

l2[0] = 10
l2[3][0] = "fake abc"

t = (1, 2, 3, 4, 5)
tt = t

