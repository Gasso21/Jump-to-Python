#Q1
def is_odd(x):
   if x % 2 == 0:
       return 'even'
   else:
       return 'odd'
x = int(input())
y = is_odd(x)
print(y)

#Q2
n = input()
sum = 0
e = 0
for i in n:
    if i == ' ':
        e += 1
    else:
        sum += int(i)
print(sum/(len(n)-e))

"""
def avg_numbers(*args):   # 입력 개수에 상관없이 사용하기 위해 *args를 사용
    result = 0
    for i in args:
        result += i
    return result / len(args)
    
print(avg_numbers(1,2,3,4))
"""

#Q3
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %d 입니다" %total)

#Q4
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))
"""
3번째
"""

#Q5
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')

print(f2.read())
f2.close()

"""
with open("test.txt", 'w') as f1:
    f1.write("Life is too short! ")
with open("test.txt", 'r') as f2:
    print(f2.read())
"""

#Q6
s = 'Life is too short\nyou need java'
print(s.replace('java', 'python'))