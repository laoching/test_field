color = {'red': '빨강', 'green': '초록', 'blue': '파랑'}

color['red'] = '레드'     # color['red']의 값 '빨강'을 '레드'로 업데이트

# 존재하지 않는 키에 접근할 경우 요소가 한 개 증가
color['yellow'] = '노랑'  # 키가 'yellow', 값이 '노랑'인 요소를 삽입

# dict.setdefault(key[, value])
# key가 딕셔너리에 존재하면 그 값을 리턴,
# 그렇지 않으면 값이 value인 key를 삽입한 다음 value를 리턴, value를 생략하면 값는 None
color = {'red': '빨강', 'green': '초록', 'blue': '파랑'}
# 업데이트
v1 = color.setdefault('red', '레드')
# 삽입
v2 = color.setdefault('yellow', '노랑')
print(v1)
print(v2)
print(color)
