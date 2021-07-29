import heapq

n = int(input())
# 우선순위 큐 사용
heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

result = 0

while True:
    # 힙에 원소 1개만 남으면 반복종료
    if len(heap) == 1:
        break
    # 가장 작은 원소
    a = heapq.heappop(heap)
    # 두번째로 작은 원소
    b = heapq.heappop(heap)
    # 두 원소의 합을 result에 더함
    result += a + b
    # 두 원소의 합을 우선순위 큐에 다시 넣음
    heapq.heappush(heap, a + b)

print(result) # 결과 출력

# 해설
"""
import heapq

n = int(input())

# 힙(Heap)에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

# 힙(Heap)에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)
"""
