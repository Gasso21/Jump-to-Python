"""
필요한 기능은?    문서 파일 읽어 들이기, 문자열 변경하기
입력 받는 값은?   탭을 포함한 문서 파일
출력하는 값은?    탭이 공백으로 수정된 문서 파일
"""
src = input()
dst = input()

f = open(src, 'r')
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " "*4)

g = open(dst, 'w')
g.write(space_content)
g.close()