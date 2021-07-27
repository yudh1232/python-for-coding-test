board = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]
    ]

# 가로: 0, 세로: 1
# 초기: (0, 0, 0)
# (x, y, 0)일 때 이동가능 경우 8가지
# (x, y, 1)일 때 이동가능 경우 8가지
# (n - 1, n - 2, 0) or (n - 2, n - 1, 1)이면 도착
# visited를 이용하여 dfs로 구현

def solution(board):
    n = len(board)
    visited = [[False] * n for _ in range(n)]

solution(board)
