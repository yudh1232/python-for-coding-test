n = int(input()) # n을 입력받음
data = list(input().split()) # 입력 계획서를 입력받아 리스트에 넣음

# (a, b)를 (1, 1)로 초기화
a, b = 1, 1

# data의 길이만큼 반복
for i in range(len(data)):
    if data[i] == 'L':
        if b == 1: # b가 1일 경우 이동하지 않음
            continue
        else: # b가 1이 아닐 경우 왼쪽으로 이동
            b -= 1

    if data[i] == 'R':
        if b == n: # b가 n일 경우 이동하지 않음
            continue
        else: # b가 n이 아닐 경우 오른쪽으로 이동
            b += 1

    if data[i] == 'U':
        if a == 1: # a가 1일 경우 이동하지 않음
            continue
        else: # a가 1이 아닐 경우 위쪽으로 이동
            a -= 1

    if data[i] == 'D':
        if a == n: # a가 n일 경우 이동하지 않음
            continue
        else: # a가 n이 아닐 경우 아래쪽으로 이동
            a += 1

print(a, b) # 결과 출력

# 해설
"""
# N을 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
"""
