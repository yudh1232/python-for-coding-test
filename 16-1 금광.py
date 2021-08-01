# 1
# 3 4   
# 1 3 3 2 2 1 4 1 0 6 4 7

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    gold_mine = [([0] * m) for _ in range(n)]
    data = list(map(int, input().split()))
    
    for i in range(n):
        for j in range(m):
            gold_mine[i][j] = data[m * i + j]
    
    dx = [-1, 0, 1]
    
    dp_value = [-1] * (m)
    dp_idx = [-1] * (m)
    
    max_value = -1
    idx = -1
    for i in range(n):
        if gold_mine[i][0] > max_value:
            max_value = gold_mine[i][0]
            idx = i
    dp_value[0] = max_value
    dp_idx[0] = idx
    
    for j in range(1, m):
        max_value = -1
        idx = -1
        
        for i in range(n):
            if gold_mine[i][j] > max_value:
                max_value = gold_mine[i][j]
                idx = i
                
        if abs(idx - dp_idx[j - 1]) <= 1:
            dp_value[j] = dp_value[j - 1] + max_value
            dp_idx[j] = idx
        else:
            previous_idx = dp_idx[j - 1]
            if previous_idx == 0:
                next_value = max(gold_mine[previous_idx][j], gold_mine[previous_idx + 1][j])
            if previous_idx == n - 1:
                next_value = max(gold_mine[previous_idx][j], gold_mine[previous_idx - 1][j])
            else:
                next_value = max(gold_mine[previous_idx][j], gold_mine[previous_idx + 1][j], gold_mine[previous_idx - 1][j])
            if max_value > dp_value[j - 1] + next_value:
                height_gap = previous_idx - idx
            
    print('height_gap:', height_gap)
    print('value:', dp_value)
    print('idx:', dp_idx)
