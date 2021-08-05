# n을 입력받음
n = int(input())

# 못생긴 수를 담을 리스트, 다이나믹프로그래밍 이용
ugly_num = [0] * n
ugly_num[0] = 1

# 어떤 못생긴 수 까지 2, 3, 5를 곱했는지 나타내는 인덱스 
idx2, idx3, idx5 = 0, 0, 0
# 못생긴 수에 2, 3, 5를 곱한 값
next2, next3, next5 = 2, 3, 5 

for i in range(1, n):
    value = min(next2, next3, next5)
    ugly_num[i] = value

    # next2가 가장 작았다면
    if value == next2:
        # 다음 못생긴수에 2를 곱한값을 next2로 함
        idx2 += 1
        next2 = ugly_num[idx2] * 2
     # next3이 가장 작았다면
    if value == next3:
        # 다음 못생긴수에 3을 곱한값을 next2로 함
        idx3 += 1
        next3 = ugly_num[idx3] * 3
     # next5가 가장 작았다면
    if value == next5:
        # 다음 못생긴수에 5를 곱한값을 next2로 함
        idx5 += 1
        next5 = ugly_num[idx5] * 5

print(ugly_num[n - 1]) # 결과 출력

# 해설
"""
n = int(input())

ugly = [0] * n # 못생긴 수를 담기 위한 테이블 (1차원 DP 테이블)
ugly[0] = 1 # 첫 번째 못생긴 수는 1

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음에 곱셈 값을 초기화
next2, next3, next5 = 2, 3, 5

# 1부터 n까지의 못생긴 수들을 찾기
for l in range(1, n):
    # 가능한 곱셈 결과 중에서 가장 작은 수를 선택
    ugly[l] = min(next2, next3, next5)
    # 인덱스에 따라서 곱셈 결과를 증가
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

# n번째 못생긴 수를 출력
print(ugly[n - 1])
"""
