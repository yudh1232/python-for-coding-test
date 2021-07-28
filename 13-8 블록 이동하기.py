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
    # 방문여부를 나타냄, 1: 가로방향으로 방문, 2: 세로방향으로 방문, 3: 가로방향, 세로방향으로 방문, 0: 한번도 방문하지 않음
    visited = [[0] * n for _ in range(n)]
    q = deque()
    # (x, y, mode, level)
    # mode: 로봇의 방향을 나타냄. 가로방향(1), 세로방향(2)
    # level: 경과한 시간초를 나타냄.
    q.append((0, 0, 1, 0)) # 큐에 초기위치 삽입
    visited[0][0] = 1 # 방문표시(가로방향)
    while q:
        x, y, mode, level = q.popleft()
        level += 1
        # 가로방향이라면
        if mode == 1:
            # 회전가능 하다면
            if x - 1 >= 0 and y + 1 < n and board[x - 1][y] != 1 and board[x - 1][y + 1] != 1 and visited[x - 1][y] != 2 and visited[x - 1][y] != 3:
                # (n, n)에 도달했다면 종료
                if x - 1 == n - 2 and y == n - 1:
                    answer = level
                    break
                q.append((x - 1, y, 2, level))
                visited[x - 1][y] += 2
            # 회전가능 하다면
            if x + 1 < n and y + 1 < n and board[x + 1][y] != 1 and board[x + 1][y + 1] != 1 and visited[x][y] != 2 and visited[x][y] != 3:
                # (n, n)에 도달했다면 종료
                if x == n - 2 and y == n - 1:
                    answer = level
                    break
                q.append((x, y, 2, level))
                visited[x][y] += 2
            # 회전가능 하다면
            if x - 1 >= 0 and y + 1 < n and board[x - 1][y] != 1 and board[x - 1][y + 1] != 1 and visited[x - 1][y + 1] != 2 and visited[x - 1][y + 1] != 3:
                # (n, n)에 도달했다면 종료
                if x - 1 == n - 2 and y + 1 == n - 1:
                    answer = level
                    break
                q.append((x - 1, y + 1, 2, level))
                visited[x][y] += 2
            # 회전가능 하다면
            if x + 1 < n and y + 1 < n and board[x + 1][y] != 1 and board[x + 1][y + 1] != 1 and visited[x][y + 1] != 2 and visited[x][y + 1] != 3:
                # (n, n)에 도달했다면 종료
                if x == n - 2 and y + 1 == n - 1:
                    answer = level
                    break
                q.append((x, y + 1, 2, level))
                visited[x][y] += 2
            # 이동가능 하다면
            if x - 1 >= 0 and y + 1 < n and board[x - 1][y] != 1 and board[x - 1][y + 1] != 1 and visited[x - 1][y] != 1 and visited[x - 1][y] != 3:
                # (n, n)에 도달했다면 종료
                if x - 1 == n - 1 and y == n - 2:
                    answer = level
                    break
                q.append((x - 1, y, 1, level))
                visited[x - 1][y] += 1
            # 이동가능 하다면
            if x + 1 < n and y + 1 < n and board[x + 1][y] != 1 and board[x + 1][y + 1] != 1 and visited[x + 1][y] != 1 and visited[x + 1][y] != 3:
                # (n, n)에 도달했다면 종료
                if x + 1 == n - 1 and y == n - 2:
                    answer = level
                    break
                q.append((x + 1, y, 1, level))
                visited[x + 1][y] += 1
            # 이동가능 하다면
            if y - 1 >= 0 and board[x][y - 1] != 1 and visited[x][y - 1] != 1 and visited[x][y - 1] != 3:
                # (n, n)에 도달했다면 종료
                if x == n - 1 and y - 1 == n - 2:
                    answer = level
                    break
                q.append((x, y - 1, 1, level))
                visited[x][y - 1] += 1
            # 이동가능 하다면
            if y + 2 < n and board[x][y + 2] != 1 and visited[x][y + 1] != 1 and visited[x][y + 1] != 3:
                # (n, n)에 도달했다면 종료
                if x == n - 1 and y + 1 == n - 2:
                    answer = level
                    break
                q.append((x, y + 1, 1, level))
                visited[x][y + 1] += 1
        if mode == 2:
            # 회전가능 하다면
            if x + 1 < n and y - 1 >= 0 and board[x][y - 1] != 1 and board[x + 1][y - 1] != 1 and visited[x][y - 1] != 1 and visited[x][y - 1] != 3:
                # (n, n)에 도달했다면 종료
                if x == n - 1 and y - 1 == n - 2:
                    answer = level
                    break
                q.append((x, y - 1, 1, level))
                visited[x][y - 1] += 1
            # 회전가능 하다면
            if x + 1 < n and y + 1 < n and board[x][y + 1] != 1 and board[x + 1][y + 1] != 1 and visited[x][y] != 1 and visited[x][y] != 3:
                # (n, n)에 도달했다면 종료
                if x == n - 1 and y == n - 2:
                    answer = level
                    break
                q.append((x, y, 1, level))
                visited[x][y] += 1
            # 회전가능 하다면
            if x + 1 < n and y - 1 >= 0 and board[x][y - 1] != 1 and board[x + 1][y - 1] != 1 and visited[x + 1][y - 1] != 1 and visited[x + 1][y - 1] != 3:
                # (n, n)에 도달했다면 종료
                if x == n - 1 and y - 1 == n - 2:
                    answer = level
                    break
                q.append((x + 1, y - 1, 1, level))
                visited[x + 1][y - 1] += 1
            # 회전가능 하다면
            if x + 1 < n and y + 1 < n and board[x][y + 1] != 1 and board[x + 1][y + 1] != 1 and visited[x + 1][y] != 1 and visited[x + 1][y] != 3:
                # (n, n)에 도달했다면 종료
                if x + 1 == n - 1 and y == n - 2:
                    answer = level
                    break
                q.append((x + 1, y, 1, level))
                visited[x + 1][y] += 1
            # 이동가능 하다면
            if x + 1 < n and y - 1 >= 0 and board[x][y - 1] != 1 and board[x + 1][y - 1] != 1 and visited[x][y - 1] != 2 and visited[x][y - 1] != 3:
                # (n, n)에 도달했다면 종료
                if x == n - 2 and y - 1 == n - 1:
                    answer = level
                    break
                q.append((x, y - 1, 2, level))
                visited[x][y - 1] += 2
            # 이동가능 하다면
            if x + 1 < n and y + 1 < n and board[x][y + 1] != 1 and board[x + 1][y + 1] != 1 and visited[x][y + 1] != 2 and visited[x][y + 1] != 3:
                # (n, n)에 도달했다면 종료
                if x == n - 2 and y + 1 == n - 1:
                    answer = level
                    break
                q.append((x, y + 1, 2, level))
                visited[x][y + 1] += 2
            # 이동가능 하다면
            if x - 1 >= 0 and board[x - 1][y] != 1 and visited[x - 1][y] != 2 and visited[x - 1][y] != 3:
                # (n, n)에 도달했다면 종료
                if x - 1 == n - 2 and y == n - 1:
                    answer = level
                    break
                q.append((x - 1, y, 2, level))
                visited[x - 1][y] += 2
            # 이동가능 하다면
            if x + 2 < n and board[x + 2][y] != 1 and visited[x + 1][y] != 2 and visited[x + 1][y] != 3:
                # (n, n)에 도달했다면 종료
                if x + 1 == n - 2 and y == n - 1:
                    answer = level
                    break
                q.append((x + 1, y, 2, level))
                visited[x + 1][y] += 2
    
    return answer

