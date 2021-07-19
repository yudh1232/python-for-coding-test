n = 5
build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
build_frame2 = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

def solution(n, build_frame):
    board = [[2] * (n + 1) for _ in range(n + 1)]
    
    for process in build_frame:
        x, y = process[0], process[1]
        # 삭제작업
        if process[3] == 0:
            # 기둥
            if process[2] == 0:
                # 기둥을 삭제할 수 없을 때
                if board[y + 1][x] == 0 or (board[y + 1][x] == 1 and board[y][x + 1] != 0) or (board[y + 1][x - 1] == 1 and board[y][x - 1] != 0):
                    continue # 작업무시
                # 기둥을 삭제할 수 있을 때
                else: 
                    board[y][x] = 2 # 기둥 삭제
            # 보
            else:
                # 보를 삭제할 수 없을 때
                if (board[y][x - 1] == 1 and board[y - 1][x] != 0 and board[y - 1][x - 1] != 0) or (board[y][x + 1] == 1 and board[y - 1][x + 1] != 0 and board[y - 1][x + 2] != 0):
                    continue # 작업무시
                # 보를 삭제할 수 있을 때
                else: 
                    board[y][x] = 2 # 보 삭제
        # 설치작업
        else:
            # 기둥
            if process[2] == 0:
                # 기둥을 설치할 수 있을 때
                if y == 0 or (board[y][x - 1] == 1 and board[y][x] != 1) or (board[y][x] == 1 and board[y][x - 1] != 1) or board[y - 1][x] == 0:
                    board[y][x] = 0 # 기둥 설치
                # 기둥을 설치할 수 없을 때
                else:
                    continue # 작업무시
            # 보
            else:
                # 보를 설치할 수 있을 때
                if board[y - 1][x] == 0 or board[y - 1][x + 1] == 0 or (board[y][x - 1] == 1 and board[y][x + 1] == 1):
                    board[y][x] = 1 # 보 설치
                # 보를 설치할 수 없을 때
                else:
                    continue # 작업무시

solution(n, build_frame2)
