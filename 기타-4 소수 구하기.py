import math

# m, n을 입력받음
m, n = map(int, input().split())

# 1부터 1000000까지 소수인지 아닌지 나타내는 리스트 생성 
array = [True] * 1000001
# 1은 소수가 아님
array[1] = False

# 에라토스테네스의 체
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

# 결과 출력
for i in range(m, n + 1):
    if array[i]:
        print(i)
