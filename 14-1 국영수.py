# n을 입력받음
n = int(input())
# n쌍의 이름과 점수를 입력받아 넣을 리스트
data = []

# n쌍의 이름과 점수를 입력받아 리스트에 넣음
for _ in range(n):
    name, korean, english, math = input().split()
    korean = int(korean)
    english = int(english)
    math = int(math)
    data.append((korean, english, math, name))

# 국어 내림차순, 수학 오름차순, 영어 내림차순, 이름 오름차순으로 정렬
sorted_data = sorted(data, key = lambda x : (-x[0], x[1], -x[2], x[3]))

# 결과 출력
for i in range(n):
    print(sorted_data[i][3])
    
# 해설
"""
n = int(input())
students = [] # 학생 정보를 담을 리스트

# 모든 학생 정보를 입력 받기
for _ in range(n):
    students.append(input().split())

'''
[ 정렬 기준 ]
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
3) 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
4) 네 번째 원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순 정렬
'''
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])
"""
