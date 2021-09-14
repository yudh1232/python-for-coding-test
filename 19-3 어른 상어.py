import sys
input = sys.stdin.readline

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

def scent():
    for i in range(n):
        for j in range(n):
            if grid[i][j] != 0:
                smell[i][j][0] = grid[i][j]
                smell[i][j][1] = k

n, m, k = map(int, input().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

smell = [[[0] * 2 for _ in range(n)] for _ in range(n)]

direction = list(map(int, input().split()))
direction.insert(0, 0) # 인덱스 맞춰주기 위해 앞에 0 넣어줌

# 인덱스 맞춰주기 위해 빈 리스트 넣어줌
priority = [[] for _ in range(m + 1)]
for i in range(1, m + 1):
    priority[i].append([])
    for _ in range(4):
        priority[i].append(list(map(int, input().split())))

# 냄새 뿌림
scent()

t = 0
while True:
    if t == 1000:
        print(-1)
        break
