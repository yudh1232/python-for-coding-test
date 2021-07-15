# n을 입력받음
n = input()

# n을 반으로 나눠서 각 숫자를 정수로 담을 리스트
n1 = []
n2 = []

for i in range(len(n)):
    # n의 앞쪽 절반은 n1에 넣음
    if i < len(n) / 2:
        n1.append(int(n[i]))
    # n의 뒤쪽 절반은 n2에 넣음
    else:
        n2.append(int(n[i]))

# n1과 n2의 각 자릿수의 합이 같다면
if sum(n1) == sum(n2):
    print('LUCKY')
# n1과 n2의 각 자릿수의 합이 다르다면
else:
    print('READY')

# 해설
"""
n = input()
length = len(n) # 점수값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print('LUCKY')
else:
    print('READY')
"""
