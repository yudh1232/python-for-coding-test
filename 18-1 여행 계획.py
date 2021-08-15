INF = int(1e9) # 무한으로 10억을 설정

# n, m 을 입력받음
n, m = map(int, input().split())

# graph 2차원 리스트를 입력받음
graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    for j in range(1, n + 1):
        graph[i][j] = data[j - 1]

# 여행계획을 입력받음
plan = list(map(int, input().split()))
# 여행계획에서 중복제거
s = list(set(plan))

# parent 리스트 생성 및 자기자신으로 초기화
parent = []
for i in range(n + 1):
    parent.append(i)

# grapn 행렬을 순회
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 연결되어 있다면 parent를 업데이트
        if graph[i][j] == 1:
            if parent[i] < parent[j]:
                parent[j] = parent[i]
            elif parent[i] > parent[j]:
                parent[i] = parent[j]
            else:
                continue

flag = 1 # 여행 계획이 가능한지 나타내는 변수
# 여행 계획에 있는 원소들의 parent가 다르면 불가능
for i in s:
    if parent[i] != parent[s[0]]:
        print('NO')
        flag = 0
        break

# 여행 계획에 있는 원소들의 parent가 모두 같으면 가능
if flag == 1:
    print('YES')

# 해설
"""
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 여행지의 개수와 여행 계획에 속한 여행지의 개수 입력받기
n, m = map(int, input().split())
parent = [0] * (n + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

# Union 연산을 각각 수행
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: # 연결된 경우 합집합(Union) 연산 수행
            union_parent(parent, i + 1, j + 1)

# 여행 계획 입력받기
plan = list(map(int, input().split()))

result = True
# 여행 계획에 속하는 모든 노드의 루트가 동일한지 확인
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        result = False

# 여행 계획에 속하는 모든 노드가 서로 연결되어 있는지(루트가 동일한지) 확인
if result:
    print("YES")
else:
    print("NO")
"""
