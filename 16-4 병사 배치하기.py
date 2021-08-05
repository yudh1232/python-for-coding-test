# n을 입력받음
n = int(input())
# 병사들의 전투력을 입력받아 리스트에 넣음
data = list(map(int, input().split()))
# LIS 크기를 저장할 dp 테이블 생성
dp = [1] * n

# 오름차순으로 계산하기 위해 배열을 뒤집음
data.reverse()

# LIS 크기 계산
for i in range(1, n):
    for j in range(0, i):
        if data[i] > data[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp)) # 결과 출력

# 해설
"""
n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 '최장 증가 부분 수열' 문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수를 출력
print(n - max(dp))
"""
