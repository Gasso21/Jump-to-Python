#if문
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#조건문에서 아무 일도 하지 않게 설정
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

#elif 사용
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

#if문을 한 줄로 작성
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")

#조건부 표현식
"""
if score >= 60:
    message = "success"
else:
    message = "failure"
"""
message = "success" if score >= 60 else "failure"