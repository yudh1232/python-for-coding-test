# 식량창고의 개수 n을 입력받음
n = int(input())

# 식량창고 n개의 식량 개수를 입력받아 리스트에 넣음
food = list(map(int, input().split()))
# i번 식량창고에 food[i]을 대응하기 위해서 앞에 0을 채워줌
food.insert(0, 0)

# DP 이용하기 위한 리스트
result = [0] * 101

# i번째 식량창고가 선택되었는지 나타내는 리스트
selected = [0] * 101

for i in range(1, n + 1):
    # i - 1번째가 선택되지 않았다면 i번째는 무조건 선택
    if selected[i - 1] == 0:
        result[i] = result[i - 1] + food[i]
        selected[i] = 1

    # i - 1번째가 선택되었다면
    else:
        # i - 2번째까지의 결과와 i번째의 합이 i - 1번째까지의 결과보다 크다면 i번째를 선택
        if result[i - 2] + food[i] > result[i - 1]:
            result[i] = result[i - 2] + food[i]
            selected[i - 1] = 0
            selected[i] = 1
        # 작다면 i번째를 선택하지 않음
        else:
            result[i] = result[i - 1]

print(result[n]) # 결과 출력

# 해설
"""
# 정수 N을 입력 받기
n = int(input())
# 모든 식량 정보 입력 받기
array = list(map(int, input().split()))

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
d[0] = array[0]
d[1] = max(array[0], array[1]) 
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

# 계산된 결과 출력
print(d[n - 1])
"""
