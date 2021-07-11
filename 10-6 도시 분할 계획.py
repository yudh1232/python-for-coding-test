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

# n, m을 공백으로 구분하여 입력받음
n, m = map(int, input().split())

# parent 리스트, 각 노드에 대하여 부모를 자기 자신으로 초기화 
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i

# 길의 정보를 담을 리스트
array = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    array.append((cost, a, b))

# 크루스칼 알고리즘을 적용하기 위해 유지비를 기준으로 오름차순으로 정렬
array.sort()

# 크루스칼 알고리즘에 의해 선택된 간선들의 유지비를 담을 리스트
result = []
# 크루스칼 알고리즘 수행
for i in range(m):
    if find_parent(parent, array[i][1]) != find_parent(parent, array[i][2]):
        union_parent(parent, array[i][1], array[i][2])
        result.append(array[i][0])
    else:
        continue

# 마을을 두개로 분리하기 위해 마지막 선택된 간선을 제거
result.pop()

# 결과 출력
print(sum(result))

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

# 노드의 개수와 간선(Union 연산)의 개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()
last = 0 # 최소 신장 트리에 포함되는 간선 중에서 가장 비용이 큰 간선

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        last = cost

print(result - last)
"""
