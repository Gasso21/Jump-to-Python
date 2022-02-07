#모듈 만들기
import mod1
print(mod1.add(3, 4))
print(mod1.sub(4, 2))

from mod1 import add
print(add(3, 4))

#if__name__=="__main__":의 의미
# mod1.py
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

print(add(1, 4))
print(sub(4, 2))
"""
위 작성한 mod1.py 파일을 명령프롬프트창에서 실행하면
C:/Users/Jaehwan/Desktop/Git/Jump-to-Python/05장 파이썬 날개달기>python mod1.py
5
2

그런데 이 때, mod1.py 파일의 add와 sub 함수를 사용하기 위해 mod1 모듈을 import할 때 문제가 발생한다.
C:/Users/Jaehwan/Desktop/Git/Jump-to-Python/05장 파이썬 날개달기>python
Type "help", "copyright", "credits" or "license" for more information.
>>> import mod1
5
2

import mod1를 수행하는 순간 mod1.py가 실행이 되어 결과값을 출력

이 문제를 해결하기 위해 다음처럼 변경
"""
# mod1.py
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

if __name__ == "__main__":
    print(add(1, 4))
    print(sub(4, 2))

"""
if __name__== "__main__": 을 사용하면
C:/Users/Jaehwan/Desktop/Git/Jump-to-Python/05장 파이썬 날개달기>python
처럼 직접 이 파일을 실행했을 때는 __name__== "__main__"이 참이되어 if문 다음 문장이 수행된다.
반대로 대화형 인터프리터나 다른 파일에서 이 모듈을 불러서 사용할 때는 거짓이 되어 수행되지 않음
"""
"""
__name__ 변수란

파이썬의 __name__ 변수는 파이썬이 내부적으로 사용하는 특별한 변수 이름이다.
만약, C:/Users/Jaehwan/Desktop/Git/Jump-to-Python/05장 파이썬 날개달기>python
처름 직접 mod1.py 파일을 실행할 경우 mod1.py의 __name__ 변수에는 __main__ 값이 저장된다.
하지만 파이썬 셸이나 다른 파이썬 모듈에서 mod1을 import할 경우에는 mod1.py의 __name__변수에는 mod1.py의 모듈 이름 값 mod1이 저장된다.

>>> import mod1
>>> mod1.__name__
'mod1'
"""

#클래스나 변수 등을 포함한 모듈
"""
#mod2.py
PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)

def add(a, b):
    return a+b
"""
import mod2
print(mod2.PI)

a = mod2.Math()
print(a.solv(2))
print(mod2.add(mod2.PI, 4.4))

#다른 파일에서 모듈 불러오기
"""
# modtest.py
import mod2
result = mod2.add(3, 4)
print(result)
"""
#1.sys.path.append(모듈을 저장한 디렉터리) 사용하기
import sys
print(sys.path)
"""
sys.path는 파이썬 라이브러리가 설치되어 있는 디렉터리를 보여준다.
파이썬 모듈이 위 디렉터리에 들어 있따면 모듈이 저장된 디렉터리로 이동할 필요 없이 바로 불러서 사용할 수 있다.
sys.path에 위 파일이 들어있는 디렉터리를 추가하면 아무곳에서나 불러 사용할 수 있다.
sys.path의 결과값이 리스트이므로 sys.path.append를 사용하면 된다.

EX)
>>> sys.path.append("C:/doit/mymod")
>>> sys.path
['', 'C:\\Windows\\SYSTEM32\\python37.zip', 'c:\\Python37\\DLLs', 
'c:\\Python37\\lib', 'c:\\Python37', 'c:\\Python37\\lib\\site-packages', 
'C:/doit/mymod']
>>>

>>> import mod2
>>> print(mod2.add(3,4))
7

이상없이 사용할 수 있다.
"""

#2.PYTHONPATH 환경 변수 사용하기
"""
C:\doit>set PYTHONPATH=C:\doit\mymod
C:\doit>python
>>> import mod2
>>> print(mod2.add(3,4))
7

set 명령어를 사용해 PYTHONPATH 환경 변수에 mod2.py 파일이 있는 C:\doit\mymod 디렉터리를 설정한다.
"""