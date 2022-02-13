#Q1
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
"""
shirt
"""

#Q2
n = 1
sum = 0
while n <= 1000:
    if n % 3 == 0:
        sum += n
    elif n == 1000:
        print("end")
    else:
        pass
    n += 1
print(sum)

#Q3
n = 1
while n <= 5:
    print("*"*n)
    n += 1

"""
i = 0
while True:
    i += 1 # while문 수행 시 1씩 증가
    if i > 5: break     # i 값이 5보다 크면 while문을 벗어난다.
    print('*' * i)     # i 값 개수만큼 *를 출력한다.
"""

#Q4
for i in range(1,101):
    print(i)

#Q5
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0
result = 0
for i in a:
    sum += i
result = sum/len(a)
print(result)

#Q6
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

"""
numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n%2==1]
print(result)
[2, 6, 10]
"""