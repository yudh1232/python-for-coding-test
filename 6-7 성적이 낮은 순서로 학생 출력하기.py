n = int(input()) # n을 입력받음

data = [] # 이름과 성적을 담는 리스트
scores = [] # 성적을 담는 리스트

# n개의 이믈과 성적을 입력받음
for i in range(n):
    data.append(list(input().split()))
    data[i][1] = int(data[i][1])
    scores.append(data[i][1])

# 성적을 기준으로 정렬
scores.sort()

# 낮은 성적부터 해당하는 이름을 찾아 결과 출력
for score in scores:
    for i in range(n):
        if score in data[i]:
            print(data[i][0], end = ' ')
            break

# 해설
"""
# N을 입력받기
n = int(input())

# N명의 학생 정보를 입력받아 리스트에 저장
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

# 키(Key)를 이용하여, 점수를 기준으로 정렬
array = sorted(array, key=lambda student: student[1])

# 정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end = ' ')
"""