print(solution(board)) # 결과 출력

# 해설
"""
from collections import deque

def get_next_pos(pos, board):
    next_pos = [] # 반환 결과 (이동 가능한 위치들)
    pos = list(pos) # 현재 위치 정보를 리스트로 변환 (집합 → 리스트)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    # (상, 하, 좌, 우)로 이동하는 경우에 대해서 처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append({(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)})
    # 현재 로봇이 가로로 놓여 있는 경우
    if pos1_x == pos2_x:
        for i in [-1, 1]: # 위쪽으로 회전하거나, 아래쪽으로 회전
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0: # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    # 현재 로봇이 세로로 놓여 있는 경우
    elif pos1_y == pos2_y:
        for i in [-1, 1]: # 왼쪽으로 회전하거나, 오른쪽으로 회전
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0: # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})
    # 현재 위치에서 이동할 수 있는 위치를 반환
    return next_pos

def solution(board):
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    # 너비 우선 탐색(BFS) 수행
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)} # 시작 위치 설정
    q.append((pos, 0)) # 큐에 삽입한 뒤에
    visited.append(pos) # 방문 처리
    # 큐가 빌 때까지 반복
    while q:
        pos, cost = q.popleft()
        # (n, n) 위치에 로봇이 도달했다면, 최단 거리이므로 반환
        if (n, n) in pos:
            return cost
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0
"""
