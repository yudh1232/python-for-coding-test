from collections import deque

n, m = map(int, input().split())
# 그래프를 2차원 리스트로 선언
graph = [[] for _ in range(n + 1)]

# 그래프 정보를 입력받음
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 각 학생이 누구에게 연결될 수 있는지 저장하는 리스트
reachable = [[] for _ in range(n + 1)]
q = deque()

# graph를 순회하여 각 학생이 누구에게 연결될 수 있는지 확인
for node in range(1, n + 1):
    for e in graph[node]:
        q.append(e)
        while q:
            now = q.popleft()
            if now not in reachable[node]:
                reachable[node].append(now)
                for edge in graph[now]:
                    q.append(edge)

# recheable을 바탕으로 각 학생의 indegree를 계산
indegree = [0] * (n + 1)
for i in range(1, n + 1):
    for dest in reachable[i]:
        indegree[dest] += 1

count = 0       
for i in range(1, n + 1):
    # outdegree(len(recheable[i]))와 indegree의 합이 n - 1이면 성적 순위를 알 수 있음
    if len(reachable[i]) + indegree[i] == n - 1:
        count += 1

print(count) # 결과 출력

# 해설
"""
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]
 
# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0
 
# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용을 1로 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
 
# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
# 각 학생을 번호에 따라 한 명씩 확인하며 도달 가능한지 체크
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    if count == n:
        result += 1
print(result)
"""
