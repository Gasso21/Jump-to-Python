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

