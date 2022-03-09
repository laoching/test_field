try:
    a = int(input('정수 a: '))
    #if a == 0:                     raise로 예외를 발생 시킬 수 있음
    #    raise ValueError
    b = int(input('정수 b: '))

    print(f'a * b는 {a*b}')
    print(f'a / b는 {a/b}')

except ValueError:
    print('정수가 아닌듯?')

except ZeroDivisionError:
    print('0으로 나누기네요')

#except (ValueError, ZeroDivisionError) as e:
#   print(type(e))
#   print('0으로 나누었거나 확인할 수 없음')

else:
    print('성공!')

finally:
    print('수고')

"""
try는 프로그램을 중단시키지 않는다.

else는 except절에서 예외가 포착되지 않는 경우에 실행됨

finally는 예외 발생 유무과 상관없이 실행시킴

except의 규칙
- 한 개 이상 존재할 수 있음
- except로 지정한 예외와 호환되는 예외를 포착할 수 있음
    예외 B가 예외 A의 파생 클래스면 except A는 예외 A뿐만 아니라 예외 B도 포착함 -> B는 A의 일종이기 때문에
- 단일 except절에서 여러 예외를 튜플로 지정할 수 있음
- 포착한 예외를 변수로 받을 수 있음
    except (ValueError, ZeroDivisionError) as e:
    처럼 에러를 e라는 변수에 받을 수 있음
- 포착하는 예외를 지정하지 않을 수 있음
    예외의 종류를 지정하지 않은 except 절은 모든 예외를 포착하기 때문에 except 절이 여러 개인 형식의 except 절은 가장 마지막에 위치한다.
"""