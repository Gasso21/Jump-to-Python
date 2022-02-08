"""
오류를 무시하고 싶을 때,
try, except를 사용해서 예외적으로 오류를 처리할 수 있다.
"""

#디렉터리 안에 없는 파일을 열려고 시도했을 때 발생하는 오류
"""
FileNotFoundError: [Errno 2] No such file or directory: '  '
"""

#0으로 다른 숫자를 나누는 경우
"""
ZeroDivisionError: division by zero
"""

#리스트에 없는 값
"""
IndexError: list index out of range
"""

#오류 예외 처리 기법
#try, except문
try:
    ...
except [발생 오류[as 오류 메시지 변수]]:
    ...
"""
try 블록 수행 중 오류가 발생하면 except 블록이 수행
"""

# except 구문
"""
except [발생 오류 [as 오류 메시지 변수]]:

1. try, except만 쓰는 방법

try:
    ...
except:
    ...
    
2. 발생 오류만 포함한 except문

try:
    ...
except 발생 오류:
    ...

오류가 발생했을 때 except문에 미리 정해 놓은 오류 이름과 일치할 때만 except 블록을 수행함

3. 발생 오류와 오류 메시지 변수까지 포함한 except문

try:
    ...
except 발생 오류 as 오류 메시지 변수:
    ...

오류 메시지의 내용ㄲ지 알고 싶을 때 사용

EX)
try:
    4 / 0
except ZeroDivisionError as e:
    print(e)
>> division by zero
"""

#try .. finally
"""
finally절은 try문 수행 도중 예외 발생 여부에 상관없이 항상 수행
보통 finally절은 사용한 리소스를 close해야 할 때 많이 사용
"""

f = open('foo.txt', 'w')
try:
    # 무언가를 수행한다.
finally:
    f.close()
"""
foo.txt 파일을 쓰기 모드로 연 후에 try문을 수행한 후 예외 발생 여부와 상관없이 finally절에서 f.close()로 열린 파일을 닫을 수 있다.
"""

#여러개의 오류처리하기
try:
    ...
except 발생 오류1:
   ...
except 발생 오류2:
   ...
"""
EX)
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 할 수 없습니다.")

위 예시에서는 a[3]에 해당하는 오류가 발생
그에 따라 4/0으로 발생되는 ZeroDivisionError 오류는 발생하지 않는다.

EX)
try:
    a = [1,2]
    print(a[3])
    4/0
except ZeroDivisionError as e:
    print(e)
except IndexError as e:
    print(e)

프로그램을 실행하면 "list index out of range" 오류 메시지가 출력

EX)
try:
    a = [1,2]
    print(a[3])
    4/0
except (ZeroDivisionError, IndexError) as e:
    print(e)

ZeroDivisionError와 IndexError를 함께 처리
"""

#try문에 else절 사용

try:
    ...
except [발생 오류[as 오류 메시지 변수]]:
    ...
else:  # 오류가 없을 경우에만 수행된다.
    ...
"""
try:
    age=int(input('나이를 입력하세요: '))
except:
    print('입력이 정확하지 않습니다.')
else:
    if age <= 18:
        print('미성년자는 출입금지입니다.')
    else:
        print('환영합니다.')
"""

#오류 회피하기
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass

#오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()
"""
Eagle 클래스에서 fly 함수를 구현하지 않았기 때문에 Bird 클래스의 fly 함수가 호출된다.
그리고 raise문에 의해 NotImplementedError가 발생할 것이다.
"""
"""
EX)
class Eagle(Bird):
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()

>> very fast
"""

#예외 만들기
#파이썬 내장 클래스인 Exception 클래스를 상속하여 만들기
"""
class MyError(Exception):
    pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

say_nick("천사")
say_nick("바보")

>>
천사
Traceback (most recent call last):
  File "...", line 11, in <module>
    say_nick("바보")
  File "...", line 7, in say_nick
    raise MyError()
__main__.MyError
"""
#예외 처리 기법을 사용하여 MyError 발생을 예외 처리
"""try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")

만약 오류 메시지를 사용하고 싶을 경우 다음처럼 예외 처리

try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)

이경우 print(e)로 오류 메시지가 출력되지 않음
오류 메시지가 보이게 하려면 오류 클래스에 다음과 같은 __str__ 메서드를 구현해야 함
__str__ 메서드는 print(e)처럼 오류 메시지를 print문으로 출력할 경우에 호출되는 메서드

class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."
"""
class MyError(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

try:
    say_nick("천사")
    say_nick("바보")
except MyError:
    print("허용되지 않는 별명입니다.")