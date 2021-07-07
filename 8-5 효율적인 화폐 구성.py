# n, m을 공백으로 구분하여 입력받음
n, m = map(int, input().split())

# 화폐의 가치를 입력받아 리스트에 넣음
value = []
for i in range(n):
    value.append(int(input()))

# 화폐의 가치를 오름차순으로 정렬
value.sort()
