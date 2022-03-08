"""
상속의 기초가 되는 클래스
- basic class
- super class
- parant class

상속으로 새로 만들어진 클래스
- derived class(파생 클래스)
- sub class
- child class
"""

"""
파생 클래스 정의 형식
class 파생클래스이름(기본클래스이름):
    클래스 본체
"""
class Pet:
    """애완동물 클래스"""

    def __init__(self, name: str, master: str) -> None:
        """생성자"""
        self._name = name
        self._master = master

    def introduce(self) -> None:
        """자기소개"""
        print(f'제 이름은 {self._name}입니다.')
        print(f'제 주인의 이름은 {self._master}입니다.')

    def __str__(self) -> str:
        """문자열화"""
        return self._name + '<<' + self._master + '>>'

    def print(self) -> None:
        """출력(__str__이 리턴하는 문자열을 출력하고 개행)"""
        print(self.__str__())

class RobotPet(Pet):
    """로봇 클래스"""

    def __init__(self, name: str, master: str, type_no: str) -> None:
        """생성자"""
        super().__init__(name, master)  # 기본 클래스의 메소드를 호출하기 위해서 super()를 사용함, 기본 클래스를 수퍼클래스라고도 부름
        self._type_no = type_no
