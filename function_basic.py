'''
매개 변수 n을 전달받는 abc라는 함수를 정의
def abc(n):
    aaaaa       # 함수 본체
    aaaaa       # 함수 본체
    return bbbb # 함수의 반환 값
'''

def max(a,b):
    if a > b:
        return a
    else:
        return b
    # 여러 개의 값을 리턴하기 위해서는 튜플을 사용한다.
    # return (a,b) if a < b else (b, a)
a1 = int(input('a: '))
b1 = int(input('b: '))
print(max(a1, b1))
# min, max = max(a1, b1)    튜플을 언팩하는 과정
# print(min, max)

