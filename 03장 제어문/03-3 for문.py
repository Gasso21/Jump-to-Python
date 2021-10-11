#for문
"""
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
    ...
"""
#전형적인 for문
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

#다양한 for문의 사용
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

#for문의 응용
"""
총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지 결과를 보여 주시오.
"""
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)

#continue문을 통해 for문의 처음으로 돌아감
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number +1
    if mark < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다. " % number)

#for문과 함께 자주 사용하는 range 함수
a = range(10)
print(a)

#예시
add = 0
for i in range(1, 11):
    add = add + i
print(add)

marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))

#for와 range를 이용한 구구단
for i in range(2, 10):
    for j in range(1, 10):
        print("{0:2d}" .format(i*j), end=" ") #해당 결과값을 출력할 때 다음줄로 넘기지 않고 그 줄에 계속해서 출력하기 위해 사용
    print('') #두 번째 for문이 끝나면 결과값을 다음줄부터 출력하게 함

#리스트 내포 사용
a = [1,2,3,4]
result = list()
for num in a:
    result.append(num*3)
print(result)

a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)
"""
[표현식 for 항목 in 반복가능객체 if 조건문]

[표현식 for 항목1 in 반복가능객체1 if 조건문1
        for 항목2 in 반복가능객체2 if 조건문2
        ...
        for 항목n in 반복가능객체n if 조건문n]
"""

result = [x*y for x in range(2,10)
              for y in range(1,10)]
print(result)
