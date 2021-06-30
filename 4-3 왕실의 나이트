s = input() # 현재 나이트의 위치를 입력받음

a = ord(s[0]) # 알파벳으로 된 첫 번째 글자를 정수로 바꿈
b = int(s[1]) # 숫자로 된 두 번째 글자를 정수로 바꿈

count = 0 # 결과 값

# 나이트가 이동할 수 있는 지 체크('a'와 'h'의 정수 값은 각각 97과 104)
if a + 2 <= 104:
    if b + 1 <= 8:
        count += 1
    if b - 1 >= 1:
        count += 1

if a + 1 <= 104:
    if b + 2 <= 8:
        count += 1
    if b - 2 >= 1:
        count += 1

if a - 1 >= 97:
    if b + 2 <= 8:
        count += 1
    if b - 2 >= 1:
        count += 1

if a - 2 >= 97:
    if b + 1 <= 8:
        count += 1
    if b - 1 >= 1:
        count += 1

print(count) # 결과 출력

# 해설
"""
# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >=1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)
"""
