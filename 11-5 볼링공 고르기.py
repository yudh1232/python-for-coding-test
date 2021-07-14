# n, m을 공백으로 구분하여 입력받음
n, m = map(int, input().split())
# 공의 무게를 입력받아 리스트에 넣음
data = list(map(int, input().split()))
# 특정 무게의 공이 몇 개 있는지 나타내는 리스트
array = [0] * m

# 공 리스트를 순회하여 특정 무게의 공이 몇 개 있는지 셈
for i in range(n):
    array[data[i] - 1] += 1

result = 0

# 무게가 1인 공부터 나머지 공들의 개수와 곱한 값을 result에 더해감
for i in range(m):
    n -= array[i]
    result += n * array[i]

print(result) # 결과 출력

# 해설
"""
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)
"""
