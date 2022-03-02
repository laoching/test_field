def is_leapyear(year: int) -> bool:
    """입력된 연도가 윤년인지 판단하는 함수
        윤년이면 1을 반환"""
    return year % 4 == 0 and y % 100 != 0 or y % 400 == 0
help(is_leapyear)
print('특정 해의 일 수를 구합니다.')
y = int(input('구할 년도: '))
print(f'그 해는 {365+is_leapyear(y)}일 입니다.')
