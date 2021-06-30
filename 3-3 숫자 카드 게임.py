n, m = map(int, input().split()) # n, m을 공백으로 구분하여 입력받음

result = 0 # 결과 값

# 모든 행을 순회할 때까지
for i in range(n):
  # 한 행을 공백으로 구분하여 입력받음
  data = list(map(int, input().split()))
  
  minimum = min(data) # 현재 행의 최솟값

  # 현재행의 최솟값이 이전의 최솟값보다 클 경우 스왑
  if minimum > result:
    result = minimum

print(result) # 결과 값 출력

# 해설 1
"""
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = min(data)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result) # 최종 답안 출력
"""

# 해설 2
"""
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
# 한 줄씩 입력받아 확인
for i in range(n):
  data = list(map(int, input().split()))
  # 현재 줄에서 '가장 작은 수' 찾기
  min_value = 10001
  for a in data:
    min_value = min(min_value, a)
  # '가장 작은 수'들 중에서 가장 큰 수 찾기
  result = max(result, min_value)

print(result) # 최종 답안 출력
"""
