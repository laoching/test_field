a, b, c = 1, 2, 3

print(f'a = {a}, b = {b}, c = {c}')
print(f'{a} + {b} + {c} = {a + b + c}')
print()
n = 123456
print(f'n = {n:4}')
print(f'n = {n:6}')
print(f'n = ({n:b})2')  # 2진수
print(f'n = ({n:o})8')  # 8진수
print(f'n = ({n})10')   # 10진수
print(f'n = ({n:x})16') # 16진수
print(f'n = ({n:X})16') # 16진수 대문자
print()
f = 7.123
f1 = 8
print(f'f = {f:.0f}')    # 소수부 생략
print(f'f1 = {f1:#.0f}') # 소수부가 없어도 소수점
print()
for i in range(65, 91): #ASCII 65 ~ 90의 문자
    print(f'{i:c}', end=' ')
