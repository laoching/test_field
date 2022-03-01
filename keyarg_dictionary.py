# 딕셔너리화된 키워드 인수 정보 출력

def print_kwargs(s, **kwargs):
    '''딕셔너리화된 키워드 인수를 받는 kwargs의 정보 출력하기'''

    print(s)
    print(f'type(kwargs): {type(kwargs)}')
    print(f'len(kwargs): {len(kwargs)}')
    print(f'kwqrgs ={kwargs}')

print_kwargs('1번', spring="봄", summer='여름')
print()
print_kwargs('2번', spring='봄')

# s에 1번, 2번이 넘어가고
# **kwargs에 spring이 키, 봄이 value로 들어감