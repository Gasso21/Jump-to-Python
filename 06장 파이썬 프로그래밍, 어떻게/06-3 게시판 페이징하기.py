"""
함수 이름은? getTotalPage
입력 받는 값은? 게시물의 총 건수(m), 한 페이지에 보여줄 게시물 수(n)
출력하는 값은? 총 페이지수

게시물의 총 건수(m)	페이지당 보여줄 게시물 수(n)	총 페이지 수
    5	                10	                        1
    15	                10	                        2
    25	                10	                        3
    30	                10	                        3
"""
"""
m = int(input('게시물의 총 건수를 입력하시오: '))
n = int(input('페이지당 보여줄 게시물 수를 입력하시오: '))

result = divmod(m, n)
if result[1] != 0:
    print('총 페이지 수는 %d' %(result[0]+1)+'입니다.')
else:
    print('총 페이지 수는 %d' %(result[0])+'입니다.')
"""

def getTotalPage(m, n):
    if m % n == 0:
        return m // n
    else:
        return m // n + 1

print(getTotalPage(5, 10))
print(getTotalPage(15, 10))
print(getTotalPage(25, 10))
print(getTotalPage(30, 10))