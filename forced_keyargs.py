def puts(*, n, s):
    for _ in range(n):
        print(s, end='')

puts(n = 3, s = '*')
print()
puts(s = '+', n = 7)
print()
puts(3, '*')    # 오류 발생

'''
함수의 인수에 *를 사용한다면 그 이후의 것들은 강제로 키워드 인수로 다룬다는 뜻이다.
만약 puts(n, *, s)라면 n은 위치 인수, s는 키워드 인수로 강제함
'''