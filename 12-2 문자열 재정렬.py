# 문자열 s를 입력받음
s = input()

# 알파벳들을 넣을 리스트
alphabet = []
# 숫자들을 넣을 리스트
number = []

# 알파벳과 숫자를 분리
for char in s:
    # 문자가 A~Z일 경우
    if ord(char) >= 65 and ord(char) <= 90:
        alphabet.append(ord(char))
    # 문자가 0~9일 경우
    elif ord(char) >= 48 and ord(char) <= 57:
        number.append(int(char))

# 코드로 저장된 알파벳을 정렬
alphabet.sort()

# 정렬된 코드를 알파벳으로 출력
for item in alphabet:
    print(chr(item), end = '')
# 숫자의 합을 출력
print(sum(number))

# 해설
"""
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))
"""
