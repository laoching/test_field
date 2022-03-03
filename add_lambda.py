"""두 수의 합을 구하는 람다식"""

a = int(input('정수 a: '))
b = int(input('정수 b: '))

'''
만약 함수가 한번만 사용된다면 이름을 붙일 필요가 없음
add2 = lambda x, y: x + y
print(f'a와 b의 합은 {add2(a, b)}')
'''
print(f'a와 b의 합은 {(lambda x, y: x + y)(a, b)}')


'''
람다 사용법 -> lambda 매개변수: 리턴 값

lambda x, y: x + y는
def ~~(x, y):
    return x + y와 동일함
'''