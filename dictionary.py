# 딕셔너리는 {키:값} 형태로 이루어져있음
# 인덱스로 키를 지정하면 해당하는 값이 따라온다.
# 같은 키가 여러 개 존재할 수 없다.
# 등록되지 않은 키를 참조하면 KeyError 예외가 발생한다.

season = {
    '봄': 'spring',
    '여름': 'summer',
    '가을': 'autumn',
    '겨울': 'winter'
}
print("season['봄'] = ", season['봄'])
print("season['여름'] = ", season['여름'])
print("season['가을'] = ", season['가을'])
print("season['겨울'] = ", season['겨울'])