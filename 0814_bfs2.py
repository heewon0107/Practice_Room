from collections import deque

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

N = 7
maze = [[0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 99, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 1, ]
        ]


# (r,c) 가 유효한 위치(인덱스) 인가 검사
def is_vaild(r, c):
    return 0 <= r < N and 0 <= c < N


# 2차원 배열을 탐색
def bfs(sr, sc):
    # 중복체크
    visited = [[0] * N for _ in range(N)]
    # 큐생성
    q = deque()
    # 시작 위치 추가
    q.append((sr, sc))
    visited[sr][sc] = 1
    # 미로를 탈출할 때까지, 모든 위치를 탐색
    while q:
        # 아직 방문할 위치가 남아있다면 하나 꺼내와
        r, c = q.popleft()

        # (r,c) 에서 해야 할 일
        # (r,c) 가 도착 점인가?
        if maze[r][c] == 99:
            print(f"탈출 : ({r},{c}), 거리 : {visited[r][c]}")
            return True
        # (r,c)와 인접한 위치 확인
        # 인접한 위치는 상하좌우
        for d in range(4):
            # 다음 위치 계산
            nr = r + dr[d]
            nc = c + dc[d]

            # (nr,nr) 가 탐색 가능한 위치인가 판별
            # 1. 배열의 범위 안 (유효한 인덱스)
            # 2. 방문한 적이 없어야 한다.
            # 3. 벽이 아니어야 이동할 수 있다.
            if is_vaild(nr,nc) and not visited[nr][nc] and maze[nr][nc] != 1:
                # (nr, nc)는 다음에 방문
                q.append((nr, nc))
                # 중복 방문 방지 + 거리 계산
                visited[nr][nc] = visited[r][c] + 1

    # 반복중에 도착지점을 찾지 못했다.
    print("탈출 실패")
    return False

bfs(0,0)