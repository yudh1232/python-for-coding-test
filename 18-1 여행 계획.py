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
