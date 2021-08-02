t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    gold_mine = [([0] * m) for _ in range(n)]
    data = list(map(int, input().split()))
    
    # 금광 2차원 리스트 생성
    for i in range(n):
        for j in range(m):
            gold_mine[i][j] = data[m * i + j]
    
    # DP 2차원 리스트를 생성하고 0열을 채움
    dp = [([-1] * m) for _ in range(n)]
    for i in range(n):
        dp[i][0] = gold_mine[i][0]
    
    # 1열부터 (m - 1)열까지
    for j in range(1, m):
        왼쪽 위, 왼쪽, 왼쪽 아래 중 최대값을 구해서 현재 위치의 값을 구함
        for i in range(n):
            if i == 0:
                dp[i][j] = max(gold_mine[i][j] + dp[i][j - 1], gold_mine[i][j] + dp[i + 1][j - 1])
            elif i == n - 1:
                dp[i][j] = max(gold_mine[i][j] + dp[i - 1][j - 1], gold_mine[i][j] + dp[i][j - 1])
            else:
                dp[i][j] = max(gold_mine[i][j] + dp[i - 1][j - 1], gold_mine[i][j] + dp[i][j - 1], gold_mine[i][j] + dp[i + 1][j - 1])
    
    # DP 2차원 리스트의 최대값을 구함 
    result = max(map(max, dp))
    print(result) # 결과 출력
    
# 해설
"""
# 테스트 케이스(Test Case) 입력
for tc in range(int(input())):
    # 금광 정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index + m])
        index += m

    # 다이나믹 프로그래밍 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래에서 오는 경우
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽에서 오는 경우
            left = dp[i][j - 1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m - 1])

    print(result)
"""
