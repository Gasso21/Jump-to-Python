"""
def 함수명(매개변수):
    <수행할 문장1>
    <수행할 문장2>
    ...
"""
#일반적인 함수
def add(a, b):
    return a + b

a = 3
b = 4
print(add(a, b))

def add(a,b):
    result = a + b
    return result

print(add(a,b))

#입력값이 없는 함수
def say():
    return 'HI'

print(say())

#결과값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." %(a, b, a+b))

print(add(3, 4))
"""
>> 3, 4의 합은 7입니다.
>> None
'None'이란 거짓을 나타내는 자료형
함수 실행 과정에서의 값이 나온 것일 뿐, 궁극적인 결과값은 None
"""

#입력값도 결과값도 없는 함수
def say():
    print('Hi')

print(say())

#매개변수 지정하여 호출하기
def sub(a, b):
    return a-b

result = sub(a=3, b=7)
print(result)

result = sub(b=7, a=3)
print(result)

#입력값이 몇 개가 될지 모를 때
"""
def 함수이름(*매개변수): 
    <수행할 문장>
    ...
"""
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
"""
add_many 함수는 입력값이 몇 개이든 상관이 없다.
매개변수 이름 앞에 *을 붙이면 입력값을 전부 모아서 튜플로 만들어 주기 때문
args는 매개변수를 뜻하는 영어 단어 arguments의 약자이며 관례적으로 자주 사용
"""
result = add_many(1, 2, 3)
print(result)

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

def add_mul(choice, *args):
    if choice =="add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result)
result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)

#키워드 파라미터 kwargs
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo', age=3)
"""
키워드 파라미터를 사용할 때는 매개변수 앞에 별 두 개(**)를 붙임
**kwargs처럼 매개변수 이름 앞에 **을 붙이면 매개변수 kwargs는 딕셔너리가 되고 모든 key=value 형태의 결과값이 그 딕셔너리에 저장됨
"""

#함수의 결과값은 언제나 하나
def add_and_mul(a,b):
    return a+b, a*b
result = add_and_mul(3,4)
print(result)
"""
결과값이 2개라면, 튜플로 묶여서 하나로 표현됨
"""

#return의 또 다른 쓰임새
def say_nick(nick):
    if nick == "바보":
        return
    print("나의 별명은 %s 입니다." %nick)
"""
입력값으로 '바보'라는 값이 들어오면 문자열을 출력하지 않고 함수를 즉시 빠져나감
"""
say_nick('야호')
say_nick('바보')

#매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself('정재환', 26, 1)

"""
def say_myself(name, man=True, old): 
    ...
say_myself("정재환", 26)
이렇게 되면 아래와 같은 오류가 발생한다.
SyntaxError: non-default argument follows default argument
"""

#함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a+1

vartest(a)
print(a)
"""
결과값은 1로 출력.
함수 안에서 a <- 2가 됐어도 범위는 함수 내로 국한.
"""

def vartest(a):
    a = a + 1

vartest(3)
print(a)
"""
print(a)에서 오류 발생.
"""

#함수 안에서 함수 밖의 변수를 변경하는 방법
#1. return 사용하기
a = 1
def vartest(a):
    a = a+1
    return a

a = vartest(a)
print(a)

#2. global 명령어 사용하기
a = 1
def vartest():
    global a
    a = a+1

vartest()
print(a)
"""
global a 문장은 함수 안에서 함수 밖의 a 변수를 직접 사용하겠다는 뜻
프로그래밍을 할 때 global 명령어는 사용하지 않는 것이 좋다.
왜냐하면 함수는 독립적으로 존재하는 것이 좋기 때문
외부 변수에 종속적인 함수는 그다지 좋은 함수가 아니다.
"""

#lambda
"""
보통 함수를 한 줄로 간결하게 만들 때 사용
lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
"""
add = lambda a, b: a+b
result = add(3,4)
print(result)
"""
def add(a, b):
    return a+b

result = add(3, 4)
print(result)
이 것과 완전히 동일
"""
