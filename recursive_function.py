def factorial(n):
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1

n = int(input('양의 정수 입력: '))
print(f'!의 값은 {factorial(n)}입니다.')