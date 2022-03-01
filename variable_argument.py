# *num은 0 이상의 임의의 정수를 입력받는다.
# *num은 튜플이기 때문에 여러개의 입력을 받을 수 있고 이를 가변 인수(arbitray argument)라고 함

def max2more(a, b, *num):
    '''두 개 이상의 값 중 최댓값 구하기'''
    max = a if a > b else b
    for n in num:
        if n > max:
            max = n
    return max

print(f'(1, 2): {max(1, 2)}')
print(f'(1, 2, 3): {max(1, 2, 3)}')
print(f'(1, 2, 3, 4, 5): {max(1, 2, 3, 4, 5)}') # 이 경우 a=1, b=2, num=(3, 4, 5)

# b에 해당하는 argument가 없음 -> error 발생
print(f'(1): {max(1)}')
