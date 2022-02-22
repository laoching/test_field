p1 = [1, 2, 3]
p2 = [9, 8, 7]
name = ['a', 'b', 'c']
pl = list(zip(p1, p2))  # p1, p2의 동일한 인덱스 끼리 묶음
pt = tuple(zip(p1, p2, name))   # p1, p2, name의 동일한 인덱스 끼리 묶음
print(pl)
print(pt)