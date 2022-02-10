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

#shutil
import shutil
"""
파일을 복사해주는 파이썬 모듈
"""
shutil.copy("src.txt", "dst.txt") #src.txt 파일과 동일한 내용의 파일이 dst.txt로 복사