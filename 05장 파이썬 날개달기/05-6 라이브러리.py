# sys
"""
* 파일 경로를 표시할 때 명령 프롬프트 창에서는 /, \든 상관없지만,
    소스코드 안에서는 반드시 / 또는 \\ 기호를 사용해야 한다.
"""
import sys
"""
sys.path
sys.path.append("C:/doit/mymod")
"""

# pickle
"""
객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
pickle 모듈의 dump 함수를 사용하여 딕셔너리 객체인 data를 그대로 파일에 저장하는 방법
"""
import pickle
f = open("test.txt", 'wb')
data = {1: 'python', 2: 'you need'}
pickle.dump(data, f)
f.close()

import pickle
f = open("test.txt", 'rb')
data = pickle.load(f)
print(data)
>>> {2:'you need', 1:'python'}

# OS
import os
"""
OS 모듈은 환경 변수나 디렉터리, 파일 등의 
OS 자원을 제어할 수 있게 해주는 모듈
"""

# 내 시스템의 환경 변수값을 알고 싶을 때
"""
현재 시스템의 환경변수 값을 보여줌
"""
os.environ
>>>environ({'PROGRAMFILES': 'C:\\Program Files', 'APPDATA': … 생략 …})

"""
위에 결과값이 딕셔너리형의 객체이기 때문에 다음과 같이 호출 가능
"""
os.environ['PATH']
>>>'C:\\ProgramData\\Oracle\\Java\\javapath;...생략...'

# 디렉터리 위치 변경하기
"""
현재 디렉터리 위치 변경
"""
os.chdir("C:\WINDOWS")

# 디렉터리 위치 돌려받기
"""
현재 자신의 디렉터리 위치를 돌려줌
"""
os.getcwd()
>>>'C:\WINDOWS'

# 시스템 명령어 호출하기
"""
시스템 자체의 프로그램이나 기타 명령어를 파이썬에서 호출
os.system("명령어")
"""
os.system("dir")

# 실행한 시스템 명령어의 결과값 돌려받기
"""
시스템 명령어를 실행한 결과값을 읽기 모드 형태의 파일 객체로 돌려줌
"""
f = os.popen("dir")
"""
읽어 들인 파일 객체의 내용을 보기 위해서는 다음과 같이 실행
"""
print(f.read())

# 이 외 기타 함수
"""
함수	설명
os.mkdir(디렉터리)	디렉터리를 생성한다.
os.rmdir(디렉터리)	디렉터리를 삭제한다.단, 디렉터리가 비어있어야 삭제가 가능하다.
os.unlink(파일)	    파일을 지운다.
os.rename(src, dst)	src라는 이름의 파일을 dst라는 이름으로 바꾼다.
"""

# shutil
import shutil
"""
파일을 복사해주는 파이썬 모듈
"""
shutil.copy("src.txt", "dst.txt") #src.txt 파일과 동일한 내용의 파일이 dst.txt로 복사

# glob
import glob
"""
특정 디렉터리 내에 모든 파일 이름을 알고싶을 때
glob(pathname)
"""
glob.glob("c:/doit/mark*")
>>>['c:/doit\\marks1.py', 'c:/doit\\marks2.py', 'c:/doit\\marks3.py']

# tempfile
import tempfile
"""
파일을 임시로 만들어서 사용할 때
tempfile.mkstemp()는 중복되지 않는 임시 파일의 이름을 무작위로 만들어서 돌려준다.
"""
filename = tempfile.mkstemp()
filename
>>>'C:\WINDOWS\TEMP\~-275151-0'
"""
tempfile.TemporaryFile()은 임시 저장 공간으로 사용할 파일 객체를 돌려준다.
이 파일은 기본적으로 바이너리 쓰기 모드(wb)를 갖는다. f.close()가 호출되면 이 파일 객체는 자동으로 사라진다.
"""
import tempfile
f = tempfile.TemporaryFile()
f.close()

# time
import time
"""
UTC를 사용하여 현재 시간을 실수 형태로 돌려주는 함수
1970년 1월 1일 0시 0분 0초를 기준
"""
time.time()
>>> 988458015.73417199

"""
time.localtime은 time.time()이 돌려준 실수 값을 사용해서 연도, 월, 일, 시, 분, 초, ... 의 형태로 바꾸어 주는 함수이다.
"""
time.localtime(time.time())
>>> time.struct_time(tm_year=2013, tm_mon=5, tm_mday=21, tm_hour=16,
    tm_min=48, tm_sec=42, tm_wday=1, tm_yday=141, tm_isdst=0)

"""
위 time.localtime에 의해서 반환된 튜플 형태의 값을 인수로 받아서 날짜와 시간을 알아보기 쉬운 형태로 돌려주는 함수이다.
"""
time.asctime(time.localtime(time.time()))
>>> 'Sat Apr 28 20:50:20 2001'

