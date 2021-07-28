from collections import deque

board = [
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]
    ]

def solution(board):
    n = len(board)
    visited = [[0] * n for _ in range(n)]
    # (x, y, mode), mode: 로봇의 방향을 나타냄. 가로방향(1), 세로방향(2)
    q = deque()
    q.append((0, 0, 1))
    visited[0][0] = 1
    answer = 0
    while q:
        answer += 1
        x, y, mode = q.popleft()
        if mode == 1:
            if x - 1 >= 0 and y + 1 < n and board[x - 1][y] != 1 and board[x - 1][y + 1] != 1 and visited[x - 1][y] != 2 and visited[x - 1][y] != 3:
                if x - 1 == n - 2 and y == n - 1:
                    break
                q.append((x - 1, y, 2))
                visited[x - 1][y] += 2
            if x + 1 < n and y + 1 < n and board[x + 1][y] != 1 and board[x + 1][y + 1] != 1 and visited[x][y] != 2 and visited[x][y] != 3:
                if x == n - 2 and y == n - 1:
                    break
                q.append((x, y, 2))
                visited[x][y] += 2
            if x - 1 >= 0 and y + 1 < n and board[x - 1][y] != 1 and board[x - 1][y + 1] != 1 and visited[x - 1][y + 1] != 2 and visited[x - 1][y + 1] != 3:
                if x - 1 == n - 2 and y + 1 == n - 1:
                    break
                q.append((x - 1, y + 1, 2))
                visited[x][y] += 2
            if x + 1 < n and y + 1 < n and board[x + 1][y] != 1 and board[x + 1][y + 1] != 1 and visited[x][y + 1] != 2 and visited[x][y + 1] != 3:
                if x == n - 2 and y + 1 == n - 1:
                    break
                q.append((x, y + 1, 2))
                visited[x][y] += 2
            if x - 1 >= 0 and y + 1 < n and board[x - 1][y] != 1 and board[x - 1][y + 1] != 1 and visited[x - 1][y] != 1 and visited[x - 1][y] != 3:
                if x - 1 == n - 1 and y == n - 2:
                    break
                q.append((x - 1, y, 1))
                visited[x - 1][y] += 1
            if x + 1 < n and y + 1 < n and board[x + 1][y] != 1 and board[x + 1][y + 1] != 1 and visited[x + 1][y] != 1 and visited[x + 1][y] != 3:
                if x + 1 == n - 1 and y == n - 2:
                    break
                q.append((x + 1, y, 1))
                visited[x + 1][y] += 1
            if y - 1 >= 0 and board[x][y - 1] != 1 and visited[x][y - 1] != 1 and visited[x][y - 1] != 3:
                if x == n - 1 and y - 1 == n - 2:
                    break
                q.append((x, y - 1, 1))
                visited[x][y - 1] += 1
            if y + 2 < n and board[x][y + 2] != 1 and visited[x][y + 1] != 1 and visited[x][y + 1] != 3:
                if x == n - 1 and y + 1 == n - 2:
                    break
                q.append((x, y + 1, 1))
                visited[x][y + 1] += 1
        if mode == 2:
            if x + 1 < n and y - 1 >= 0 and board[x][y - 1] != 1 and board[x + 1][y - 1] != 1 and visited[x][y - 1] != 1 and visited[x][y - 1] != 3:
                if x == n - 1 and y - 1 == n - 2:
                    break
                q.append((x, y - 1, 1))
                visited[x][y - 1] += 1
            if x + 1 < n and y + 1 < n and board[x][y + 1] != 1 and board[x + 1][y + 1] != 1 and visited[x][y] != 1 and visited[x][y] != 3:
                if x == n - 1 and y == n - 2:
                    break
                q.append((x, y, 1))
                visited[x][y] += 1
            if x + 1 < n and y - 1 >= 0 and board[x][y - 1] != 1 and board[x + 1][y - 1] != 1 and visited[x + 1][y - 1] != 1 and visited[x + 1][y - 1] != 3:
                if x == n - 1 and y - 1 == n - 2:
                    break
                q.append((x + 1, y - 1, 1))
                visited[x + 1][y - 1] += 1
            if x + 1 < n and y + 1 < n and board[x][y + 1] != 1 and board[x + 1][y + 1] != 1 and visited[x + 1][y] != 1 and visited[x + 1][y] != 3:
                if x + 1 == n - 1 and y == n - 2:
                    break
                q.append((x + 1, y, 1))
                visited[x + 1][y] += 1
            if x + 1 < n and y - 1 >= 0 and board[x][y - 1] != 1 and board[x + 1][y - 1] != 1 and visited[x][y - 1] != 2 and visited[x][y - 1] != 3:
                if x == n - 2 and y - 1 == n - 1:
                    break
                q.append((x, y - 1, 2))
                visited[x][y - 1] += 2
            if x + 1 < n and y + 1 < n and board[x][y + 1] != 1 and board[x + 1][y + 1] != 1 and visited[x][y + 1] != 2 and visited[x][y + 1] != 3:
                if x == n - 2 and y + 1 == n - 1:
                    break
                q.append((x, y + 1, 2))
                visited[x][y + 1] += 2
            if x - 1 >= 0 and board[x - 1][y] != 1 and visited[x - 1][y] != 2 and visited[x - 1][y] != 3:
                if x - 1 == n - 2 and y == n - 1:
                    break
                q.append((x - 1, y, 2))
                visited[x - 1][y] += 2
            if x + 2 < n and board[x + 2][y] != 1 and visited[x + 1][y] != 2 and visited[x + 1][y] != 3:
                if x + 1 == n - 2 and y == n - 1:
                    break
                q.append((x + 1, y, 2))
                visited[x + 1][y] += 2
        
    return answer

print(solution(board))
