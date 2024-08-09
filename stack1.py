# 파이썬에서 리스트 메서드 사용해서 스택 만들기

# 1. 스택 초기화 (선언) : 빈 리스트를 스택으로 사용
s=[]    # 사용 가능한 메서드 append, pop, [-1]( -1 : 마지막 꺼를 사용한다는 뜻)


# 스택에 원소 삽입하기 : push
for i in range(10):
    s.append(i)

print(s)

# 스택에 원소 삭제하기 : pop
# for i in range(10):
#     print(s.pop(), end =" ")
# print()
#
# print(s)

# 스택에서 원소를 모두 꺼내고 싶은데 몇개 있는지 몰라
# [] 빈 리스트는 False로 취급이 된다.
while s:    # 비어있으면 False
    print(s.pop(), end=" ")
print()
print(s)