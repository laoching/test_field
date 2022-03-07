class Commander:
    """장군 클래스"""
    __counter = 0   # 몇 번 까지 아이덴티티를 사용하는지 체크

    def __init__(self, name: str) -> None:
        """생성자"""
        self.__name = name
        Commander.__counter += 1
        self.__id = Commander.__counter

    def id(self) -> int:
        """아이덴티티 받기"""
        return self.__id

    @classmethod
    def max_id(cls) -> int:
        """지금까지 아이덴티티를 몇 번까지 부여했는가"""
        return cls.__counter

    def print(self) -> None:
        """데이터 출력"""
        print(f'{self.__name}:{self.__id}')

kim = Commander('kim')
park = Commander('park')
ahn = Commander('ahn')

print(f'kim.id() = {kim.id()}')
print(f'park.id() = {park.id()}')
print(f'ahn.id() = {ahn.id()}')

print(f'Commander.max_id() = {Commander.max_id()}')     # 이처럼 [인스턴스 이름.메소드 이름(인수)] 형식으로 클래스 메소드 호출 가능
print(f'kim.max_id() = {kim.max_id()}')

"""
@classmethod
개별 인스턴스에는 속하지 않고 클래스에 속한 메소드
클래스 메소드임을 나타내기 위해 앞에 @classmethod 데코레이터를 사용함
메소드가 받는 첫 번째 인수 cls는 자신이 속한 클래스 객체를 참조하는 변수임

따라서 이 메소드는 클래스에 속하는 클래스 변수 Commander.__counter를 cls.__counter로 액세스할 수 있음

클래스 메소드에는 self가 없음 -> 인스턴스 변수에 액세스할 수 없음
-> max_id에는 self.__name과 self.__id에 액세스할 수 없다는 뜻

하지만 인스턴스 메소드에서는 클래스 변수에 자유롭게 액세스 간으함

@staticmethod
정적 메소드라고 부르며 @staticmethod 데코레이터를 시작으로 정의함
메소드의 인수로 cls를 받지 않음
-> 클래스 변수에 접근하기 위해 명시적인 클래스 선언이 필요함
"""