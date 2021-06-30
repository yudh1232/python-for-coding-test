n = int(input()) # n을 입력받음
h, m, s = 0, 0, 0 # 시, 분, 초 초기화
count = 0 # 결과 값 초기화

# N시 59분 59초가 될때까지 1초씩 더해가며 반복
while True:
    if h == n + 1:
        break

    if s // 60 == 1:
        m += 1
        s = 0
    if m // 60 == 1:
        h += 1
        m = 0
    
    # 시, 분, 초 순서대로 3이 있는지 확인 후 카운트 함
    if h % 10 == 3:
        count += 1
    elif m // 10 == 3:
        count += 1
    elif m % 10 == 3:
        count += 1
    elif s // 10 == 3:
        count += 1
    elif s % 10 ==3:
        count += 1

    s += 1

print(count) # 결과 출력

# 해설
"""
# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
"""
