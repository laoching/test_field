def gugu(func):
    """9행 9열의 표를 출력"""
    for i in range(1, 10):
        for j in range(1, 10):
            print(f'{func(i, j)}', end='')  # gugu(mul2)라면 func(i, j) = mul2(i, j)와 동일
        print()                             # gugu(add2)라면 func(i, j) = add2(i, j)와 동일
        
def mul2(x, y):
    return x * y

def add2(x, y):
    return x + y

n = int(input('곱셈[0] / 덧셈[1]: '))

if n == 0:
    print('9행 9열의 곱셈 표')
    gugu(mul2)
elif n == 1:
    print('9행 9열의 덧셈 표')
    gugu(add2)