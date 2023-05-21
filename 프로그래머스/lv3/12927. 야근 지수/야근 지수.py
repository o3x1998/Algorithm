import heapq

def solution(n, works):
    answer = 0
    max_heap = [] # 최대힙 사용
    
    for w in works:
        heapq.heappush(max_heap, (-w, w))
        
    for i in range(n):
        if max_heap[0][1] > 0:
            x = heapq.heappop(max_heap)[1] - 1
            heapq.heappush(max_heap, (-x, x))
    
    for i in range(len(max_heap)):
        answer += (max_heap[i][1]**2)
    
    return answer