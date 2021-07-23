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
