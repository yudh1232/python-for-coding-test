import copy

def find_pos(fish_num):
    for i in range(4):
        for j in range(4):
            if grid[i][j][0] == fish_num:
                return i, j

def fish_move():
    for f in fish:
        f_x, f_y = find_pos(f)
        f_dir = grid[f_x][f_y][1]
        for _ in range(8):
            nf_x = f_x + dx[f_dir]
            nf_y = f_y + dy[f_dir]
            if nf_x < 0 or nf_x >= 4 or nf_y < 0 or nf_y >= 4 or grid[nf_x][nf_y][0] == 0:
                f_dir = f_dir % 8 + 1
                continue
            else:
                grid[f_x][f_y], grid[nf_x][nf_y] = grid[nf_x][nf_y], grid[f_x][f_y]
                break

def shark_move():
    global s_x, s_y, s_dir, finish
    temp = copy.deepcopy(grid)


# dx[1] ~ dx[8], dy[1] ~ dy[8]: 8방향
dx = [9, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [9, 0, -1, -1, -1, 0, 1, 1, 1]

grid = [[] for _ in range(4)]

for i in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    grid[i].append((a1, b1))
    grid[i].append((a2, b2))
    grid[i].append((a3, b3))
    grid[i].append((a4, b4))

fish = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# 초기값 설정
s_x = 0
s_y = 0
s_dir = grid[0][0][1]
result = grid[0][0][0]
fish.remove(grid[0][0][0])
grid[0][0] = (0, s_dir)
finish = False

while True:
    fish_move()
    shark_move()
    if finish == True:
        break

print(result)
