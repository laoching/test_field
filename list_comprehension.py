# 리스트 내포 표시 => [식 for 요소 in 이터러블]
x = [n for n in range(1, 8)]
print(x)

# [식 for 요소 in 이터러블 if 판정식]
x = [n for n in range(1, 8) if n % 2 == 0]  # 짝수
# for문을 반복하면서 if 판정식이 성립하는 n의 값을 순서대로 나열
print(x)

# for문 중첩 내포 표기
x = [i * 10 + j for i in range(1,3) for j in range(1, 4)]
# i는 1부터 2까지, j는 1부터 3까지
print(x)

# 중첩 리스트 내포 표기로 2차원 리스트 생성
x = [[i * 10 + j for i in range(1, 3)] for j in range(1, 4)]
# i * 10이 있는 부분에서 리스트를 생성하고 이것들을 요소로 하는 리스트를 외부의 for문에서 생성
print(x)