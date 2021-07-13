# 문자열 s를 입력받음
s = input()

result = 0

for i in range(len(s)):
    # 이전값 또는 현재값이 1이하 일 때는 더함
    if result <= 1 or int(s[i]) <= 1:
        result += int(s[i])
    # 이전값과 현재값 모두 2이상 일 때는 곱함
    else:
        result *= int(s[i])

print(result) # 결과 출력

# 해설
"""
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
"""
