from itertools import combinations

# l, c를 입력받음
l, c = map(int, input().split())

# 문자들을 입력받고 정렬
data = list(input().split())
data.sort()

# 각 조합에 대하여
for combi in list(combinations(data, l)):
    # 모음 개수
    vowel_count = 0
    # 각 문자가 모음일 경우, 모음 개수 += 1
    for i in range(len(combi)):
        if combi[i] == 'a' or combi[i] == 'e' or combi[i] == 'i' or combi[i] == 'o' or combi[i] == 'u':
            vowel_count += 1
    
    # 모음개수가 1이상이고, 자음개수가 2이상일 경우 출력
    if vowel_count >= 1 and l - vowel_count >= 2:
        print(''.join(combi))
