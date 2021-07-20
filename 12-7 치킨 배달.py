from itertools import combinations

n, m = map(int, input().split())
data = []
for i in range(n):
    data.append(list(map(int, input().split())))

# 집
house = []
# 치킨집
chicken_house = []


for x in range(n):
    for y in range(n):
        # 집이라면 집 리스트에 넣음
        if data[x][y] == 1:
            house.append((x, y))
        # 치킨집이라면 치킨집 리스트에 넣음
        if data[x][y] == 2:
            chicken_house.append((x, y))

# 치킨집 중에서 m개를 뽑는 조합을 구함
combination_list = list(combinations(chicken_house, m))

result = 100000

# 각 치킨집 조합에 대하여 도시의 치킨 거리가 가장 작게 되는 조합을 구함
for combination in combination_list:
    sum = 0
    for hx, hy in house:
        min_distance = 100000
        for cx, cy in combination:
            distance = abs(hx - cx) + abs(hy - cy)
            min_distance = min(min_distance, distance)
        sum += min_distance

    result = min(result, sum)
    
print(result) # 결과 출력

# 해설
"""
from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) # 일반 집
        elif data[c] == 2:
            chicken.append((r, c)) # 치킨집

# 모든 치킨 집 중에서 m개의 치킨 집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidate):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨 집을 찾기
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨 집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 반환
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)
"""
