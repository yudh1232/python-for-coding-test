# 테스트 케이스
test_case = ["aabbaccc", "ababcdcdababcdcd", "abcabcdede", "abcabcabcabcdededededede", "xababcdcdababcdcd"]

# 테스트 케이스 중 하나
s = "xababcdcdababcdcd"

# 문자열 중 가장 짧은 것의 길이, result 값 초기화
result = len(s)

# 압축 단위를 1부터 1씩 늘려가며 확인
for i in range(1, len(s) // 2 + 1):
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

# 해설
"""
def solution(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            # 이전 상태와 동일하다면 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            # 다른 문자열이 나왔따면(더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 상태 초기화
                count = 1
        # 남아 있는 문자열에 대해서 처리
        compressed += str(count) + prev if count >= 2 else prev
        # 만들어지는 압축 문자열이 가장 짧은 것이 정답
        answer = min(answer, len(compressed))
    return answer
"""
