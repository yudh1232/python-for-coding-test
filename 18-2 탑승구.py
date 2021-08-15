# g와 p를 입력받음
g = int(input())
p = int(input())

# n번 탑승구가 도킹되어있는지 나타내는 리스트
gate = [0] * (g + 1)

count = 0 # 도킹한 비행기 수
flag = 0 # 더 이상 도킹할 수 없는지 나타내는 플래그

for _ in range(p):
    gi = int(input())
    for i in range(gi, 0, -1):
        # gate gi가 비어있으면 도킹하고, 안 비어있으면 gate (gi - 1)을 살펴보러 감
        if gate[i] == 0:
            gate[i] = 1
            break
        else:
            # gi이하의 모든 게이트가 다 안 비어있으면 
            if i == 1:
                flag = 1
    
    # 더 이상 도킹할 수 없으면
    if flag == 1:
        break
    
    # 도킹한 비행기 수 증가
    count += 1

print(count) # 결과 출력
