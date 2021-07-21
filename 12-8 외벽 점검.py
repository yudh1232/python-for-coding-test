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
