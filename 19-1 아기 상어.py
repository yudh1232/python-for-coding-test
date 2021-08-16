from collections import deque
import sys
input = sys.stdin.readline

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# n을 입력받음
n = int(input())

# 공간 정보를 입력받음
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 물고기 크기에따른 좌표를 담는 리스트
fish = [[] for _ in range(7)]

# data를 순회하며 물고기의 좌표와 상어의 좌표를 저장
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            fish[1].append((i, j))
        elif data[i][j] == 2:
            fish[2].append((i, j))
        elif data[i][j] == 3:
            fish[3].append((i, j))
        elif data[i][j] == 4:
            fish[4].append((i, j))
        elif data[i][j] == 5:
            fish[5].append((i, j))
        elif data[i][j] == 6:
            fish[6].append((i, j))
        elif data[i][j] == 9:
            # 상어가 있는칸은 0으로 초기화해줌
            data[i][j] = 0
            # (x, y): 상어의 좌표
            x = i
            y = j

t = 0 # 시간
size = 2 # 상어의 사이즈
eat_count = 0 # 먹은 물고기 수
visited = [[False] * n for _ in range(n)] # bfs를 위한 visited
q = deque() # bfs를 위한 큐

# 먹을 수 있는게 없을때까지
while True:
    # 먹을 수 있는 물고기가 있는지 체크
    eatable_fish_count = 0
    for i in range(1, size):
        if i >= 7:
            break
        eatable_fish_count += len(fish[i])
    if eatable_fish_count == 0:
        break

    # 물고기 먹기, bfs로 가까운 물고기 위치를 찾아 먹음
    eat_success = False
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
    q.clear()
    q.append((x, y)) # 큐에 현재 상어의 좌표를 넣어줌
    visited[x][y] = True
    level = 0 # bfs 깊이, 이동한 칸 수
    while q:
        q_size = len(q)
        eat_a = n
        eat_b = n
        while q_size > 0:
            a, b = q.popleft()
            q_size -= 1
            # 먹을 수 있는 물고기일 경우, 좌표를 기억해둠
            if data[a][b] != 0 and data[a][b] < size:
                if a < eat_a or (a == eat_a and b < eat_b):
                    eat_a = a
                    eat_b = b
            # 빈 곳이거나 크기가 같은 물고기일 경우
            else:
                for i in range(4):
                    nx = a + dx[i]
                    ny = b + dy[i]
                    if (nx >= 0 and nx < n and ny >= 0 and ny < n and data[nx][ny] <= size and visited[nx][ny] == False):
                        q.append((nx, ny))
                        visited[nx][ny] = True
        
        # 먹을 수 있는 물고기를 발견한 경우 물고기를 먹음
        if eat_a != n:
            fish[data[eat_a][eat_b]].remove((eat_a, eat_b))
            data[eat_a][eat_b] = 0
            eat_count += 1
            t += level
            x = eat_a
            y = eat_b
            eat_success = True
            break
        
        level += 1

    # 길이 없어 믈고기를 못먹었으면 종료
    if eat_success == False:
        break

    # 먹은 물고기 수가 크기와 같다면, 크기 증가
    if eat_count == size:
        size += 1
        eat_count = 0

print(t) # 결과 출력

# 해설
"""
from collections import deque
INF = 1e9 # 무한을 의미하는 값으로 10억을 설정

# 맵의 크기 N 입력
n = int(input())

# 전체 모든 칸에 대한 정보 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 아기 상어의 현재 크기 변수와 현재 위치 변수
now_size = 2
now_x, now_y = 0, 0

# 아기 상어의 시작 위치를 찾은 뒤에 그 위치엔 아무것도 없다고 처리
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 모든 위치까지의 '최단 거리만' 계산하는 BFS 함수
def bfs():
    # 값이 -1이라면 도달할 수 없다는 의미 (초기화)
    dist = [[-1] * n for _ in range(n)]
    # 시작 위치는 도달이 가능하다고 보며 거리는 0
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                # 자신의 크기보다 작거나 같은 경우에 지나갈 수 있음
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
    # 모든 위치까지의 최단 거리 테이블 반환
    return dist

# 최단 거리 테이블이 주어졌을 때, 먹을 물고기를 찾는 함수
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기일 때
            if dist[i][j] != -1 and 1 <= array[i][j] and array[i][j] < now_size:
                # 가장 가까운 물고기 한 마리만 선택
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF: # 먹을 수 있는 물고기가 없는 경우
        return None
    else:
        return x, y, min_dist # 먹을 물고기의 위치와 최단 거리

result = 0 # 최종 답안
ate = 0 # 현재 크기에서 먹은 양

while True:
    # 먹을 수 있는 물고기의 위치 찾기
    value = find(bfs())
    # 먹을 수 있는 물고기가 없는 경우, 현재까지 움직인 거리 출력
    if value == None:
        print(result)
        break
    else:
        # 현재 위치 갱신 및 이동 거리 변경
        now_x, now_y = value[0], value[1]
        result += value[2]
        # 먹은 위치에는 이제 아무것도 없도록 처리
        array[now_x][now_y] = 0
        ate += 1
        # 자신의 현재 크기 이상으로 먹은 경우, 크기 증가
        if ate >= now_size:
            now_size += 1
            ate = 0
"""
