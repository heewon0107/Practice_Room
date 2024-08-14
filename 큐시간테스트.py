import time
from collections import deque
start = time.time()

N = 30000


# 1. 파이썬의 리스트 사용
q1 = []

for i in range(N):
    q1.append(N)

for i in range(N):
    q1.pop(0)

end = time.time()

print(f"걸린 시간 {end - start:0.5f}")

# 2. 배열과 front, rear 사용
q2 = [0] * N

front = rear = -1

start = time.time()
for i in range(N):
    rear += 1
    q2[rear] = i

for i in range(N):
    front += 1
    q2[front] = 1
end = time.time()

print(f"2번 걸린 시간 : {end - start:.5f}")

# deque 사용
start = time.time()

q3 = deque()

for i in range(N):
    q3.append(i)

for i in range(N):
    q3.popleft()

end = time.time()

print(f"3번 걸린 시간 : {end - start:.5f}")