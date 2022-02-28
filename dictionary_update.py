# dict.update([other])
# 딕셔너리의 내용을 other 키와 값으로 수정함, 기존의 키는 덮어쓰고 리턴은 None임
# 키워드 인수가 지정된 경우 그 키와 값의 쌍으로 딕셔너리를 수정함

rgb = {'red': '빨', 'blue': '파', 'green': '초'}

# 동일한 키인 red가 있는데 이 경우 '빨'에서 '빨강'으로 수정됨
cm = {'cyan': '하늘', 'magenta': '자주', 'red': '빨강'}

# 딕셔너리 rgb에 딕셔너리 cm을 결합
rgb.update(cm)
print(rgb)