"""
time.asctime(time.localtime(time.time()))은 time.ctime()을 사용해 간편하게 표시할 수 있다.
asctime과 다른 점은 ctime은 항상 현재 시간만을 돌려준다는 점이다.
"""
time.ctime()
>>> 'Sat Apr 28 20:56:31 2001'

"""
time.strftime('출력할 형식 포맷 코드', time.localtime(time.time()))

strftime 함수는 시간에 관계된 것을 세밀하게 표현하는 여러 가지 포맷 코드를 제공한다.
시간에 관계된 것을 표현하는 포맷 코드

포맷코드	설명	예
%a	요일 줄임말	                        Mon
%A	요일	                                Monday
%b	달 줄임말	                        Jan
%B	달	                                January
%c	날짜와 시간을 출력함	                06/01/01 17:22:21
%d	날(day)	                            [01,31]
%H	시간(hour)-24시간 출력 형태	        [00,23]
%I	시간(hour)-12시간 출력 형태	        [01,12]
%j	1년 중 누적 날짜	                    [001,366]
%m	달	                                [01,12]
%M	분	                                [01,59]
%p	AM or PM	                        AM
%S	초	                                [00,59]
%U	1년 중 누적 주-일요일을 시작으로	        [00,53]
%w	숫자로 된 요일	                    [0(일요일),6]
%W	1년 중 누적 주-월요일을 시작으로	        [00,53]
%x	현재 설정된 로케일에 기반한 날짜 출력	    06/01/01
%X	현재 설정된 로케일에 기반한 시간 출력	    17:22:21
%Y	년도 출력	                        2001
%Z	시간대 출력	                        대한민국 표준시
%%	문자	                                %
%y	세기부분을 제외한 년도 출력	            01
"""
time.strftime('%x', time.localtime(time.time()))
>>> '05/01/01'
time.strftime('%c', time.localtime(time.time()))
>>> '05/01/01 17:22:21'

"""
time.sleep 함수는 주로 루프 안에서 많이 사용한다.
이 함수를 사용하면 일정한 시간 간격을 두고 루프를 실행할 수 있다.
"""
for i in range(10):
    print(i)
    time.sleep(1)
"""
1초 간격으로 0부터 9까지의 숫자를 출력
time.sleep 함수의 인수는 실수 형태
즉 1이면 1초, 0.5면 0.5초
"""

# calendar
import calendar
"""
calendar.calendar(연도)로 사용하면 그해의 전체 달력을 볼 수 있다.
calendar.prcal(연도)를 사용해도 위와 똑같은 결괏값을 얻을 수 있다.

"""
print(calendar.calendar(2015))
print(calendar.prcal(2015))

print(calendar.prmonth(2015, 12))
>>>
December 2015
Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6
7  8  9  10 11 12 13
14 15 16 17 18 19 20
21 22 23 24 25 26 27
28 29 30 31

"""
weekday(연도, 월, 일) 함수는 그 날짜에 해당하는 요일 정보를 돌려준다. 
월요일은 0, 
화요일은 1, 
수요일은 2, 
목요일은 3, 
금요일은 4, 
토요일은 5, 
일요일은 6이라는 값을 돌려준다.
"""
calendar.weekday(2015, 12, 31)
>>>3

"""
monthrange(연도, 월) 함수는 입력받은 달의 1일이 무슨 요일인지와 
그 달이 며칠까지 있는지를 튜플 형태로 돌려준다.
"""
calendar.monthrange(2015,12)
>>>(1, 31) #1일은 화요일, 31일까지

# random
"""
다음은 0.0에서 1.0 사이의 실수 중에서 난수 값을 돌려줌
"""
random.random()
>>>0.53840103305098674

"""
다음 예는 1에서 10 사이의 정수 중에서 난수 값
"""
random.randint(1, 10)
>>>6

"""
다음 예는 1에서 55 사이의 정수 중에서 난수 값
"""
random.randint(1, 55)
>>>43

# random_pop.py
import random
def random_pop(data):
    number = random.randint(0, len(data)-1) # 0~4
    return data.pop(number) # index, EX) number = 0, data list 중 '[0]1' 제거

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    while data:
        print(random_pop(data))

# webbrowser
import webbrowser
"""
webbrowser는 자신의 시스템에서 사용하는 기본 웹 브라우저를 자동으로 실행하는 모듈이다.
다음 예제는 웹 브라우저를 자동으로 실행하고 해당 URL인 google.com으로 가게 해 준다.

webbrowser의 open 함수는 웹 브라우저가 이미 실행된 상태라면 입력 주소로 이동한다.
만약 웹 브라우저가 실행되지 않은 상태라면 새로 웹 브라우저를 실행한 후 해당 주소로 이동한다.
"""
webbrowser.open("http://google.com")

"""
open_new 함수는 이미 웹 브라우저가 실행된 상태이더라도 새로운 창으로 해당 주소가 열리게 한다.
"""
webbrowser.open_new("http://google.com")