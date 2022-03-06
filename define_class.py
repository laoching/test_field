class Member:
    """스포츠 클럽 회원 클래스"""

    def __init__(self, no: int, name: str, weight: float) -> None:
        """생성자"""
        self.no = no            #회원 번호
        self.name = name        #이름
        self.weight = weight    # 체중

    def print(self) -> None:
        """데이터 출력"""
        print(f'{self.no}: {self.name} / {self.weight}kg')

#회원 클래스 테스트

kim = Member(15, 'abc', 44.4)
park = Member(22, 'efg', 22.2)

kim.print()
park.print()

'''
클래스의 첫 번째 인수인 self
-> 자기 자신의 인스턴스를 참조하는 변수, 이름도 자유롭게 설정 가능하지만 보통 self로 사용

self를 제외한 두 번째 인수부터가 실질적인 인수임.
-> __init__ 메소드: 실질적인 인수 = 3개
-> print 메소드: 실질적인 인수 = 2개

시작 부분의 __init__ 메소드는 인스턴스를 초기화하는 메소드임
-> 일반적으로 생성자(constructor)라고 부름
-> __과 같이 언더바 두개는 dunder라고 부름, __init__는 dunder init dunder라고 부름
이 생성자는 no, name, weight 매개 변수에 받은 세 개의 값을 self.no, self.name, self, weight에 대입하는 역할임
이 생성자는 return을 사용하지 않아도 None을 return하며 return으로 None이 아닌 값을 반환하면 TypeError가 발생함


클래스를 호출하면 인스턴스가 생성되고 동시에 __init__ 메소드가 자동으로 호출된다.
kim과 park은 인스턴스를 참조하는 이름이다.
self는 kim과 park이 참조하는 인스턴스를 참조한다

이 코드에서 인스턴스를 생성하는 방법
kim = Member(12, 'abc', 22.2)

print를 메소드라고 부름.
이 코드에서 메소드 print는 출력하는 역할임
정규화된 이름은 Member.print()임
인스턴스 변수의 값은 인스턴스의 현재 상태를 나타내끼 때문에 state라고도 부름
'''