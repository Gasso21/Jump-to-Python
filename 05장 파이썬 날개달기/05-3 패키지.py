#패키치란 무엇인가
"""
패키지(Packages)는 도트(.)를 사용하여 파이썬 모듈을 계층적(디렉터리 구조)으로 관리할 수 있게 함
EX)
A.B
(A는 패키지 이름, B는 모듈)
파이썬에서 모듈은 하나의 .py 파일이다.
"""
#가상의 game 패키지 예
"""
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
        
game, sound, graphic, play는 디렉터리이고 확장자가 .py인 파일은 파이썬 모듈이다.
game 디렉터리가 이 패키지의 루트 디렉터리이고 sound, graphic, play는 서브 디렉터리이다.

패키지 구조로 파이썬 프로그램을 만드는 것이 공동 작업이나 유지 보수 등 여러 면에서 유리
패키지 구조로 모듈을 만들면 다른 모듈과 이름이 겹치더라도 더 안전하게 사용할 수 있음
"""

#패키지 만들기
#1. 파일 준비
"""
C:/doit/game/__init__.py
C:/doit/game/sound/__init__.py
C:/doit/game/sound/echo.py
C:/doit/game/graphic/__init__.py
C:/doit/game/graphic/render.py
"""
#2. echo.py 파일
# echo.py
"""
def echo_test():
    print("echo")
"""
#3. render.py 파일
# render.py
"""
def render_test():
    print("render")
"""

#패키지 안의 함수 실행하기
"""
C:\\Users\Jaehwan\Desktop\Git\Jump-to-Python\05장 파이썬 날개달기'> set PYTHONPATH=C:/Users/Jaehwan/Desktop/Git/Jump-to-Python/"05장 파이썬 날개달기"
C:\\Users\Jaehwan\Desktop\Git\Jump-to-Python\05장 파이썬 날개달기'> python
Python 3.8.3 (default, Jul  2 2020, 17:30:36) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.

>>> import game.sound.echo
>>> game.sound.echo.echo_test()
echo

>>> from game.sound import echo
>>> echo.echo_test()
echo

>>> from game.sound.echo import echo_test
>>> echo_test()
echo

>>> import game
>>> game.sound.echo.echo_test()
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
AttributeError: 'module' object has no attribute 'sound'

import game을 수행하면 game 디렉터리의 __init__.py 에 정의한 것만 참조할 수 있다.

>>> import game.sound.echo.echo_test
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
ImportError: No module named echo_test

도트 연산자(.)를 사용해서 import a.b.c처럼 import할 때 가장 마지막 항목인 c는 반드시 모듈 또는 패키지여야만 한다.
"""

#__init__.py 의 용도
"""
__init__.py 파일은 해당 디렉터리가 피키지의 일부임을 알려주는 역할
만약 game, sound, graphic 등 패키지에 포함된 디렉터리에 __init__.py 파일이 없다면 패키지로 인식되지 않는다.

※ python3.3 버전부터는 __init__.py 파일이 없어도 패키지로 인식한다(PEP 420).
    하지만 하위 버전 호환을 위해 __init__.py 파일을 생성하는 것이 안전한 방법이다.
"""