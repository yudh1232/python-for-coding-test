from itertools import permutations

def solution(n, weak, dist):
    weak_length = len(weak)
    # 외벽이 원이므로 접근하기 쉽게 외벽을 두배로 늘려 1차원화 시킴
    for i in range(weak_length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1

    # 모든 취약점에 대하여
    for i in range(weak_length):
        # 점검 시작점 설정
        start = weak[i]
        # 친구들의 모든 순열에 대하여
        for permutation in list(permutations(dist, len(dist))):
            position = start
            index = i
            friends_count = 0
            check_count = 0
            for j in range(len(dist)):
                # 친구 투입
                friends_count += 1
                position += permutation[j]
                # 친구가 점검한 외벽을 셈
                while index < 2 * weak_length:
                    if position < weak[index]:
                        break
                    index += 1
                    check_count += 1

                # 다음 친구의 시작지점 설정
                if index < 2 * weak_length:     
                    position = weak[index]
                
                # 외벽 점검을 마친 경우
                if check_count >= weak_length:
                    answer = min(answer, friends_count)
                    break
    
    # 모든 경우에 대하여 외벽 점검을 못한 경우
    if answer == len(dist) + 1:
        return -1

    return answer

# 해설
"""
from itertools import permutations

def solution(n, weak, dist):
    # 길이를 2배로 늘려서 '원형'을 일자 형태로 변형
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)
    answer = len(dist) + 1 # 투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화
    # 0부터 length - 1까지의 위치를 각각 시작점으로 설정
    for start in range(length):
        # 친구를 나열하는 모든 경우 각각에 대하여 확인
        for friends in list(permutations(dist, len(dist))):
            count = 1 # 투입할 친구의 수
            # 해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]
            # 시작점부터 모든 취약한 지점을 확인
            for index in range(start, start + length):
                # 점검할 수 있는 위치를 벗어나는 경우
                if position < weak[index]:
                    count += 1 # 새로운 친구를 투입
                    if count > len(dist): # 더 투입이 불가능하다면 종료
                        break
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count) # 최솟값 계산
    if answer > len(dist):
        return -1
    return answer
"""
