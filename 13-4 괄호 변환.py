def solution(p):
    # 입력이 빈 문자열인 경우, 빈 문자열을 반환
    if len(p) == 0:
        return p
    
    open = 0 # '('의 개수
    close = 0 # ')'의 개수
    is_proper = 1 # 올바른 괄호 문자열인지 나타내는 변수
    u = ''
    v = ''

    for i in range(len(p)):
        if p[i] == '(':
            open += 1
        if p[i] == ')':
            close += 1
        u += p[i]

        # 올바른 괄호 문자열이 아닐 때
        if close > open:
            is_proper = 0
        
        # 균형잡힌 괄호 문자열이 됐을 때
        if open == close:
            v += p[i + 1:]
            break
    
    # u가 올바른 괄호 문자열이라면
    if is_proper == 1:
        return u + solution(v)
    # u가 올바른 괄호 문자열이 아니라면
    else:
        s = '('
        s += solution(v)
        s += ')'
        for i in range(1, len(u) - 1):
            if u[i] == '(':
                s += ')'
            if u[i] == ')':
                s += '('
        return s
