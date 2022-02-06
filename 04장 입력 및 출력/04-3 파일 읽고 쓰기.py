#파일 생성하기
"""
f = open("새파일.txt", 'w')
f.close()
"""
"""
파일 객체 = open(파일 이름, 파일 열기 모드)

파일열기모드	설명
r	읽기모드 - 파일을 읽기만 할 때 사용
w	쓰기모드 - 파일에 내용을 쓸 때 사용
a	추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용

새파일.txt 파일을 C:/doit 디렉터리에 생성할 때,

f = open("C:/doit/새파일.txt", 'w')
f.close()

f.close()는 열려 있는 파일 객체를 닫아 주는 역할
쓰기모드로 열었던 파일을 닫지 않고 다시 사용하려고 하면 오류가 발생

파일 경로와 슬래시(/)

파이썬 코드에서 파일 경로를 표시할 때 "C:/doit/새파일.txt" 처럼 슬래시(/)를 사용할 수 있다.
만약 역슬래시(\)를 사용한다면 "C:\\doit\\새파일.txt" 처럼 역슬래시를 2개 사용하거나
r"C:\doit\새파일.txt"와 같이 문자열 앞에 r 문자(Raw String)를 덧붙여 사용해야 한다.
왜냐하면 "C:\note\test.txt"처럼 파일 경로에 \n과 같은 이스케이프 문자가 있을 경우
줄바꿈 문자로 해석되어 의도했던 파일 경로와 달라지기 때문이다.
"""
#파일을 쓰기 모드로 열어 출력값 적기
f = open(r"C:\Users\Jaehwan\Desktop\Git\Jump-to-Python\04장 입력 및 출력\새파일.txt", 'w')
for i in range(1,11):
    data = "%d번째 줄입니다.\n" %i
    f.write(data)
f.close()
"""
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    print(data)
이 함수와 동일
"""
#프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법
#readline 함수 이용하기
f = open(r"C:\Users\Jaehwan\Desktop\Git\Jump-to-Python\04장 입력 및 출력\새파일.txt", 'r')
line = f.readline()
print(line)
f.close()
"""
첫 번째 줄을 읽어 출력
"""
f = open(r"C:\Users\Jaehwan\Desktop\Git\Jump-to-Python\04장 입력 및 출력\새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
"""
모든 줄을 읽어 화면에 출력

즉, f.readline()을 사용해 파일을 계속해서 한줄 씩 읽어 들인다.
readline()은 더 이상 읽을 줄이 없으면 break를 수행
"""
while True:
    data = input()
    if not data: break
    print(data)

#readlines 함수 사용하기
f = open(r"C:\Users\Jaehwan\Desktop\Git\Jump-to-Python\04장 입력 및 출력\새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    print(line)
f.close()

#줄 바꿈(\n) 문자 제거하기
f = open(r"C:\Users\Jaehwan\Desktop\Git\Jump-to-Python\04장 입력 및 출력\새파일.txt", 'r')
lines = f.readlines()
for line in lines:
    line = line.strip()
    print(line)
f.close()

#read 함수 사용하기
f = open(r"C:\Users\Jaehwan\Desktop\Git\Jump-to-Python\04장 입력 및 출력\새파일.txt", 'r')
data = r.read()
print(data)
f.close()
