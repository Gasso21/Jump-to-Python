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

#매개변수에 초깃값 미리 설정하기
