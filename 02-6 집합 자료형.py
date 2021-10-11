#집합 자료형
s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello")
print(s2) #중복을 허용하지 않음, 순서가 없음(Unordered) -> 인덱싱으로 값을 얻을 수 없음

s3 = set([1, 1, 2, 3, 4, 4,])
print(s3)

#비어있는 집합 자료형
s = set()
print(s)

s1 = set([1, 2, 3])
l1 = list(s1) #set 자료형에 저장된 값을 인덱싱으로 접근하려면 리스트나 튜플로 변환 후 해야 함
print(l1)
print(l1[0])

t1 = tuple(s1)
print(t1)
print(t1[0])
"""
중복을 허용하지 않는 set의 특징은 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용
"""
#교집합, 합집합, 차집합
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

#교집합
print(s1&s2)
print(s1.intersection(s2))

#합집합
print(s1|s2)
print(s1.union(s2))

#차집합
print(s1.difference(s2))
print(s2.difference(s1))

#값 1개 추가하기(add)
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

#값 여러 개 추가하기(update)
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

#특정 값 제거하기(remove)
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)