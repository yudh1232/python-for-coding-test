from bisect import bisect_left, bisect_right

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

def solution(words, queries):
    # word를 뒤집은 것들의 리스트 reversed_words를 생성
    reversed_words = []
    for word in words:
        reversed_words.append(word[::-1])
    # words와 reversed_words를 정렬
    words.sort()
    reversed_words.sort()
    answer = []

    # 모든 query에 대하여
    for query in queries:
        count = 0 # 매치된 단어의 개수
        q_len = len(query) # query의 길이
        new_query = '' # '?'를 'z'로 바꿔 처리할 new_query
        
        # '?'로 시작하는 query일 경우
        if query[0] == '?':
            # query를 뒤집음
            query = query[::-1]
            # '?'를 'z'로 바꿔 처리하여 new_query 생성
            for i in range(q_len):
                if query[i] == '?':
                    new_query += 'z'
                else:
                    new_query += query[i]
            # query의 '?'를 제외한 부분을 포함한 reversed_word에 대하여
            for j in range(bisect_left(reversed_words, query), bisect_right(reversed_words, new_query)):
                # query와 길이도 같다면 매치된 단어임
                if len(reversed_words[j]) == q_len:
                    count += 1
            answer.append(count) # 결과 리스트에 넣음
        
        # 알파벳으로 시작하는 query일 경우
        else:
            # '?'를 'z'로 바꿔 처리하여 new_query 생성
            for i in range(q_len):
                if query[i] == '?':
                    new_query += 'z'
                else:
                    new_query += query[i]
            # query의 '?'를 제외한 부분을 포함한 word에 대하여
            for j in range(bisect_left(words, query), bisect_right(words, new_query)):
                # query와 길이도 같다면 매치된 단어임
                if len(words[j]) == q_len:
                    count += 1
            answer.append(count) # 결과 리스트에 넣음

    return answer

solution(words, queries)

# 해설
"""
from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 모든 단어들을 길이마다 나누어서 저장하기 위한 리스트
array = [[] for _ in range(10001)]
# 모든 단어들을 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words: # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        array[len(word)].append(word) # 단어를 삽입
        reversed_array[len(word)].append(word[::-1]) # 단어를 뒤집어서 삽입

    for i in range(10001): # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
        array[i].sort()
        reversed_array[i].sort()

    for q in queries: # 쿼리를 하나씩 확인하며 처리
        if q[0] != '?': # 접미사에 와일드 카드가 붙은 경우
            res = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else: # 접두사에 와일드 카드가 붙은 경우
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        # 검색된 단어의 개수를 저장
        answer.append(res)
    return answer
"""
