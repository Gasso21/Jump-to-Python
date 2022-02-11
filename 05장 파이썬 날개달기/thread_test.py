# thread_test.py
"""
import time

def long_task():  # 5초의 시간이 걸리는 함수
    for i in range(5):
        time.sleep(1)  # 1초간 대기한다.
        print("working:%s\n" %(i+1) )

print("Start")

for i in range(5):  # long_task를 5회 수행한다.
    long_task()

print("End")
"""
"""
25" 소모
"""

"""
import time
import threading  # 스레드를 생성하기 위해서는 threading 모듈이 필요하다.

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)  # 스레드를 생성한다.
    threads.append(t)

for t in threads:
    t.start()  # 스레드를 실행한다.

print("End")
"""
"""
5초 소모
start 와 join이 먼저 출력
"""

import time
import threading

def long_task():
    for i in range(5):
        time.sleep(1)
        print("working:%s\n" % i)

print("Start")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()  # join으로 스레드가 종료될때까지 기다린다.

print("End")