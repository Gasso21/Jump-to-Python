"""
x = input()
List = []
def GuGu(x):
    for i in range(1,10):
        List.append(i*int(x))
    return List
print(GuGu(x))
"""

def GuGu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i = i + 1
    return result

print(GuGu(2))