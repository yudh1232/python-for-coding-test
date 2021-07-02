# n, m을 공백으로 구분하여 입력받음
n, m = map(int, input().split())
# 떡의 개별 높이 h를 공백으로 구분하여 리스트에 넣음
h = list(map(int, input().split()))

# 절단기 높이의 최초값을 떡의 개별 높이들의 평균으로 초기화
cutter = int(sum(h) / n)

# 절단기의 높이를 조절해가며 m과 잘린 떡 길이의 합이 같아질 때까지 반복
while True:
    sum = 0 # 잘린 떡 길이의 합
    for i in range(n):
        # 떡의 길이가 절단기 높이보다 클 경우
        if h[i] > cutter:
            sum += h[i] - cutter
    # 잘린 떡 길이의 합이 m보다 큰 경우
    if sum > m:
        cutter += 1
    # 잘린 떡 길이의 합이 m보다 작은 경우
    elif sum < m:
        cutter -= 1
    # 잘린 떡 길이의 합이 m과 같은 경우
    else:
        break

print(cutter) # 결과 출력

# 해설
"""
# 떡의 개수(N)와 요청한 떡의 길이(M)을 입력받기
n, m = map(int, input().split())
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)
"""
