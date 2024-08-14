from collections import deque

'''
7 8
1 2
1 3
2 4
2 5
4 6
5 6
6 7
3 7
'''


# G : 그래프 정보
# v : 시작 정점 번호
# N : 정점의 개수
def bfs(G, v, N):
    # 중복방문 방지를 위한 방문 배열
    visited = [0] * (N + 1)
    # 내가 다음에 방문할 정점을 기억할 큐
    q = deque()
    # 큐에 시작 정점을 넣은 상태로 탐색 시작
    q.append(v)
    visited[v] = 1

    # 큐가 빌 때까지 계속 탐색 == 큐안에 방문할 곳이 남았으면 계속 탐색
    while q:
        # 큐에서 방문할 곳 하나 꺼내 오기
        now = q.popleft()
        ###############
        # now 에서 할일 처리
        ###############
        print(now, end=" ")

        # 현재 정점 now 에서 연결된 모든 정점 next 를 확인
        for next in G[now]:
            # next 정점을 이전에 방문한 적이 없으면 다음 방문 예약
            if not visited[next]:
                # 다음에 방문예약
                q.append(next)
                # 중복 방문 처리
                # next 까지의 거리 = now 까지 거리 + 1
                visited[next] = visited[now] + 1


V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for i in range(E):
    start, end = map(int, input().split())
    G[start].append(end)
    G[end].append(start)

bfs(G, 1, V)