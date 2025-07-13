import sys

input = sys.stdin.readline

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
INF = 10000 * (N-1)
distance = [INF] * (N+1) # 시작 노드에서 i번 노드까지의 최단거리 저장
distance[1] = 0

for _ in range(N-1):
    for u, v, w in edges:
        if distance[u] != INF and distance[u] + w < distance[v]:
            distance[v] = distance[u] + w
        
for u, v, w in edges:
    if distance[u] != INF and distance[u] + w < distance[v]:
        print(-1)
        break
else:
    for i in range(2, N + 1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])