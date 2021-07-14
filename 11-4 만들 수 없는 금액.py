import copy

# 동전의 개수 n을 입력받음
n = int(input())
# 동전 데이터를 입력받아 리스트에 넣음
data = list(map(int, input().split()))
data.sort()

# 만들 수 있는 금액을 담는 리스트
possible = []
possible.append(data[0])

for i in range(1, n):
    temp = copy.deepcopy(possible)
    # possible 리스트에 현재 동전을 더한 값을 추가함
    for possible_coin in possible:
        temp.append(data[i] + possible_coin)
    possible = copy.deepcopy(temp)

    # possible 리스트에 현재 동전을 추가함
    if data[i] not in possible:
        possible.append(data[i])

# 1부터 시작하고 1씩 증가하여 만들 수 없는 금액이 나오면 반복 종료
result = 1
while True:
    if result not in possible:
        break
    result += 1

print(result) # 결과 출력

# 해설
"""
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    # 만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    target += x

# 만들 수 없는 금액 출력
print(target)
"""
