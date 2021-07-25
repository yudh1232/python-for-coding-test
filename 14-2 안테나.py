import sys
input = sys.stdin.readline

# 집의 수 n을 입력받음
n = int(input())
# 집들의 위치를 입력받아 리스트에 넣음
house = list(map(int, input().split()))

# 집들의 위치를 오름차순으로 정렬
house.sort()

# 정렬된 집들의 위치 중에서 중간값을 구함
# n이 짝수라면
if n % 2 == 0:
    if house[int(n / 2) - 1] <= house[int(n / 2)]:
        print(house[int(n / 2) - 1])
    else:
        print(house[int(n / 2)])
# n이 홀수라면
else:
    print(house[int(n / 2)])
    
# 해설
"""
n = int(input())
a = list(map(int, input().split()))
a.sort()

# 중간값(median)을 출력
print(a[(n - 1) // 2])
"""
