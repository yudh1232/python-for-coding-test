# 정수 삼각형의 크기 n을 입력받음
n = int(input())

# 삼각형 수를 입력받아 2차원리스트 생성
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 다이나믹 프로그래밍
for i in range(n):
    for j in range(i + 1):
        # 삼각형의 오른쪽 위 숫자가 없는경우
        if i - 1 < 0 or i - 1 < j:
            up = 0
        # 삼각형의 오른쪽 위 숫자가 있는경우
        else:
            up = data[i - 1][j]
        # 삼각형의 왼쪽 위 숫자가 없는경우
        if j - 1 < 0:
            left_up = 0
        # 삼각형의 왼쪽 위 숫자가 있는경우            
        else:
            left_up = data[i - 1][j - 1]
        # 현재 숫자와 왼쪽 위와 오른쪽 위 중 큰 숫자를 더해서 리스트를 업데이트
        data[i][j] = data[i][j] + max(up, left_up)

print(max(data[n - 1])) # 결과 출력

# 해설
"""
n = int(input())
dp = [] # 다이나믹 프로그래밍을 위한 DP 테이블 초기화

for _ in range(n):
    dp.append(list(map(int, input().split())))

# 다이나믹 프로그래밍으로 2번째 줄부터 내려가면서 확인
for i in range(1, n):
    for j in range(i + 1):
        # 왼쪽 위에서 내려오는 경우
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i - 1][j - 1]
        # 바로 위에서 내려오는 경우
        if j == i:
            up = 0
        else:
            up = dp[i - 1][j]
        # 최대 합을 저장
        dp[i][j] = dp[i][j] + max(up_left, up)

print(max(dp[n - 1]))
"""
