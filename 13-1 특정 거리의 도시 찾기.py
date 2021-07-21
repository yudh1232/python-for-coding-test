import sys
input = sys.stdin.readline
from collections import deque
INF = int(1e9)

# n, m, k, x를 공백으로 구분하여 입력받음
n, m, k, x = map(int, input().split())

# 그래프를 링크드 리스트 형태로 표현
graph = [[] for _ in range(n + 1)]
# 거리를 담는 리스트
distance_list = [INF] * (n + 1)
distance_list[x] = 0
# 방문 표시 리스트
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# BFS 수행
q = deque()
distance = 1
q.append((x, distance))
while q:
    # 큐에서 노드를 하나 뺌
    node, distance = q.popleft()
    # 방문하지 않았다면
    if not visited[node]:
        # 그 노드에 연결된 노드들을 큐에 넣음
        for i in graph[node]:
            distance_list[i] = min(distance_list[i], distance)
            q.append((i, distance + 1)) # 길이를 1 증가하여 큐에 넣음
        visited[node] = True # 방문 표시

# 최단 거리가 k인 도시가 존재하지 않으면
if k not in distance_list:
    print(-1)

# 결과 출력
for i in range(n + 1):
    if distance_list[i] == k:
        print(i)
