from itertools import combinations
import copy

def dfs(x, y):
    # 연구소를 벗어나거나, 벽이거나, 이미 방문했으면 리턴
    if x < 0 or y < 0 or x >= n or y >= m or temp[x][y] == 1 or temp[x][y] == 3:
        return
    # 방문표시
    temp[x][y] = 3
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)

# n, m을 공백으로 구분하여 입력받음
n, m = map(int, input().split())

# 연구소 정보를 입력받아 2차원 리스트에 넣음
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 빈칸 좌표를 모아 리스트에 넣음
blank = []
for x in range(n):
    for y in range(m):
        if data[x][y] == 0:
            blank.append((x, y))

# 안전 영역 크기의 최대값을 구하기 위해 0으로 초기화
max_safe = 0
# 벽을 세울 수 있는 모든 조합에 대하여
for coordinate in combinations(blank, 3):
    temp = copy.deepcopy(data)
    # 벽 3개를 세움
    temp[coordinate[0][0]][coordinate[0][1]] = 1
    temp[coordinate[1][0]][coordinate[1][1]] = 1
    temp[coordinate[2][0]][coordinate[2][1]] = 1
    
    # dfs 수행
    for x in range(n):
        for y in range(m):
            if data[x][y] == 2:
                dfs(x, y)
    
    # 안전 영역 크기를 구함
    safe_count = 0
    for x in range(n):
        for y in range(m):
            if temp[x][y] == 0:
                safe_count += 1
                
    # 안전 영역 크기의 최대값을 구함
    max_safe = max(max_safe, safe_count)

print(max_safe) # 결과 출력

# 해설
"""
n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상, 하, 좌, 우 중에서 바이러스가 퍼질 수 있는 경우
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매 번 안전 영역의 크기 계산
def dfs(count):
    global result
    # 울타리가 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역의 최대값 계산
        result = max(result, get_score())
        return
    # 빈 공간에 울타리를 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)
"""
