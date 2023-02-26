import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

bus_cost = [[float('inf')] * (n+1) for _ in range(n+1)]
             
for _ in range(m):
  s, e, c = map(int, input().split())
  bus_cost[s][e] = min(c, bus_cost[s][e])

# 플로이드-워셜 알고리즘
for k in range(1, n+1): # k는 어느 정류장을 거쳐갈건지. 경로 for문이 가장 상위 단계여야 누락되지 않는다
    bus_cost[k][k] = 0 # 시작도시와 도착도시가 같은 경우는 없다
    for i in range(1, n+1):
        for j in range(1, n+1):
            bus_cost[i][j] = min(bus_cost[i][j], bus_cost[i][k] + bus_cost[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        print(bus_cost[i][j] if bus_cost[i][j] != float('inf') else 0, end = " ")
    print()
  