def solution(food_times, k):
    index = 0
    while k > 0:
        # 남은 음식 찾기
        while food_times[index] == 0:
            index = (index + 1) % len(food_times)
        
        # 음식 섭취
        food_times[index] -= 1
        
        # 인덱스를 다음 음식으로 바꿈
        index = (index + 1) % len(food_times)
        
        k -= 1
    
    # 더 섭취할 음식이 없는 경우
    if max(food_times) < 1:
        return -1
    # 현재 인덱스의 음식이 안 남은 경우
    while food_times[index] == 0:
        index = (index + 1) % len(food_times)
    answer = index + 1
    return answer

food_times = [3, 1, 2]
k = 5
print(solution(food_times, k)) # 결과 출력
