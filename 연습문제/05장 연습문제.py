#Q1
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value) # 10에서 7을 뺀 3을 출력

#Q2
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value >= 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기
print(cal.value) # 100 출력

#Q3
print(all([1, 2, abs(-3)-3]))
"""
False
"""
print(chr(ord('a')) == 'a')
"""
True
"""

#Q4
l = [1, -2, 3, -5, 8, -3]
print(list(filter(lambda x: x > 0, l)))

#Q5
print(hex(234))
print(int('0xea', 16))

#Q6
print(list(map(lambda x: x*3, [1, 2, 3, 4])))

#Q7
mi = 0
ma = 0
for i in [-8, 2, 7, 5, -3, 5, 0, 1]:
    if i < mi:
        mi = i
    elif i > ma:
        ma = i

print(mi+ma)
"""
a = [-8, 2, 7, 5, -3, 5, 0, 1]
print(max(a) + min(a))
"""

#Q8
print(round(17/3, 4))

#Q9
import sys
x = sys.argv
s = 0
for i in x[1:]:
    s += int(i)
print(s)

"""
import sys

numbers = sys.argv[1:] # 파일 이름을 제외한 명령 행의 모든 입력

result = 0
for number in numbers:
    result += int(number)
print(result)
"""

#Q10
"""
import os
os.chdir('C:/doit')
#os.system('dir')
f = os.popen('dir')
print(f.read())
"""

#Q11
import glob
print(glob.glob("c:/doit/*.py"))

#Q12
import time
print(time.strftime('%Y/%m/%d %X', time.localtime(time.time())))
"""
2018/04/03 17:20:32
"""

#Q13
"""
random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성.
(단 중복된 숫자가 있으면 안 됨)
"""
import random
i = 1
l = []
while i <= 6:
    r = random.randint(1, 45)
    if r in l:
        pass
    else:
        l.append(r)
        i += 1

print(l)