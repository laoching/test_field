# puts 함수 = n개의 s를 연속으로 출력하는 함수

def puts(n, s):
    for i in range(n):
        print(s, end=' ')

print('직각 이등변 삼각형')
n = int(input('짧은 변의 길이: '))

for i in range(1, n + 1):
    puts(n = i, s = '*')
    print()

'''    
키워드 인수는 함수에 넘겨줘야 할 인수가 많을 때 유용하게 사용된다.
헷갈리지 않게 넘겨줄 수 있음
키워드 인수처럼 지정하지 않고 위치에 맞게 넘겨주는 방식을 position argument(위치 인수)라고 함
    ex) puts(i, '*')

키워드 인수와 위치 인수를 같이 사용할 때는 키워드 인수가 뒤에 온다. 
    ex) puts(5, s = '+')
'''