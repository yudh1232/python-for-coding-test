import sys
input = sys.stdin.readline

# 상, 하, 좌, 우, 인덱스 맞춰주기 위해 앞에 0 넣어줌
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

# 냄새 뿌리기
# 격자를 순서대로 탐색하다가 상어가 있는 자리를 만나면 냄새를 뿌림
def scent():
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                smell[i][j][0] = grid[i][j]
                smell[i][j][1] = k

# 상어 이동
def move():
    # 1번 상어부터 m번 상어까지
    for s in range(1, m + 1):
        # 쫓겨난 상어면 통과
        if valid_shark[s] == 0:
            continue
        

        x, y = shark[s][1], shark[s][2]
        move_flag = 0 # 냄새가 없는 칸으로 이동 성공했는지 나타내는 변수
        # 보고있는 방향에 따른 우선순위에 따라
        for d in priority[s][shark[s][3]]:
            nx = x + dx[d]
            ny = y + dy[d]
            # 격자를 벗어나면 통과
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            # 냄새가 없는 칸이면
            if smell[nx][ny][0] == 0:
                # 상어가 없는 칸이면
                if grid[nx][ny] == 0:
                    # 그 곳으로 이동
                    grid[nx][ny] = s
                # 상어가 있는 칸이면
                else:
                    # 쫓겨남
                    valid_shark[s] = 0
                
                # 상어의 좌표, 방향 업데이트
                grid[x][y] = 0
                shark[s][1], shark[s][2] = nx, ny
                shark[s][3] = d
                
                # 냄새가 없는 칸으로 이동 성공
                move_flag = 1
                break
        
        # 냄새가 없는 칸으로 이동하지 못했다면
        if move_flag == 0:
            # 보고있는 방향에 따른 우선순위에 따라
            for d in priority[s][shark[s][3]]:
                nx = x + dx[d]
                ny = y + dy[d]
                # 격자를 벗어나면 통과
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                # 자신의 냄새가 있는 칸이면
                if smell[nx][ny][0] == s:
                    # 그 곳으로 이동
                    grid[nx][ny] = s
                    
                    # 상어의 좌표, 방향 업데이트
                    grid[x][y] = 0
                    shark[s][1], shark[s][2] = nx, ny
                    shark[s][3] = d
                    break

# 1번 상어만 남았는지 체크
def is_finish():
    if sum(valid_shark) == 1:
        return True
    return False

# 기존 냄새들 -= 1
def decrease_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] >= 2:
                smell[i][j][1] -= 1
            elif smell[i][j][1] == 1:
                smell[i][j][0] = 0
                smell[i][j][1] = 0

# n, m, k를 입력받음
n, m, k = map(int, input().split())

# 격자의 상태를 입력받음
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 상어가 남아있으면 1, 쫓겨났으면 0, 인덱스 맞춰주기 위해 앞에 0 넣어줌
valid_shark = [1] * (m + 1)
valid_shark[0] = 0

# i행 j열에 [상어번호, 남은냄새시간]을 나타냄
smell = [[[0] * 2 for _ in range(n)] for _ in range(n)]

# 상어들의 초기 방향 상태를 입력받음
direction = list(map(int, input().split()))
direction.insert(0, 0) # 인덱스 맞춰주기 위해 앞에 0 넣어줌

# [상어번호, 상어의 행, 상어의 열, 방향]을 저장하는 리스트 
shark = []
for i in range(n):
    for j in range(n):
        if grid[i][j] != 0:
            shark.append([grid[i][j], i, j, direction[grid[i][j]]])
# 인덱스 맞춰주기 위해 앞에 빈 리스트 넣어줌, 상어번호 순대로 정렬
shark.insert(0, [])
shark.sort()

# 인덱스 맞춰주기 위해 빈 리스트 넣어줌
priority = [[] for _ in range(m + 1)]
for i in range(1, m + 1):
    priority[i].append([])
    for _ in range(4):
        priority[i].append(list(map(int, input().split())))

# 맨 처음 상어가 냄새를 뿌림
scent()

# 시간
t = 0

while True:
    t += 1

    # 상어 이동
    move()

    # 1번 상어만 격자에 남으면
    if is_finish():
        # 시간 출력, 반복 종료
        print(t)
        break
    
    # 기존 냄새들 -= 1
    decrease_smell()

    # 냄새 뿌리기
    scent()

    # 1000초가 넘어도 다른 상어가 격자에 남아있으면
    if t == 1000:
        # -1 출력, 반복 종료
        print(-1)
        break
