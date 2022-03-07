class Member:
    """스포츠 클럽 회원 클래스 3"""

    def __init__(self, no: int, name: str, weight: float) -> None:
        """생성자"""
        self.__no = no
        self.__name = name
        self.__weight = weight

    def lose_weight(self, loss: float) -> None:
        """감량한 무게"""
        self.__weight -= loss

    def print(self) -> None:
        """데이터 출력"""
        print(f'{self.__no}: {self.__name} / {self.__weight}kg')

    @property
    def weight(self) -> float:
        """체중 획득(게터)"""
        return self.__weight

    @weight.setter
    def weight(self, weight: float) -> None:
        """체중 설정(세터)"""
        self.__weight = weight if weight > 0.0 else 0.0

# 회원 클래스 테스트

kim = Member(15, 'jane', 22.2)

kim.weight = 67.3
print(f'kim.weight = {kim.weight}')

"""
데이터 속성 값을 받아오거나 설정하는 메소드 = 게터와 세터(getter, setter)
둘을 통틀어 부르는 말 = 접근자(accessor)

게터는 @property를 붙여 정의함, 메소드 이름은 값을 확인하는 데이터 특성을 잘 나타낼 수 있는 이름으로 짓는다. = 접근자 이름
__weight의 접근자 일므을 weight로 설정
게터의 본체에서는 데이터 값을 리턴함

세터는 앞에 @접근자이름.setter를 붙여 정의함, 메소드 이름은 게터와 같은 이름, 즉 접근자 이름을 사용함
세터 본체에서는 매개 변수로 전달받은 값을 데이터에 대입함.
weight if weight > 0.0 else 0.0은 매개 변수 weight에 0.0 이하의 값이 들어왔을 경우 데이터 __weight에 0.0을 대입함

게터와 세터를 정의하면 [인스턴스이름.접근자이름] 형식으로 값을 획득하고 설정할 수 있음 -> 우변, 좌변 모두 대입 가능
-> kim.weight에 대입하고 값을 획득

@property 데코레이터?
-> 데코레이터는 다름 함수를 리턴하는 함수를 만들기 위한 구조임. 
위처럼 정의하면 아래처럼 코드가 변환된다.
-------------------
@deco
def func(...):
    함수 본체
-------------------
def func(...):
    함수 본체
func = deco(func)
-------------------

즉 @deco를 쓴 함수 func를 정의하면 deco(func)를 func로 호출할 수 있음
"""