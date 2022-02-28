import copy

x = [[1, 2, 3], [4, 5, 6]]
y = x.copy()    # 얇은 복사
b = copy.deepcopy(x)    # 깊은 복사(deep copy)
x[0][1] = 9
print(f'x =:{x}\n'
      f'y =:{y}\n'  # 얇은 복사는 복사 후에 원본이 바뀌면 똑같이 바뀜
      f'a =:{b}')   # 깊은 복사는 복사 후에 원본이 바뀌어도 변하지 않음

