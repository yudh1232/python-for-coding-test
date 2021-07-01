from collections import deque

# n, m을 공백으로 구분하여 입력받음
n, m = map(int, input().split())

# 얼음 틀을 입력받음
frame = []
for _ in range(n):
    frame.append(list(map(int, input())))

# 그래프의 노드 번호를 위한 리스트
array = []
for i in range(n):
    array.append([])
    for j in range(m):
        array[i].append(m * i + j + 1)

# 연결 상태를 나타내는 그래프
graph = []
graph.append([])

# 상하좌우를 체크하여 연결 상태를 나타냄
for i in range(n):
    for j in range(m):
        linked = []
        if frame[i][j] == 0:
            if i - 1 >= 0:
                if frame[i - 1][j] == 0:
                    linked.append(array[i - 1][j])
            if j - 1 >= 0:
                if frame[i][j - 1] == 0:
                    linked.append(array[i][j - 1])
            if j + 1 < m:
                if frame[i][j + 1] == 0:
                    linked.append(array[i][j + 1])
            if i + 1 < n:
                if frame[i + 1][j] == 0:
                    linked.append(array[i + 1][j])
            graph.append(linked)
        else:
            graph.append([])

# BFS
def bfs(graph, start, visited):
    global count
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    count += 1

# 방문 여부를 나타내는 리스트
visited = [False] * (n * m + 1)

# 결과 값
count = 0

# 모든 노드에 대하여 0이면서 방문하지 않았으면 bfs를 수행
for i in range(n):
    for j in range(m):
        if frame[i][j] == 0 and visited[m * i + j + 1] == False:
            bfs(graph, m * i + j + 1, visited)

print(count) #결과 출력

# 해설
"""
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력
"""
