# 더 맵게 - heap
import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    
    while heap[0]<K:
        try:
            n= heapq.heappop(heap) + (heapq.heappop(heap)*2)
            heapq.heappush(heap,n)
        except IndexError:
            return -1
        answer += 1
    return answer