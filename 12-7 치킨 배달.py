import sys
input = sys.stdin.readline
from collections import deque
from itertools import combinations

# 상, 우, 하, 좌 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 집에서 부터 치킨집까지의 최소값을 구하는 함수
def calculate_cd(x, y):
    chicken_distance = 0
    q = deque()
    q.append((x, y, chicken_distance))
    # BFS 수행
    while q:
        x, y, chicken_distance = q.popleft()
        chicken_distance += 1
        for direction in range(4):
            nx = x + dx[direction]
            ny = y + dy[direction]
            # 범위를 벗어나는 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            # 치킨집을 만났을 경우
            if data[nx][ny] == 2:
                return chicken_distance
            # 치킨집이 아닌 경우 레벨 증가
            else:
                q.append((nx, ny, chicken_distance))

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

# 치킨집의 (x, y)좌표를 넣을 리스트
chicken_house = []

for x in range(n):
    for y in range(n):
        if data[x][y] == 2:
            chicken_house.append((x, y))
            data[x][y] = 0

# 치킨집 중에서 m개를 뽑는 조합을 구함
combination_list = list(combinations(chicken_house, m))

minimum = 100000

# 각 치킨집 조합에 대하여 도시의 치킨 거리가 가장 작게 되는 조합을 구함
for combination in combination_list:
    for i in range(m):
        x, y = combination[i]
        data[x][y] = 2
    
    sum = 0
    for x in range(n):
        for y in range(n):
            if data[x][y] == 1:
                sum += calculate_cd(x, y)

    minimum = min(minimum, sum)

    for i in range(m):
        x, y = combination[i]
        data[x][y] = 0
    
print(minimum) # 결과 출력
