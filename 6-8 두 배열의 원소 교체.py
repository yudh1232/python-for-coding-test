# n, k를 공백으로 구분하여 입력받음
n, k = map(int, input().split())

# a의 원소들을 공백으로 구분하여 리스트에 넣음
data_a = list(map(int, input().split()))

# b의 원소들을 공백으로 구분하여 리스트에 넣음
data_b = list(map(int, input().split()))

# 리스트 a를 오름차순으로 정렬
data_a.sort()

# 리스트 b를 내림차순으로 정렬
data_b.sort(reverse=True)

# a[i] < b[i]이면 스왑하고, 아니면 반복문을 종료
for i in range(k):
    if data_a[i] < data_b[i]:
        data_a[i], data_b[i] = data_b[i], data_a[i]
    else:
        break

print(sum(data_a)) # 결과 출력

# 해설
"""
n, k = map(int, input().split()) # N과 K를 입력 받기
a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력받기
b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력받기

a.sort() # 배열 A는 오름차순 정렬 수행
b.sort(reverse=True) # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a)) # 배열 A의 모든 원소의 합을 출력
"""
