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
