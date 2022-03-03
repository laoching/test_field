# 80점 이상의 점수만 출력

import random

num = int(input('학생 수: '))

score = [None] * num

for i in range(num):
    score[i] = random.randint(0, 100)

print(f'모든 학생의 점수= {score}')
print(f'합격자 점수= {list(filter(lambda n: n>=80, score))}')

'''
filter 함수는 80점 이상의 점수만 추출함
전달된 인수가 80 이상이면 True를, 아니면 False를 반환하는 함수를 lambda로 생성함

호출된 filter는 두 번째 인수로 받은 리스트의 모든 요소를 순서대로 탐색함 
-> 80점 이상만 추출하고 그것들을 filter 객체로 생성함

filter 객체를 그대로 출력할 수 없어 list로 변환함 
'''