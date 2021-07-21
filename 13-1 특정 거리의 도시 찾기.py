import sys
input = sys.stdin.readline
from collections import deque

# n, m, k, x를 공백으로 구분하여 입력받음
n, m, k, x = map(int, input().split())

# 그래프를 링크드 리스트 형태로 표현
graph = [[] for _ in range(n + 1)]
# 거리를 담는 리스트
distance_list = [-1] * (n + 1)
distance_list[x] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# BFS 수행
q = deque()
q.append(x)
while q:
    # 큐에서 노드를 하나 뺌
    now = q.popleft()
    # 현재 노드에서 방문할 수 있는 모든 노드를 체크
    for next_node in graph[now]:
        # 방문하지 않았다면
        if distance_list[next_node] == -1:
            # 최단 거리 갱신
            distance_list[next_node] = distance_list[now] + 1
            q.append(next_node)

# 결과 출력
check = False
for i in range(n + 1):
    if distance_list[i] == k:
        print(i)
        check = True

# 최단 거리가 k인 도시가 존재하지 않으면
if check == False:
    print(-1)

# 해설
"""
from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력 받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False:
    print(-1)
"""
