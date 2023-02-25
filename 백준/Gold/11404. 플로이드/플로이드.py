import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

bus_cost = [[float('inf')] * (n+1) for _ in range(n+1)]
             
for _ in range(m):
  s, e, c = map(int, sys.stdin.readline().split())
  bus_cost[s][e] = min(c, bus_cost[s][e])

# 플로이드-워셜 알고리즘
for k in range(1, n+1): # k는 어느 정류장을 거쳐갈건지. 경로 for문이 가장 상위 단계여야 누락되지 않는다
  for i in range(1, n+1):
    for j in range(1, n+1):
      if i == j: # 자기 자신으로 오는 경우는 없다고 함
        bus_cost[i][j] = 0
      else: # 경로 거치는 것 or 직접 가는 것 or 이전 경로들
        bus_cost[i][j] = min(bus_cost[i][j], bus_cost[i][k] + bus_cost[k][j])

for i in range(1, n+1) :
  for j in range(1, n+1):
    if bus_cost[i][j] == float('inf'):
      print(0, end = " ")
    else:
      print(bus_cost[i][j], end = " ")
  print()
  