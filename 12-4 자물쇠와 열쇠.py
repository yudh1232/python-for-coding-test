# key를 시계방향으로 90도 회전하는 함수
def rotate_90(array):
    k = len(array)
    rotate_result = [[0] * k for _ in range(k)]
    for i in range(k):
        for j in range(k):
            rotate_result[j][k - 1 - i] = array[i][j]
    return rotate_result

# key를 a, b만큼 이동한 결과 lock에서 key가 어떻게 나타나는지 처리하는 함수
def move(array, m, n, a, b):
    # key를 a, b만큼 이동한 결과 lock에서 key의 결과를 담는 리스트
    temp = [[0] * n for _ in range(n)]
    for i in range(m):
        for j in range(m):
            # lock을 벗어나는 부분은 처리 안함
            if i + a < 0 or i + a >= n or j + b < 0 or j + b >= n:
                continue
            # 이동한 key를 lock에 표시
            temp[i + a][j + b] = array[i][j]
    return temp

def solution(key, lock):
    m = len(key)
    n = len(lock)
    for _ in range(4):
        # key를 시계방향으로 90도 회전
        key = rotate_90(key)
        for i in range(-m + 1, n):
            for j in range(-m + 1, n):
                # 키가 꽂힌 lock을 나타내는 리스트
                keyed_lock = [[0] * n for _ in range(n)]
                # key를 이동
                converted_key = move(key, m, n, i, j)
                for k in range(n):
                    for l in range(n):
                        # 이동한 key를 lock에 꽂음
                        keyed_lock[k][l] += lock[k][l] + converted_key[k][l]
                
                # key와 lock이 맞는지 나타내는 변수
                flag = 1
                for a in range(n):
                    for b in range(n):
                        # key와 lock이 맞지 않다면
                        if keyed_lock[a][b] != 1:
                            flag = 0

                # key와 lock이 맞다면
                if flag == 1:
                    return True
    
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))
