# 정수 x를 입력받음
x = int(input())

# 최소값 테이블
data = [0] * 30001

# 초기값 설정
data[1], data[2], data[3], data[4], data[5] = 1, 1, 1, 2, 1

# data[i // 2], data[i // 3], data[i // 5], data[i - 1]중에 가장 작은값을 찾은 다음 1을 더해준 값을 data[i]로 함
for i in range(6, x + 1):
    if i % 2 == 0:
        if data[i // 2] < data[i - 1]:
            data[i] = data[i // 2] + 1
        else:
            data[i] = data[i - 1] + 1
    elif i % 3 == 0:
        if data[i // 3] < data[i - 1]:
            data[i] = data[i // 3] + 1
        else:
            data[i] = data[i - 1] + 1
    elif i % 5 == 0:
        if data[i // 5] < data[i - 1]:
            data[i] = data[i // 5] + 1
        else:
            data[i] = data[i - 1] + 1
    else:
        data[i] = data[i - 1] + 1

print(data[x]) # 결과 출력

# 해설
"""
# 정수 X를 입력 받기
x = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1000001

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
for i in range(2, x + 1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i - 1] + 1
    # 현재의 수가 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    # 현재의 수가 5로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])
"""
