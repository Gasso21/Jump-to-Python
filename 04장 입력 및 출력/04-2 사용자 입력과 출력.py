#사용자 입력
#1. input의 사용
a = input()
print(a)
"""
input은 입력되는 모든 것을 문자열로 취급
"""

#2. 프롬프트를 띄워서 사용자 입력 받기
number = input("숫자를 입력하세요: ")
print(number)

"""
input은 입력되는 모든 것을 문자열로 취급
number는 숫자가 아닌 문자열
"""

#print 자세히 알기
#1. 큰따옴표(")로 둘러싸인 문자열은 + 연산과 동일
print("life" "is" "too short")
print("life"+"is"+"too short")

#2. 문자열 띄어쓰기는 콤마로 한다
print("life", "is", "too short")

#3. 한 줄에 결과값 출력하기
for i in range(10):
    print(i, end=' ')