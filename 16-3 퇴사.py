t = [] # 각 상담의 시간 리스트
p = [] # 각 상담의 페이 리스트

# n을 입력받음
n = int(input())
# 시간과 페이를 입력받음
for _ in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)

# 다이나믹 프로그래밍을 위한 리스트
dp = [0] * (n + 1)    

max_pay = 0 
# 다이나믹 프로그래밍
for i in range(n - 1, -1, -1):
    # 이번 상담을 시간안에 끝낼 수 있는 경우
    if i + t[i] <= n:
        # (이번 상담의 페이 + 이번 상담이 끝난 이후의 페이)를 뒤에서부터 계속 업데이트
        dp[i] = max(p[i] + dp[i + t[i]], max_pay)
        max_pay = dp[i]
    # 이번 상담을 시간안에 끝낼 수 없는 경우
    else:
        dp[i] = max_pay

print(max_pay) # 결과 출력

# 해설
"""
n = int(input()) # 전체 상담 개수
t = [] # 각 상담을 완료하는데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n - 1, -1, -1):
    time = t[i] + i
    # 상담이 기간 안에 끝나는 경우
    if time <= n:
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    # 상담이 기간을 벗어나는 경우
    else:
        dp[i] = max_value

print(max_value)
"""
