# all
print("ALL")
"""
반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다

*iterable 자료형
for문으로 그 값을 출력할 수 있는 것을 의미
EX) 리스트, 튜플, 문자열, 딕셔너리, 집합 등
"""
print(all([1, 2, 3]))
print(all([1, 2, 3, 0]))
print(all([]))
"""
리스트형 자료 중 요소 0은 거짓이므로 False를 돌려줌
입력 인수가 빈 값인 경우에는 True를 리턴
"""

# any
print("\n"+"ANY")
"""
반복 가능한(iterable) 자료형 x를 입력 인수로 받으며 이 x의 요소 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때에만 False를 돌려준다.
all(x)의 반대이다.
"""
print(any([1, 2, 3, 4]))
print(any([1, 2, 3, 0]))
print(any([0, ""]))
print(any([]))

# dir
print("\n"+"DIR")
"""
dir은 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌
"""
print(dir([1, 2, 3, 4]))
print(dir(['1', 'a']))

# divmod
print("\n"+"DIVMOD")
"""
divmod(a, b)는 2개의 숫자를 입력으로 받는다.
a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려주는 함수
"""
print(divmod(7, 3))
print(7/3)
print(7//3)
print(7%3)

# enumerate
print("\n"+"ENUMERATE")
"""
순서가 있는 자료형(리스트, 튜플, 문자열)을 입력으로 받아 인덱스를 포함하는 enumerate 객체를 반환
*보통 enumerate 함수는 다음 예제처럼 for문과 함께 자주 사용
"""
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# eval
print("\n"+"EVAL")
"""
eval(expression)은 실행 가능한 문자열(1+2, 'hi' + 'a' 같은 것)을 입력으로 받아 문자열을 실행한 결과값을 돌려주는 함수
*입력받은 문자열로 파이썬 함수나 클래스를 동적으로 실행하고 싶을 때 사용
"""
print(eval('1+2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))

# filter
print("\n"+"FILTER")
"""
첫 번째 인수로 함수 이름을
두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다.
그리고 두 번째 인수인 반복 가능한 자료형 요소가 첫 번째 인수인 함수에 입력되었을 때 반환값이 참인 것만 묶어서(걸러 내서) 돌려준다.
"""
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

print(positive([1, -3, 2, 0, -5, 6]))

def positive(x):
    return x>0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# int
print("\n"+"INT")
"""
2진수로 표현된 11의 10진수 값
"""
print(int('11', 2))

"""
16진수로 표현된 1A의 10진수 값
"""
print(int('1A', 16))

# isinstance
print("\n"+"ISINSTANCE")
"""
isinstance(object, class)는 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다.
입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 돌려준다.
"""
class Person: pass
a = Person()
print(isinstance(a, Person))

b = 3
print(isinstance(b, Person))

# len
print("\n"+"LEN")
print(len("python"))
print(len([1, 2, 3]))
print(len((1, 'a')))

# map
print("\n"+"MAP")
"""
map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다.
map은 입력받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수
"""
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

def two_times(x):
    return x*2

print(list(map(two_times, [1, 2, 3, 4])))

print(list(map(lambda a: a*2, [1, 2, 3, 4])))

# ord & chr
print("\n"+"ORD & CHR")
"""
ord(c)는 문자의 유니코드 값을 돌려주는 함수
chr(i)는 유니코드 값을 받아 문자를 출력하는 함수
"""
print(ord('a'))

# pow
print("\n"+"POW")
print(pow(2, 4))

# sorted
print("\n"+"SORTED")
"""
sorted(iterable) 함수는 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수
"""
print(sorted([3, 1, 2]))
print(sorted(['a', 'c', 'b']))
print(sorted("zero"))
print(sorted((3, 2, 1)))

# zip
print("\n"+"ZIP")
"""
zip(*iterable)은 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수이다.
"""
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip("abc", "def")))