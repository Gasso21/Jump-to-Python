#변수의 메모리 주소
a = [1, 2, 3]
print(id(a)) #id 함수는 변수가 가리키고 있는 객체의 주소 값을 돌려주는 파이썬 내장 함수

#리스트를 복사
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
"""
b와 a는 완전히 동일
리스트를 참조하는 변수가 a 변수 1개에서 b 변수가 추가되어 2개로 늘어났다는 차이가 존재
"""
print(a is b) #a와 b가 가리키는 객체는 동일한가?

a[1] = 4
print(a)
print(b)
"""
a 리스트의 2번째 요소를 값 4로 바꾸었더니 b도 동일하게 변경
즉, a와 b 모두 동일한 리스트를 가리키고 있기 때문에 발생한 일
"""

"""
b 변수를 생성할 때 a 변수의 값을 가져오면서 a와는 다른 주소를 가리키도록 설정
"""
# 1. [:] 이용 - 리스트 전체를 가리키는 [:]을 사용해서 복사
a = [1, 2, 3]
b = a[:]
a[1] = 4 #a 리스트 값을 바꾸더라도 b 리스트에는 영향을 끼치치 않음
print(a, id(a))
print(b, id(b))

# 2. copy 모듈 이용
from copy import copy
a = [1, 2, 3]
b = copy(a)
print(a, id(a))
print(b, id(b))

# 3. copy 함수 이용
a = [1, 2, 3]
b = a.copy()
print(a, id(a))
print(b, id(b))

#변수를 만드는 여러가지 방법
a, b = ('python', 'life')
(a, b) = 'python', 'life'
[a, b] = ['python', 'life']
a = b = 'python'

#변수 바꾸기
a = 3
b = 5
a, b = b, a
print(a)
print(b)