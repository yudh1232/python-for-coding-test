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
