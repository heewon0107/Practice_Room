# 그래프를 빠짐없이 한번씩 모두 방문 하는게 목표
# 그 방법중 하나 dfs = depth first search
# adjust_matrix

# 그래프를 표현하는 방법
# 인접 리스트, 인접 행렬

# 인접 행렬 ,그래프의 정점이 N개라고 하면
# adj_m = [[] * N for _ in range(N)]
# adj_m[1][2] = 1
# 그래프의 1번 정점에서 2번 정점으로 바로 가는 간선이 존재한다. (연결되어있음)
# adj_m[2][3] = 1
# 그래프의 2번 정점에서 3번 정점으로 바로 가는 간선이 존재한다. (연결 되어 있음)
# adjm_m[3][4] = 0
# 그래프의 3번 정점에서 4번 정점으로 바로 가는 간선이 없다. (연결 안 되어있음)

# 4번에서 5번으로 가는 길이 있다, 무향 그래프라면 5번에서 4번으로 가는 길도 있음
# adj_m[4][5] = 1, adj_m[5][4] = 1
#       A B C D E F G
adj_m = [[0, 1, 1, 0, 0, 0, 0],  # A와의 연결점
         [1, 0, 0, 1, 1, 0, 0],  # B와의 연결점
         [1, 0, 0, 0, 1, 0, 0],  # C와의 연결점
         [0, 1, 0, 0, 0, 1, 0],  # D와의 연결점
         [0, 1, 1, 0, 0, 1, 0],  # E와의 연결점
         [0, 0, 0, 1, 1, 0, 1],  # F와의 연결점
         [0, 0, 0, 0, 0, 1, 0]]  # G와의 연결점

# 1. 인접 행렬을 사용한 DFS
# s : 탐색 시작 정점.
# v : 정점의 개수
# def dfs_m(s, V):
#     # 방문체크
#     visited = [0] * (V+1)
#     print(s)
#     # 다시 돌아올 정점 번호를 저장할 스택
#     stack = []
#
#     # 시작 정점은 방문 처리
#     visited[s] = 1
#
#     # 현재 방문하고 있는 정점 v
#     v = s
#
#     while True:
#         # 현재 있는 정점(v) 에서 방문할 수 있는 정점이 있나 확인
#         # 나머지 정점 번호를 i라고 할 때 adj_m[v][i] == 1 인가 확인
#         # i번째 정점을 이전에 방문한 적이 없나나 확인 visited[i] = 0 이면 방문가능
#         for i in range(1, V+1):
#             # v 정점에서 i 정점으로 가는 길이 있고, i 정점을 방문한 적이 없는지 검사
#             if adj_m[v][i] == 1 and visited[i] == 0:
#                 # 갔다가 길이 없으면 돌아올 곳을 기억해야 한다.
#                 # v 정점을 돌아올 곳으로 기억 => 스택에 저장.
#                 stack.append(v)
#                 ###################
#                 # i번 정점에서 하고싶은 일
#                 print(i)
#                 ###################
#                 visited[i] = 1
#
#                 # 현재 정점을 i로 바꾸고 다시 탐색 시작(반복)
#                 v = i
#                 # 새로운 v에서 탐색을 해야하기 때문에 break
#                 break
#         else:   # for - else : 중간에 break 한적이 없다.
#                 # 현재 정점 v에서 갈 수 있는 i 정점을 찾지 못했다.
#                 # 제일 최근 정점으로 돌아가기
#                 # 돌아갈 때 돌아갈 곳이 있나 먼저 확인
#             if stack:
#                 # 스택안에 원소가 있다 => 돌아갈 곳이 있다.
#                 v = stack.pop()
#             else:
#                 # 스택안에 원소가 없다. => 돌아갈 곳이 없다.
#                 # 남은 정점이 없다. 탐색 완료
#                 break
#
# dfs_m(0,7)

# # v = 정점 개수
# # e = 간선 개수
# v, e = map(int, input().split())
# adj_m = [[0] * (v+1) for _ in range(v+1)]
#
# for i in range(e):
#     # 시작 s, 도착 e
#     s, e = map(int, input().split())
#
#     adj_m[s][e] = 1
#     adj_m[e][s] = 1
#
# dfs_m(1, v)

# 인접 리스트
# 1번 정점에서 2번 정점으로 가는 길이 있다.
# 1번 정점에서 3번 정점으로 가는 길도 있다.
# adj_l[1] = [2,3]
# 5번 정점에서 갈 수 있는 정점이 없다.
# adj_l[5] = []
# adj_l[[] for _ in range(V)]

def dfs_l(s,V):
    # 방문 배열
    visited = [0]*(V+1)

    # 스택
    stack = []

    # 시작 정점 체크
    visited[s] = 1

    # 현재 정점을 v라고 하자.
    v = s
    print(v)

    # 탐색
    while True:
        # 현재 정점 v에서 갈 수 있는 정점들
        # 현재 정점 v와 연결된 정점을 i라고 하자
        for i in adj_l[v]:
            # i는 v와 연결되어 있기 때문에 연결 검사 x
            # i가 이전에 방문한 적이 없다면 가자
            if not visited[i] == 0:
                # 돌아올 위치 기억
                stack.append(v)
                print(i)

                visited[i] = 1
                v = i
                # 새로 바뀐 v에서 연결된 정점을 찾아야 하기 때문에 break
                break
        else:
            # 여기가 실행된다는 것은 중간에 break를 만난 적이 없다.
            # break 를 만난적이 없다. => 갈 수 있는 i 정점을 못찾았다.
            # 되돌아가야한다. 되돌아 갈 곳이 있다면,
            if stack:
                v = stack.pop()
            else:
                # 되돌아 갈 곳이 없다면 탐색 완료
                break

V, E = map(int, input().split())
adj_l = [[] for _ in range(V+1)]

for i in range(E):
    s, e = map(int, input().split())
    # s에서 갈 수 있는 정점 e 추가
    adj_l[s].append(e)
    # e에서 갈 수 있는 정점 s 추가
    adj_l[e].append(s)

dfs_l(1,V)