# 문자열 s를 입력받음
s = input()
# 이전 숫자와 현재 숫자가 다를때마다 1씩 증가하는 변수
count = 0

for i in range(1, len(s)):
    # 이전 숫자와 현재 숫자가 다를때마다 카운팅
    if s[i - 1] != s[i]:
        count += 1

if count % 2 == 0:
    result = int(count / 2)
else:
    result = int(count / 2) + 1

print(result) # 결과 출력

# 해설
"""
# data = input()
# count0 = 0 # 전부 0으로 바꾸는 경우
# count1 = 0 # 전부 1로 바꾸는 경우

# # 첫 번째 원소에 대해서 처리
# if data[0] == '1':
#     count0 += 1
# else:
#     count1 += 1

# # 두 번째 원소부터 모든 원소를 확인하며
# for i in range(len(data) - 1):
#     if data[i] != data[i + 1]:
#         # 다음 수에서 1로 바뀌는 경우
#         if data[i + 1] == '1':
#             count0 += 1
#         # 다음 수에서 0으로 바뀌는 경우
#         else:
#             count1 += 1

# print(min(count0, count1))
"""
