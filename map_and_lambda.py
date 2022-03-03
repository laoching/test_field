def double(n):
    return 2 * n

x = [1, 2, 3, 4]
y = map(lambda n: 2 * n, x)
print(list(y))

'''
map(함수, 이터러블객체)
lambda 매개변수: 리턴 값

'''