#문자열에 작은 따옴표(') 포함
food = "Python's favorite food is perl."
print(food)

#문자열에 큰 따옴표(") 포함
say = '"Python is very easy." he says.'
print(say)

#백슬래시(\)를 사용해서 작은 따옴표(')와 큰 따옴표(")를 문자열에 포함
food = 'Python\'s favorite food is perl.'
say = "\"Python is very easy.\" he says."
print(food)
print(say)

#줄을 바꾸기 위한 이스케이프 코드 \n 삽입
multiline = "Life is too short\nYou need Python"
print(multiline)

#연속된 작은 따옴표 3개(''') 또는 큰 따옴표 3개(""") 사용
multiline = """
Life is too short
You need Python
"""
print(multiline)

#문자열 사이에 탭 간격을 줄 때
tap = "tap\ttap"
print(tap)

#문자열 더해서 연결(Concatenation)
head = "Python"
tail = " is fun!"
print(head + tail)

#문자열 곱하기
a = "python"
print(a*2)

#문자열 길이 구하기
a = "Life is too short"
print(len(a))

#슬라이싱
a = "Life is too short, You need Python"
print(a[0:4]) #끝번호에 해당하는 것은 포함하지 않음

#Pithon 문자열을 Python 문자열로 변경
a = "Pithon"
print(a[1])
# a[1] = 'y' -> 오류 발생! 문자열의 요솟값은 바꿀 수 있는 값이 아님. immutable한 자료형
a = a[:1] + 'y' + a[2:]
print(a)

#문자열 포매팅
print("I eat %d apples." %3) #%d는 문자열 포맷 코드
print("I eat %s apples." %"five")

#문자열 포매팅 - 2개 이상의 값 넣기
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." %(number, day))

"""
문자열 포맷 코드
%s - 문자열(String)
$c - 문자 1개(Character)
%d - 정수(Integer)
%f - 부동소수(Floating-point)
%o - 8진수
%x - 16진수
%% - Literal % (문자 % 자체)
"""
#%s 포맷 코드는 어떤 형태의 값이든 변환해 넣을 수 있음
print("I have %s apples" %3)
print("rate is %s" %3.234)

#포매팅 연산자 %d와 %를 같이 쓸 때는 %% 사용
print("Error is %d%%." %98)

#정렬과 공백
print("%10s" %"hi") #전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬

print("%-10sjane" %"hi") #왼쪽 정렬

#소수점 표현
print("%0.4f" %3.141592) #'.'의 의미는 소수점 포인트, 그 뒤의 숫자 4는 소수점 뒤에 나올 숫자의 개수
print("%10.4f" %3.141592) #소수점 네 번째 자리까지만 표시하고 전체 길이가 10개인 문자열의 공간에서 오른쪽 정렬

#format 함수를 사용한 포매팅
print("I eat {0} apples" .format(3))

#문자열 바로 대입
print("I eat {0} apples" .format("five"))

#숫자 값을 가진 변수로 대입
number = 3
print("I eat {0} apples" .format(number))

#2개 이상의 값 넣기
number = 10
day = "three"
print("I ate {0} apples. so I was sick for {1} days." .format(number, day))

#이름으로 넣기
print("I ate {number} apples. so I was sick for {day} days." .format(day=3, number=10))
#{name}형태로 사용할 경우 format 함수에는 반드시 name=value와 같은 형태의 입력값이 었어야만 함

#인덱스와 이름을 혼용해서 넣기
print("I ate {0} apples. so I was sick for {day} days." .format(10, day=3))

#왼쪽 정렬
print("{0:<10}" .format("hi")) #:<10 표현식을 사용하면 치환되는 문자열을 왼쪽으로 정렬하고 문자열의 총 자릿수를 10으로 맞춤

#오른쪽 정렬
print("{0:>10}" .format("hi"))

#공백 채우기
print("{0:=^10}" .format("hi"))
print("{0:!<10}" .format("hi"))
"""
정렬할 때 공백 문자 대신에 지정한 문자 값으로 채워 넣는 것도 가능
채워 넣을 문자 값은 정렬 문자 <,^,> 바로 앞에 넣어야 함
"""

#소수점 표현
y = 3.42134234
print("{0:0.4f}" .format(y))
print("{0:10.4f}" .format(y))

#f 문자열 포매팅
name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

#표현식(+, -와 같은 수식을 함께 사용하는 것)을 지원
age = 30
print(f'나는 내년이면 {age+1}살이 된다.')

#딕셔너리 사용
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

#정렬
print(f'{"hi":<10}')
print(f'{"hi":^10}')
print(f'{"hi":>10}')

#공백채우기
print(f'{"hi":=^10}')
print(f'{"hi":!<10}')

#소수점
y = 3.141592
print(f'{y:0.4f}')
print(f'{y:10.4f}')

print(f'{{name}}')

#문자열 관련 함수
a = "hobby"
print(a.count('b')) #문자열 중 문자 b의 개수를 돌려줌

#위치 알려주기1(find)
a = "Python is the best choice."
print(a.find('b')) #'b'가 처음으로 나온 위치를 반환
print(a.find('k')) #찾는 문자나 문자열이 존재하지 않는다면 -1을 반환

#위치 알려주기2(index)
a = "Life is too short"
print(a.index('t')) #'t'가 처음으로 나온 위치를 반환
#print(a.index('k')) #찾는 문자나 문자열이 존재하지 않는다면 오류를 발생

#문자열 삽입(join)
print(",".join('abcd')) #'abcd'문자열의 각각의 문자 사이에 ','을 삽입
"""
join 함수는 문자열뿐만 아니라 앞으로 배울 리스트나 튜플도 입력으로 사용할 수 있음
"""
print(",".join(['a','b','c','d'])) #join 함수의 입력으로 리스트를 사용

#소문자 -> 대문자로
a = "hi"
print(a.upper())

#대문자 -> 소문자로
a = "HI"
print(a.lower())

#왼쪽 공백 지우기(lstrip)
a = " hi "
print(a.lstrip())

#오른쪽 공백 지우기(rstrip)
a = " hi "
print(a.rstrip())

#양쪽 공백 지우기(strip)
a = " hi "
print(a.strip())

#문자열 바꾸기(replace)
a = "Life is too short"
print(a.replace("Life", "Your leg"))

#문자열 나누기(split)
a = "Life is too short"
print(a.split()) #괄호 안에 아무 값도 넣어주지 않으면 공백(스페이스, 텝, 엔터 등)을 기준으로 문자열을 나눔
b = "a:b:c:d"
print(b.split(':')) #괄호 안에 특정 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나눔
