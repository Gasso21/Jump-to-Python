#리스트 더하기(+)
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)

#리스트 반복하기(*)
a = [1, 2, 3]
print(a*3)

#리스트 길이 구하기
a = [1, 2, 3]
print(len(a))

#리스트 연산 오류
a = [1, 2, 3]
#print(a[2] + "hi") #'int'+'str' error
print(str(a[2])+"hi")

#리스트에서 값 수정
a = [1, 2, 3]
a[2] = 4
print(a)

#del 함수 사용해 리스트 요소 삭제
a = [1, 2, 3]
del a[1] #del 객체
print(a)

a = [1, 2, 3, 4, 5]
del a[2:]
print(a)

#리스트에 요소 추가(append)
a = [1, 2, 3]
a.append(4)
print(a)

#리스트 정렬(sort)
a = [1, 4, 3, 2]
a.sort() #오름차순
print(a)

a = ['a', 'c', 'b']
a.sort() #오름차순
print(a)

#리스트 뒤집기(reverse)
a = ['a', 'c', 'b']
a.reverse()
print(a)

#위치 반환(index)
a = [1, 2, 3]
print(a.index(3))
print(a.index(1))
#print(a.index(0)) #a 리스트에 존재하지 않으면 값오류(ValueError) 발생

#리스트에 요소 삽입(insert)
a = [1, 2, 3]
a.insert(0, 4) #0번째 자리에 값 4를 삽입
print(a)

a.insert(3, 5)
print(a)

#리스트 요소 제거(remove)
a = [1, 2, 3, 1, 2, 3]
a.remove(3) #리스트에서 첫 번째로 나오는 x를 삭제하는 함수
print(a)
a.remove(3)
print(a)

#리스트 요소 끄집어내기(pop)
a = [1, 2, 3]
print(a.pop()) #리스트의 맨 마지막 요소를 돌려주고 그 요소는 삭제
print(a)

a = [1, 2, 3]
print(a.pop(1)) #리스트의 x번째 요소를 돌려주고 그 요소는 삭제
print(a)

#리스트에 포함된 요소 x의 개수 세기(count)
a = [1, 2, 3, 1]
print(a.count(1)) #1이라는 값이 리스트 a에 2개 들어있음

#리스트 확장(extend)
a = [1, 2, 3]
a.extend([4, 5]) #x에는 리스트만 올 수 있음
print(a)
b = [6, 7]
a.extend(b)
print(a)

a = [1, 2, 3]
a += [4, 5]
print(a)