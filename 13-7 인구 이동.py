import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 연합을 찾는 dfs 알고리즘
def find_group(r, c, population, group_num):
    # 땅을 벗어나는 경우, 이미 방문한 곳인 경우 종료
    if r < 0 or c < 0 or r >= n or c >= n or visited[r][c]:
        return
    # 인구 차이가 left이상 right이하일 경우
    if abs(population_list[r][c] - population) >= left and abs(population_list[r][c] - population) <= right:
        # 방문 표시
        visited[r][c] = True
        # 연합 리스트에 연합번호와 함께 넣음
        group.append((r, c, group_num))
        find_group(r - 1, c, population_list[r][c], group_num)
        find_group(r + 1, c, population_list[r][c], group_num)
        find_group(r, c - 1, population_list[r][c], group_num)
        find_group(r, c + 1, population_list[r][c], group_num)
    else:
        return
    
# 연합의 인원을 분배하는 함수
def grouping():
    start_index = 0
    end_index = 0
    for i in range(group_num):
        population_sum = 0 # 연합의 인구수
        count = 0
        while True:
            if end_index >= n * n:
                break
            x, y, g_num = group[end_index]
            if g_num != i:
                break
            population_sum += population_list[x][y]
            count += 1
            end_index += 1
        population_avg = int(population_sum / count) # 연합의 인구수의 평균
        for j in range(start_index, end_index):
            x, y, g = group[j]
            population_list[x][y] = population_avg # 인원을 분배
        start_index = end_index

# n, left, right를 공백으로 구분하여 입력받음
n, left, right = map(int, input().split())

# 인구수를 입력받아 리스트에 넣음
population_list = []
for _ in range(n):
    population_list.append(list(map(int, input().split())))

# 인구 이동 횟수를 나타내는 변수
movement_count = 0

while True:
    visited = [[False] * n for _ in range(n)]
    # 연합을 표시하는 리스트
    group = []
    # 연합번호를 나타내는 변수
    group_num = 0 
    for r in range(n):
        for c in range(n):
            # 아직 방문하지 않은 칸이라면
            if not visited[r][c]:
                # 방문 표시
                visited[r][c] = True
                # 연합 리스트에 연합번호와 함께 넣음
                group.append((r, c, group_num))
                # 연합을 찾는 dfs 알고리즘 수행
                find_group(r - 1, c, population_list[r][c], group_num)
                find_group(r + 1, c, population_list[r][c], group_num)
                find_group(r, c - 1, population_list[r][c], group_num)
                find_group(r, c + 1, population_list[r][c], group_num)
                group_num += 1

    # 연합이 안 생길 경우 종료
    if group_num == n * n:
        break
    # 연합이 생긴 경우
    else:
        # 인원 분배
        grouping()
        # 인구 이동 횟수 1 증가
        movement_count += 1

print(movement_count) # 결과 출력

# 해설
"""
from collections import deque

# 땅의 크기(N), L, R 값을 입력받기
n, l, r = map(int, input().split())

# 전체 나라의 정보(N x N)를 입력 받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    # (x, y)의 위치와 연결된 나라(연합) 정보를 담는 리스트
    united = []
    united.append((x, y))
    # 너비 우선 탐색 (BFS)을 위한 큐 라이브러리 사용
    q = deque()
    q.append((x, y))
    union[x][y] = index # 현재 연합의 번호 할당
    summary = graph[x][y] # 현재 연합의 전체 인구 수
    count = 1 # 현재 연합의 국가 수
    # 큐가 빌 때까지 반복(BFS)
    while q:
        x, y = q.popleft()
        # 현재 위치에서 4가지 방향을 확인하며
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                # 옆에 있는 나라와 인구 차이가 L명 이상, R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx, ny))
                    # 연합에 추가하기
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx, ny))
    # 연합 국가끼리 인구를 분배
    for i, j in united:
        graph[i][j] = summary // count

total_count = 0

# 더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: # 해당 나라가 아직 처리되지 않았다면
                process(i, j, index)
                index += 1
    # 모든 인구 이동이 끝난 경우
    if index == n * n:
        break
    total_count += 1

# 인구 이동 횟수 출력
print(total_count)
"""
