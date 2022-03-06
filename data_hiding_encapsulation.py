# define_class.py에서 변경 사항
# 1. 회원 번호, 이름, 체중 값을 클래스 외부에서 바꿀 수 없도록 변경
# 2. 체중 감량 메소드 lose_weight를 추가

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

#회원 클래스 테스트

kim = Member(14, 'abc', 22.2)
park = Member(22, 'def', 56.7)

kim.lose_weight(3.5)
park.lose_weight(3.5)

kim.print()
park.print()

"""
인스턴스 앞에 밑줄 두개는 뭔가요
-> 외부에서 클래스 속성에 접근하지 못하도록 하는 설정임 -> data hiding(데이터 은닉)

메소드 lose_weight는 매개 변수 loss로 받은 만큼의 체중을 줄임
-> 메소드는 속한 인스턴스의 데이터 값을 바탕으로 처리하고 그 값을 변경함 -> encapsulation(캡슐화)
"""