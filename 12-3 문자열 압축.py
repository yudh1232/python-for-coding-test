# 테스트 케이스
test_case = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]

# 테스트 케이스 중 하나
s = "xababcdcdababcdcd"

# 문자열 중 가장 짧은 것의 길이, result 값 초기화
result = 1000

# 압축 단위를 1부터 1씩 늘려가며 확인
for i in range(1, len(s) + 1):
    # 현재 단위 문자열 초기화
    current = ''
    # 압축 결과 문자열 초기화
    string = ''
    # 문자열에서 단위만큼씩 확인
    for j in range(0, len(s), i):
        # 문자열의 첫 단위일 경우
        if len(current) == 0:
            current = s[j:j + i]
            count = 1
        # 문자열의 첫 단위가 아니면서, 이전 단위와 같을 경우
        elif current == s[j:j + i]:
            count += 1
        # 문자열의 첫 단위가 아니면서, 이전 단위와 같을 경우
        else:
            if count == 1:
                string += current
            else:
                string += str(count) + current
            current = s[j:j + i]
            count = 1
    
    # 마지막 단위까지 살펴본 후, count와 current에 남아있는 값을 string에 넣어줌
    if count == 1:
        string += current
    else:
        string += str(count) + current

    length = len(string)
    result = min(result, length)

print(result) # 결과 출력
