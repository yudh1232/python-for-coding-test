# g와 p를 입력받음
g = int(input())
p = int(input())

# n번 탑승구가 도킹되어있는지 나타내는 리스트
gate = [0] * (g + 1)

count = 0 # 도킹한 비행기 수
flag = 0 # 더 이상 도킹할 수 없는지 나타내는 플래그

for _ in range(p):
    gi = int(input())
    for i in range(gi, 0, -1):
        # gate gi가 비어있으면 도킹하고, 안 비어있으면 gate (gi - 1)을 살펴보러 감
        if gate[i] == 0:
            gate[i] = 1
            break
        else:
            # gi이하의 모든 게이트가 다 안 비어있으면 
            if i == 1:
                flag = 1
    
    # 더 이상 도킹할 수 없으면
    if flag == 1:
        break
    
    # 도킹한 비행기 수 증가
    count += 1

print(count) # 결과 출력

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

# 탑승구의 개수 입력받기
g = int(input())
# 비행기의 개수 입력받기
p = int(input())
parent = [0] * (g + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, g + 1):
    parent[i] = i

result = 0
for _ in range(p):
    data = find_parent(parent, int(input())) # 현재 비행기의 탑승구의 루트 확인
    if data == 0: # 현재 루트가 0이라면, 종료
        break
    union_parent(parent, data, data - 1) # 그렇지 않다면 바로 왼쪽의 집합과 합치기
    result += 1

print(result)
"""
