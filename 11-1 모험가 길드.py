# 모험가의 수 n을 입력받음
n = int(input())
# 각 모험가의 공포도를 공백을 기준으로 입력받아 리스트에 넣음
data = list(map(int, input().split()))
# 각 모험가의 공포도를 오름차순으로 정렬함
data.sort()

# 그룹 리스트
group = []

result = 0 # 그룹 수의 최댓값

for i in range(n):
    # 그룹에 모험가를 추가
    group.append(data[i])
    # 그룹에 있는 모험가의 최고 공포도가 모험가의 수보다 작거나 같을 경우 그룹 확정
    if max(group) <= len(group):
        result += 1
        group.clear()

print(result) # 결과 출력

# 해설
"""
# n = int(input())
# data = list(map(int, input().split()))
# data.sort()

# result = 0 # 총 그룹의 수
# count = 0 # 현재 그룹에 포함된 모험가의 수

# for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
#     count += 1 # 현재 그룹에 해당 모험가를 포함시키기
#     if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
#         result += 1 # 총 그룹의 수 증가시키기
#         count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

# print(result) # 총 그룹의 수 출력
"""
