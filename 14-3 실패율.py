N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    # 전체 유저 수
    total_user = len(stages)
    # 각 스테이지에 멈춰있는 유저의 수
    stage_user = [0] * (N + 2)
    # 각 스테이지별 실패율
    failure_rate_list = []
    
    # 각 스테이지에 멈춰있는 유저의 수를 계산
    for i in stages:
        stage_user[i] += 1
    
    for i in range(1, N + 1):
        # 스테이지에 도달한 유저가 없는 경우
        if total_user == 0:
            # 실패율을 0으로 함
            failure_rate_list.append((i, 0))
        # 스테이지에 도달한 유저가 있는 경우
        else:
            # 실패율: 스테이지에 멈춘 유저의 수 / 이전 스테이지를 통과한 유저의 수
            failure_rate = stage_user[i] / total_user
            # 다음 스테이지에 갈 사용자: 이전 스테이지를 통과한 유저의 수 - 스테이지에 멈춘 유저의 수
            total_user -= stage_user[i]
            failure_rate_list.append((i, failure_rate))
    
    # 실패율이 높은 스테이지부터 내림차순으로 정렬, 작은 스테이지 번호부터 오름차순으로 정렬
    failure_rate_list.sort(key = lambda x : -x[1])

    answer = []
    for rate in failure_rate_list:
        answer.append(rate[0])
    return answer

print(solution(N, stages)) # 결과 출력

# 해설
"""
def solution(N, stages):
    answer = []
    length = len(stages)

    # 스테이지 번호를 1부터 N까지 증가시키며
    for i in range(1, N + 1):
        # 해당 스테이지에 머물러 있는 사람의 수 계산
        count = stages.count(i)
        
        # 실패율 계산
        if length == 0:
            fail = 0
        else:
            fail = count / length
        
        # 리스트에 (스테이지 번호, 실패율) 원소 삽입
        answer.append((i, fail))
        length -= count

    # 실패율을 기준으로 각 스테이지를 내림차순 정렬
    answer = sorted(answer, key=lambda t: t[1], reverse=True)
    
    # 정렬된 스테이지 번호 반환
    answer = [i[0] for i in answer]
    return answer
"""
