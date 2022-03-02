def keys_of(dic: dict, val: 'value') -> list:
    """딕셔너리 dic에 있는 값이 val인 요소의 키를 리스트로 리턴"""
    return [k for k, v in dic.items() if v == val]

txt = input('문자열: ')
cnt = {ch: txt.count(ch) for ch in txt}
print('분포 =', cnt)

num = int(input('몇 개인 문자: '))
print(f'{num}개인 문자 = {keys_of(cnt, num)}')