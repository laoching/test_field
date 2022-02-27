def reverse_list(lst):
    n = len(lst)
    for i in range(n // 2):
        lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]

x = [22, 57, 11, 32, 91, 68, 77]
print(f'x ={x}')

reverse_list(x)
print(f'x ={x}')

'''
길이가 n인 리스트를 역으로 정렬하기 위해서는 n/2번의 반복이 필요하다.
[a b c d e f g]
a와 g 교환, b와 f 교환, c와 e 교환,,,,
만약 리스트의 길이가 홀수인 경우 가운데 숫자는 위치가 그대로이기 때문에 n/2이 적용 가능하다.
'''