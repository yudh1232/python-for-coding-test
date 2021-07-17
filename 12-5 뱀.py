from collections import deque

# 보드의 크기 n을 입력받음
n = int(input())

# 보드판 생성
board = [[0] * n for _ in range(n)]

# 뱀의 위치를 나타내는 보드판 생성
snake = [[0] * n for _ in range(n)]
snake[0][0] = 1
# 뱀의 꼬리를 파악하기 위해 뱀의 이동경로를 queue로 표현
snake_history = deque()
snake_history.append((0, 0))

# 사과의 개수 k를 입력받음
k = int(input())

# 보드판에 사과 배치
for _ in range(k):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1

# 우, 상, 좌, 하
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 초기 방향: 우
direction = 0

# 뱀의 초기 위치
x = 0
y = 0

# 게임진행시간 값 초기화
count = 0

# 게임 종료를 나타내는 플래그
flag = 0

# 뱀의 방향 변환 횟수를 입력받음
l = int(input())

for _ in range(l):
    # 정수 a와 문자 c를 공백으로 구분하여 입력받음
    a, c = input().split()
    a = int(a) - count

    for _ in range(a):
        count += 1

        x += dx[direction]
        y += dy[direction]

        # 뱀이 벽을 만나거나 꼬리를 만난 경우
        if x < 0 or y < 0 or x >= n or y >= n or snake[x][y] == 1:
            # 게임 종료 플래그
            flag = 1
            break

        # 뱀이 사과를 만난 경우, 사과를 먹고 길이 1증가
        if board[x][y] == 1:
            board[x][y] = 0
            snake[x][y] = 1
            snake_history.append((x, y))

        # 뱀이 사과를 안 만난 경우, 이동하고 꼬리를 지움
        elif board[x][y] == 0:
            snake[x][y] = 1
            snake_history.append((x, y))
            tail = snake_history.popleft()
            snake[tail[0]][tail[1]] = 0
    
    # 게임 종료 플래그가 1일 경우 게임 종료
    if flag == 1:
        break
    
    # 방향 회전
    if c == 'L':
        direction = (direction + 1) % 4
    elif c == 'D':
        direction = (direction - 1) % 4

# 게임 종료 플래그가 0인 상태에서 방향을 모두 바꿨을 경우, 그 방향으로 나머지를 진행
if flag == 0:
    while True:
        count += 1

        x += dx[direction]
        y += dy[direction]

        if x < 0 or y < 0 or x >= n or y >= n or snake[x][y] == 1:
            flag = 1
            break

        if board[x][y] == 1:
            board[x][y] = 0
            snake[x][y] = 1
            snake_history.append((x, y))

        elif board[x][y] == 0:
            snake[x][y] = 1
            snake_history.append((x, y))
            tail = snake_history.popleft()
            snake[tail[0]][tail[1]] = 0

print(count) # 결과 출력

# 해설
"""
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로(동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에는 동쪽을 보고 있음
    time = 0 # 시작한 뒤에 지난 '초' 시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            # 사과가 없다면 이동 후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                data[px][py] = 0
            # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny # 다음 위치로 머리를 이동
        time += 1
        if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())
"""
