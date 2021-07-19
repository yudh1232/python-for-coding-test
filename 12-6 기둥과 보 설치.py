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

# 해설
"""
# 현재 설치된 구조물이 '가능한' 구조물인지 확인하는 함수
def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0: # 설치된 것이 '기둥'인 경우
            # '바닥 위' 혹은 '보의 한쪽 끝 부분 위' 혹은 '다른 기둥 위'라면 정상
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False # 아니라면 거짓(False) 반환
        elif stuff == 1: # 설치된 것이 '보'인 경우
            # '한쪽 끝부분이 기둥 위' 혹은 '양쪽 끝부분이 다른 보와 동시에 연결'이라면 정상
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False # 아니라면 거짓(False) 반환
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame: # 작업(frame)의 개수는 최대 1,000개
        x, y, stuff, operate = frame
        if operate == 0: # 삭제하는 경우
            answer.remove([x, y, stuff]) # 일단 삭제를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.append([x, y, stuff]) # 가능한 구조물이 아니라면 다시 설치
        if operate == 1: # 설치하는 경우
            answer.append([x, y, stuff]) # 일단 설치를 해본 뒤에
            if not possible(answer): # 가능한 구조물인지 확인
                answer.remove([x, y, stuff]) # 가능한 구조물이 아니라면 다시 제거
    return sorted(answer) # 정렬된 결과를 반환
"""
