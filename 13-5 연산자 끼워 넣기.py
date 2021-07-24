from itertools import permutations

# 연산자에 따라 계산하는 함수 (0: '+', 1: '-', 2: '*', 3: '/'')
def calculate(operand1, operand2, operator):
    if operator == 0:
        calculate_result = operand1 + operand2
    elif operator == 1:
        calculate_result = operand1 - operand2
    elif operator == 2:
        calculate_result = operand1 * operand2
    elif operator == 3:
        if operand1 < 0:
            calculate_result = -(-operand1 // operand2)
        else:
            calculate_result = operand1 // operand2
    return calculate_result

# n을 입력받음
n = int(input())
# 수열을 입력받음
sequence = list(map(int, input().split()))
# 각 연산자의 개수를 입력받음
operator = list(map(int, input().split()))

# 연산자를 나열해 리스트에 넣음 (0: '+', 1: '-', 2: '*', 3: '/'')
operator_list = []
for i in range(4):
    while operator[i] != 0:
        operator_list.append(i)
        operator[i] -= 1

maximum = -int(1e9)
minimum = int(1e9)

# 연산자를 배치하는 모든 경우에 대해서
for operator_order in permutations(operator_list):
    result = sequence[0]
    for i in range(1, n):
        # 계산
        result = calculate(result, sequence[i], operator_order[i - 1])
    maximum = max(maximum, result)
    minimum = min(minimum, result)

# 결과 출력
print(maximum)
print(minimum)

# 해설
"""
n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색 (DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i])) # 나눌 때는 나머지를 제거
            div += 1

# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(max_value)
print(min_value)
"""
