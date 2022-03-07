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
# 애완동물 클래스 테스트
kurt = Pet('kurt', 'james')
kurt.introduce()
print(kurt)
print(f'str(Kurt) : {str(kurt)}')
kurt.print()

"""
__str__ 메소드는 인스턴스를 나타내는 문자열을 리턴함
이 코드에서는 '이름 <<주인이름>>' 형식의 문자열을 리턴함

메소드 print는 __str__메소드가 리턴하는 문자열을 그대로 출력하는 메소드임
self.__str()__은 출력을 위해 내장 함수 print로 전달함
메소드에서는 자신의 클래스에 속하는 다른 메소드를 'self.메소드이름(인수)'로 호출함
"""