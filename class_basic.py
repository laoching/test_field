"""회원번호: no
    성명: name
    체중: weight"""

class Member:   # 클래스 정의 (pass문으로만 클래스 본체를 구성하는 것이 최소한의 클래스 정의)
    """스포츠 클럽 회운 클래스1"""
    pass

# 회원 클래스 테스트

kim = Member()  # 클래스 Member 타입의 객체를 생성 -> 클래스에서 생성된 객체가 인스턴스(instance)
kim.no = 15     # 속성 참조 연산자인 .을 이용해 no, name, weight라는 변수를 생성하는 동시에 대입
kim.name = '김준호'
kim.weight = 72.7

park = Member()
park.no = 22
park.name = '박박이'
park.weight = 55.5

print(f'{kim.no}: {kim.name} {kim.weight}')
print(f'{park.no}: {park.name} {park.weight}')

