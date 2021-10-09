"""
Dictionary
{key:value}
"""
#딕셔너리 쌍 추가하기
a = {1:'a'}
a[2] = 'b' #딕셔너리 a에 Key와 Value가 각각 2와 'b'라는 딕셔너리 쌍이 추가
print(a)

#딕셔너리 요소 삭제하기
del a[1] #Key에 해당하는 {key:Value} 쌍이 삭제
print(a)

#딕셔너리 사용 예시
a = {1:'a', 2:'b'}
print(a[1])

#딕셔너리 만들 때 주의사항
a = {1:'a', 1:'b'}
print(a)
"""
1. Key는 고유한 값이므로 중복되는 Key 값을 설정해 놓으면 하나를 제외한 나머지 것들이 모두 무시됨
2. Key에 리스트는 쓸 수 없음. 하지만 튜플은 Key로 사용 가능
    즉, Key에는 변하지 않는 값이 들어가야 함
"""
#a = {[1, 2] : 'hi'}

#Key 리스트 만들기(keys)
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
print(a.keys())
"""
a.keys()는 딕셔너리 a의 Key만 모아서 dict_keys 객체를 반환
파이썬 2.7까지는 a.keys()함수를 호출할 때 반환 값으로 dict_keys가 아닌 리스트를 돌려줌
리스트를 돌려주기 위해서는 메모리 낭비가 발생
파이썬 3.0이후 버전에서는 이러한 메모리 낭비를 줄이기 위해 dict_keys 객체를 돌려줌
반환값으로 리스트가 필요한 경우에는 list(a.keys())를 사용
"""
for k in a.keys():
    print(k)
"""
리스트를 사용하는 것과 차이가 없지만, 리스트 고유의 append, insert, pop, remove, sort 함수 등은 사용 불가
"""
print(list(a.keys()))

#Key, Value 쌍 얻기(items)
print(a.items())

#Key:Value 쌍 모두 지우기(clear)
a.clear()
print(a)

#Key로 Value얻기(get)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('name'))

#인덱스로 가져오는 것과 get함수의 차이
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print(a.get('nokey'))
#print(a['nokey']) #KeyError: 'nokey'오류 발생
"""
딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때에는 get(x, '디폴트 값')을 사용하면 편리
"""
print(a.get('foo', 'bar'))

#해당 Key가 딕셔너리 안에 있는지 조사하기(in)
a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
print('name' in a)
print('email' in a)