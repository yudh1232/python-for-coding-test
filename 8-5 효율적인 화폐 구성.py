# n, m을 공백으로 구분하여 입력받음
n, m = map(int, input().split())

# 화폐의 가치를 입력받아 리스트에 넣음
value = []
for i in range(n):
    value.append(int(input()))

# 화폐의 가치를 오름차순으로 정렬
value.sort()

# DP를 위한 리스트
d = [0] * 10001

# 가능 경우 리스트
possible_case = []

for i in range(1, m + 1):
    # 가능한 d[i - k] + 1 중 최솟값이 d[i]가 된다 
    for k in value:
        if i < k:
            continue
        if d[i - k] != -1:
            possible_case.append(d[i - k])
    # d[i - k] 값이 없었을 경우
    if len(possible_case) == 0:
        d[i] = -1
    # d[i - k] 값이 있었을 경우
    else:
        d[i] = min(possible_case) + 1
        possible_case.clear()

print(d[m]) # 결과 출력

# 해설
"""
# 정수 N, M을 입력 받기
n, m = map(int, input().split())
# N개의 화폐 단위 정보를 입력 받기
array = []
for i in range(n):
    array.append(int(input()))

# 한 번 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [10001] * (m + 1)

# 다이나믹 프로그래밍(Dynamic Programming) 진행(보텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001: # (i - k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - array[i]] + 1)

# 계산된 결과 출력
if d[m] == 10001: # 최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
"""
