import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

S, E = map(int, input().split())

INF = 100000 * 1000 + 1
distance = [INF] * (N+1)
distance[S] = 0

hq = []
heapq.heappush(hq, (0, S)) # 거리, 노드

while hq:
    dist, now = heapq.heappop(hq)
    
    if distance[now] < dist:
        continue
    
    for next_node, weight in graph[now]:
        cost = dist + weight
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(hq, (cost, next_node))
            
print(distance[E])