#Bool
a = True
b = False
print(type(a))

print(1==1)

"""
자료형의 참과 거짓
"python"     -> 참
""           -> 거짓
[1, 2, 3]    -> 참
[]           -> 거짓
()           -> 거짓
{}           -> 거짓
1            -> 참
0            -> 거짓
None         -> 거짓
"""

#예시
a = [1, 2, 3, 4]
while a:
    print(a.pop())

if []:
    print("참")
else:
    print("거짓")

if [1, 2, 3]:
    print("참")
else:
    print("거짓")

print(bool('python'))
print(bool(''))
