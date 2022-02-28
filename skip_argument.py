def hello(name, honorific = '씨'):
    print(f'안녕하세요 {name}{honorific}')
hello('제임스')    # 두 번째 인수 없이 함수를 실행하기 때문에 기본값인 '씨'가 붙어 나옴
hello('토마스', '선생님')
hello('존', '님')

# 이처럼 인수를 생략하기 위해서는 함수 정의에 기본값이 설정되어 있어야 한다.
