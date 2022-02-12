#Q1
dic = {'국어': 80, '영어': 75, '수학':55}
result = 0
for i in dic.values():
    result += i
print(result/len(list(dic.keys())))

#Q2
n = int(input())
if n % 2 == 0:
    print('짝수')
else:
    print('홀수')

#Q3
pin = "881120-1068234"
print(pin[:6], pin[7:])

#Q4
pin = "881120-1068234"
print(pin[7])

#Q5
a = "a:b:c:d"
print(a.replace(':','#'))

#Q6
l = [1, 3, 5, 4, 2]
l.sort()
l.reverse()
print(l)

#Q7
l = ['Life', 'is', 'too', 'short']
result = ' '.join(l)
print(result)

#Q8
t = (1,2,3)
print(t+(4,))

#09
"""
 딕셔너리의 키로는 변하는(mutable) 값을 사용할 수 없음
"""

#Q10
a = {'A':90, 'B':80, 'C':70}
print(a.pop('B'))
print(a)

#Q11
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(list(set(a)))

#Q12
a = b = [1, 2, 3]
a[1] = 4
print(b)

a = [1, 2, 3]
b = a[:]
a[1] = 4
print(b)