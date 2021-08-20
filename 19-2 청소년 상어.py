import sys
input = sys.stdin.readline
import copy

# 번호가 fish_num인 물고기의 위치를 반환
def find_pos(grid, fish_num):
    for i in range(4):
        for j in range(4):
            if grid[i][j][0] == fish_num:
                return i, j

# 물고기들의 이동
def fish_move(grid, fish, s_x, s_y):
    for f in fish:
        f_x, f_y = find_pos(grid, f)
        f_dir = grid[f_x][f_y][1]
        for _ in range(8):
            nf_x = f_x + dx[f_dir]
            nf_y = f_y + dy[f_dir]
            # 이동할 수 없는 경우, 방향회전
            if nf_x < 0 or nf_x >= 4 or nf_y < 0 or nf_y >= 4 or (s_x == nf_x and s_y == nf_y):
                f_dir = f_dir % 8 + 1
            # 이동할 수 있는 경우, 스왑
            else:
                grid[f_x][f_y][1] = f_dir
                grid[f_x][f_y], grid[nf_x][nf_y] = grid[nf_x][nf_y], grid[f_x][f_y]
                break

# 시물레이션
def shark_move(grid, fish, s_x, s_y, total):
    global result
    grid = copy.deepcopy(grid)
    fish = copy.deepcopy(fish)

    # 현재 위치의 물고기를 먹음
    total += grid[s_x][s_y][0]
    s_dir = grid[s_x][s_y][1]
    fish.remove(grid[s_x][s_y][0])
    grid[s_x][s_y][0], grid[s_x][s_y][1] = -1, -1

    # 물고기들의 이동
    fish_move(grid, fish, s_x, s_y)

    # 상어가 이동했는지 나타내는 변수
    move = False
    
    # 상어의 이동
    for _ in range(3):
        ns_x = s_x + dx[s_dir]
        ns_y = s_y + dy[s_dir]
        # 이동할 수 있는 경우
        if ns_x >= 0 and ns_x < 4 and ns_y >= 0 and ns_y < 4 and grid[ns_x][ns_y][0] != -1:
            move = True
            shark_move(grid, fish, ns_x, ns_y, total)
        s_x, s_y = ns_x, ns_y

    # 이동 못한 경우
    if move == False:
        result = max(result, total)

# dx[1] ~ dx[8], dy[1] ~ dy[8]: 8방향
dx = [9, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [9, 0, -1, -1, -1, 0, 1, 1, 1]

# 물고기의 정보를 담을 리스트
grid = [[] for _ in range(4)]

# 물고기의 정보를 입력받음
for i in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    grid[i].append([a1, b1])
    grid[i].append([a2, b2])
    grid[i].append([a3, b3])
    grid[i].append([a4, b4])

# 살아있는 물고기의 번호
fish = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 결과값
result = 0

# 시뮬레이션 실행
shark_move(grid, fish, 0, 0, 0)

# 결과 출력
print(result)

# 해설
"""
import copy
# 4 X 4 크기 격자에 존재하는 각 물고기의 번호(없으면 -1)와 방향 값을 담는 테이블
array = [[None] * 4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    # 매 줄마다 4마리의 물고기를 하나씩 확인하며
    for j in range(4):
        # 각 위치마다 [물고기의 번호, 방향]을 저장
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1]
# 8가지 방향에 대한 정의
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]
# 현재 위치에서 왼쪽으로 회전된 결과 반환
def turn_left(direction):
    return (direction + 1) % 8
result = 0 # 최종 결과
# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)
    return None
# 모든 물고기를 회전 및 이동시키는 함수
def move_all_fishes(array, now_x, now_y):
    # 1번부터 16번까지의 물고기를 차례대로 (낮은 번호부터) 확인
    for i in range(1, 17):
        # 해당 물고기의 위치를 찾기
        position = find_fish(array, i)
        if position != None:
            x, y = position[0], position[1]
            direction = array[x][y][1]
            # 해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                # 해당 방향으로 이동이 가능하다면 이동 시키기
                if 0 <= nx and nx < 4 and 0 <= ny and ny < 4:
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y]
                        break
                direction = turn_left(direction)
        
# 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    # 현재의 방향으로 쭉 이동하기
    for i in range(4):
        now_x += dx[direction]
        now_y += dy[direction]
        # 범위를 벗어나지 않는지 확인하며
        if 0 <= now_x and now_x < 4 and 0 <= now_y and now_y < 4:
            # 물고기가 존재하는 경우
            if array[now_x][now_y][0] != -1:
                positions.append((now_x, now_y))
    return positions
# 모든 경우를 탐색하기 위한 DFS 함수
def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array) # 리스트를 통째로 복사
    
    total += array[now_x][now_y][0] # 현재 위치의 물고기 먹기
    array[now_x][now_y][0] = -1 # 물고기를 먹었으므로 번호 값을 -1로 변환
    
    move_all_fishes(array, now_x, now_y) # 전체 물고기 이동 시키기
    # 이제 다시 상어가 이동할 차례이므로, 이동 가능한 위치 찾기
    positions = get_possible_positions(array, now_x, now_y)
    # 이동할 수 있는 위치가 하나도 없다면 종료
    if len(positions) == 0:
        result = max(result, total) # 최댓값 저장
        return 
    # 모든 이동할 수 있는 위치로 재귀적으로 수행
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)
# 청소년 상어의 시작 위치(0, 0)에서부터 재귀적으로 모든 경우 탐색
dfs(array, 0, 0, 0)
print(result)
"""
