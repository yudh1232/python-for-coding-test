# 가로의 길이 n을 입력받음
n = int(input())

# DP를 위한 리스트
d = [0] * 1000

# 초기값 설정
d[0] = 1
d[1] = 3

for i in range(2, n):
    # d[i]는 d[i - 1]에 2 * 1 덮개를 추가했을 때의 경우와, d[i - 2]에 1 * 2 덮개 2개 또는 2 * 2 덮개를 추가했을 때의 경우의 합과 같다
    d[i] = d[i - 1] + 2 * d[i - 2]

print(d[n - 1] % 796796) # 결과 출력

# 해설
"""
# 정수 N을 입력 받기
n = int(input())

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 1001

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

# 계산된 결과 출력
print(d[n])
"""
