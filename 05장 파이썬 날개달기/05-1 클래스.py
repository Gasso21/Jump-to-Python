"""
C 언어에는 클래스가 없다. -> 클래스가 꼭 필요한 것은 아니다.
계산기는 이전에 계산한 결과값을 항상 메모리 어딘가에 저장하고 있어야 한다.
"""

#클래스를 사용하지 않을 때
result = 0
def add(num):
    global result
    result += num
    return result

print(add(3))
print(add(4))
"""
>> 3
>> 7
"""

result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print(add2(3))
print(add2(7))
"""
한 프로그램에서 2대의 계산기가 필요한 경우 위와 같이 서로 다른 2개의 함수를 만들어야함
"""
print()
#클래스를 사용할 때
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))
"""
Calculate 클래스로 만든 객체 cal1, cal2가 각각의 역할을 수행
두 객체는 독립적인 값을 유지
빼기 기능을 추가할 때는,
    def sub(self, num):
        self.result -= num
        return self.result

클래스는 과자 틀과 같아서 무엇인가를 계속해서 만들어 낼 수 있는 설계 도면
객체는 클래스로 마들어낸 피조물
클래스로 만들어낸 객체는 그마다 고유한 성격을 가짐
"""
class Cookie:
    pass

a = Cookie()
b = Cookie()

print(type(a))
"""
<class '__main__.Cookie'>
"""
"""
객체와 인스턴스의 차이

클래스로 만든 객체를 인스턴스라고 함
a = Cookie()
여기서 a는 객체
여기서 a는 Cookie의 인스턴스
즉, 인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용
-> a는 객체
-> a는 Cookie의 인스턴스
"""

#사칙연산 클래스 만들기
#1. 클래스를 어떻게 만들지 먼저 구상하기
"""
a = FourCal()
a.setdata(4,2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
"""
#2. 클래스 구조 만들기
"""
class FourCal:
    pass

a = FourCal()
type(a)
>> <class '__main__.FourCal'>
"""
#3. 객체에 숫자 지정할 수 있게 만들기
"""
a.setdata(4,2)

"""
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
"""
def 함수명(매개변수):
    수행할 문장
    ...
    
메서드(Method): 클래스 안에 구현된 함수
"""
"""
a = FourCal()
a.setdata(4, 2)

a.setdata(4, 2) 처럼 호출하면 setdata 메서드의 첫 번째 매개변수 self에는 setdata 메서드를 호출한 객체 a가 자동으로 전달됌

[매서드의 또 다른 호출 방법]
a = FourCal()
FourCal.setdata(a, 4, 2)
클래스이름.메서드 형태로 호출할 때는 객체 a를 첫 번째 매개변수 self에 꼭 전달해 주어야 함

a = FourCal()
a.setdata(4, 2)
객체.메서드 형태로 호출할 때는 self를 반드시 생략해서 호출해야 함
"""
"""
def setdata(self, first, second):   # ① 메서드의 매개변수
    self.first = first              # ② 메서드의 수행문
    self.second = second            # ② 메서드의 수행문

self.first = 4
self.second = 2

self는 전달된 객체 a이므로 다음과 같이 해석
a.first = 4
a.second = 2

객체에 생성되는 객체만의 변수를 객체변수라고 칭함
"""

a = FourCal()
a.setdata(4, 2)
print(a.first)
# >> 4
print(a.second)
# >> 2

a = FourCal()
b = FourCal()
a.setdata(4, 2)
print(a.first)

FourCal.setdata(b, 3, 7)
print(b.first)
"""
핵심은, 클래스로 만든 객체의 객체변수는 다른 객체의 객체변수에 상관없이 독립적인 값을 유지
"""
#id 함수를 통해 객체변수가 독립적인 값을 유지한다는 점을 입증
a = FourCal()
b = FourCal()
a.setdata(4, 2)
b.setdata(3, 7)
print(id(a.first),"\n"+str(id(b.first)))
#4. 더하기 기능 만들기
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result

a = FourCal()
a.setdata(2, 3)
print(a.add())

#생성자 (Constructor)
"""
a = FourCal()
a.add()
"""
"""
FourCal 클래스의 인스턴스 a에 setdata 메서드를 수행하지 않고 add 메서드를 수행하면 
>> "AttributeError: 'FourCal' object has no attribute 'first'
오류가 발생한다.
이렇게 객체에 초기값을 설정해야 할 필요가 있을 때는 setdata와 같은 메서드를 호출하여 초기값을 설정하기 보다는
생성자를 구현하는 것이 안전한 방법이다.
생성자(Constructor)란 객체가 생성될 때 자동으로 호출되는 메서드를 의미한다.

파이썬 메서드 이름으로 __init__ 를 사용하면 이 메서드는 생성자가 된다
"""
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def setdata(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result

"""
__init__ 메서드는 setdata 메서드와 이름만 다르고 모든 게 동일하다.
단, 메서드 이름을 __init__으로 했기 때문에 생성자로 인식되어 객체가 생성되는 시점에 자동으로 호출되는 차이가 있다.
"""
"""
a = FourCal()
TypeError: __init__() missing 2 required positional arguments: 'first' and 'second'
오류가 발생한 이유는 생성자의 매개변수 first와 second에 해당하는 값이 전달되지 않았기 때문
"""
a = FourCal(4, 2)
"""
매개변수	값
self	생성되는 객체
first	4
second	2
"""
print(a.add())

#클래스의 상속
class MoreFourCal(FourCal):
    pass
"""
클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 된다.
class 클래스 이름(상속할 클래스 이름)
"""
a = MoreFourCal(4, 2)
print(print(a.mul()))
"""
왜 상속을 해야 할까

보통 상속은 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용
기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용
"""
class MorFourCal(FourCal):
    def pow(self):
        result = self.first**self.second
        return result

a = MorFourCal(4, 2)
print(a.pow())

#메서드 오버라이딩
a = FourCal(4, 0)
"""
print(a.div())
"""
"""
ZeroDivisionError: division by zero
div 메서드를 호출하면 4fmf 0으로 나누려고 하기 때문에 위와 같은 ZeroDivisionError 오류가 발생한다.
"""
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
"""
부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩(Overriding, 덮어쓰기)이라고 한다.
이렇게 메서드를 오버라이딩하면 부모클래스의 메서드 대신 오버라이딩한 메서드가 호출된다.
"""
a = SafeFourCal(4, 0)
print(a.div())

#클래스 변수
class Family:
    lastname = "김"
"""
클래스 변수는 클래스 안에 함수를 선언하는 것과 마찬가지로 클래스 안에 변수를 선언하여 생성
"""
print(Family.lastname)
"""
클래스이름.클래스변수 로 사용할 수 있음
"""
a = Family()
b = Family()
print(a.lastname)
print(b.lastname)

Family.lastname = "박"
print(a.lastname)
print(b.lastname)
"""
클래스 변수 값을 변경했더니 클래스로 만든 객체의 lastname 값도 모두 변경된다는 것을 확인할 수 있다.
즉 클래스 변수는 클래스로 만든 모든 객체에 공유된다는 특징이 있다
"""

print(id(Family.lastname))
print(id(a.lastname))
print(id(b.lastname))
"""
id 값(주소)이 모두 같으므로 위 셋은 모두 같은 메모리를 가리키고 있다.
"""