from collections import deque

# n, k를 공백으로 구분하여 입력받음
n, k = map(int, input().split())

# 시험관 정보를 담을 리스트
data = []
# 시험관 정보를 담아 2차원 리스트에 담음
for _ in range(n):
    data.append(list(map(int, input().split())))

# s, x, y를 공백으로 구분하여 입력받음
s, x, y = map(int, input().split())

# 바이러스를 (종류, x좌표, y좌표, bfs레벨)의 형태로 리스트에 넣음
virus = []
for i in range(n):
    for j in range(n):
        if data[i][j] != 0:
            virus.append((data[i][j], i, j, 0))

# 바이러스 번호에 따라 오름차순으로 정렬
virus.sort()

# bfs레벨 0의 바이러스들을 큐에 넣음
q = deque()
for v in virus:
    q.append(v)

# 몇 초째 진행중인지 나타내는 변수
count = 0

# count가 s보다 작을때까지
while count < s:
    # 큐가 비었으면 바로 종료
    if not q:
        break
    # 큐에서 바이러스를 하나 꺼냄
    v_type, a, b, level = q.popleft()
    # 큐에서 꺼낸 바이러스가 진행중인 bfs레벨과 다를 경우 다시넣고, bfs레벨을 증가 
    if level != count:
        q.appendleft((v_type, a, b, level))
        count += 1
    # 큐에서 꺼낸 바이러스가 진행중인 bfs레벨과 같을 경우
    else:
        # 상하좌우로 증식시도, 증식에 성공하면 그 좌표를 bfs레벨을 1 증가시켜 큐에 넣음
        if a - 1 >= 0:
            if data[a - 1][b] == 0:
                data[a - 1][b] = v_type
                q.append((v_type, a - 1, b, level + 1))
        if a + 1 < n:
            if data[a + 1][b] == 0:
                data[a + 1][b] = v_type
                q.append((v_type, a + 1, b, level + 1))
        if b - 1 >= 0:
            if data[a][b - 1] == 0:
                data[a][b - 1] = v_type
                q.append((v_type, a, b - 1, level + 1))
        if b + 1 < n:        
            if data[a][b + 1] == 0:
                data[a][b + 1] = v_type
                q.append((v_type, a, b + 1, level + 1))

print(data[x - 1][y - 1]) # 결과 출력
