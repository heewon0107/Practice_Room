# 파이썬의 리스트 메서드를 사용해서 큐 구현
# 성능이 좋지 않음

# 공백 상태의 큐
q = []

# 원소 10 개 추가
for i in range(1,11):
    q.append(i)

print(q)

# 원소 10 삭제
for i in range(10):
    print(q.pop(0))

print(q)