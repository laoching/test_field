import random

# 인수가 없는 함수 선언
def confirm_retry():
    '''한 번 더 할 것인지'''
    while True:
        n = int(input('한 번 더?<yes: 1 / No: 0>: '))
        if n == 0 or n == 1:
            return n
print('암산 연습 시작')

while True:
    x = random.randint(100, 900)
    y = random.randint(100, 900)
    z = random.randint(100, 900)

    while True:
        print(f'{x} + {y} + {z} = ', end=' ')
        answer = int(input())
        if answer == x + y + z:
            break
        print("wrong answer!")
    # 함수의 반환이 1이 아니면 break
    if not confirm_retry():
        break