n, m = map(int, input().split()) # n, m을 공백으로 구분하여 입력받음
a, b, d = map(int, input().split()) # a, b, d를 공백으로 구분하여 입력받음

# 맵을 입력받아 리스트에 넣음
map_data = []
for i in range(n):
    map_data.append(list(map(int, input().split())))

count = 1 # 결과 값
flag = 0 # 새로운 칸으로 이동했는지 체크하는 변수
quit = 0 # 반복문 탈출 변수

map_data[a][b] = 2 # 초기 위치 값 초기화, 2: 방문한 칸

while True:
    if quit == 1:
        break
    flag = 0

    for _ in range(4):
        # 반시계 방향으로 90도 회전
        d = (d - 1) % 4

        # 육지가 있다면 이동, 방문 표시를 함, flag를 1로 바꿈
        if d == 0:
            if map_data[a - 1][b] == 0:
                map_data[a - 1][b] = 2
                a = a - 1
                count += 1
                flag = 1
                break
        elif d == 1:
            if map_data[a][b + 1] == 0:
                map_data[a][b + 1] = 2
                b = b + 1
                count += 1
                flag = 1
                break
        elif d == 2:
            if map_data[a + 1][b] == 0:
                map_data[a + 1][b] = 2
                a = a + 1
                count += 1
                flag = 1
                break
        elif d == 3:
            if map_data[a][b - 1] == 0:
                map_data[a][b - 1] = 2
                b = b - 1
                count += 1
                flag = 1
                break

    # 방문하지 못했다면 뒤로 감. 단, 뒤가 육지이면 종료
    if flag == 0:
        if d == 0:
            if map_data[a + 1][b] != 1:
                a = a + 1
            else:
                quit = 1
        if d == 1:
            if map_data[a][b - 1] != 1:
                b = b - 1
            else:
                quit = 1
        if d == 2:
            if map_data[a - 1][b] != 1:
                a = a - 1
            else:
                quit = 1
        if d == 3:
            if map_data[a][b + 1] != 1:
                b = b + 1
            else:
                quit = 1

print(count) # 결과 출력

# 해설
"""
# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)
"""
