def puts(n, s):
    for _ in range(n):
        print(s, end='')

# 인수 이름이 문자열이 아니면 에러 발생
d1 = {'n': 3, 's': '*'}
d2 = {'s': '+', 'n': 7}

# **를 쓰면 딕셔너리가 언팩되서 전달된다.
puts(**d1)
print()
puts(**d2)
