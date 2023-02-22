import sys

n, m = map(int, sys.stdin.readline().split())

parent = []
for i in range(0, n+1):
  parent.append(i)

# 부모노드 찾기
def find(n):
  if n == parent[n]:
    return n

  return find(parent[n])

# u와 v가 속한 두 그래프를 하나로 합치기
def union(u, v):
  #두 노드의 루트노드 찾기
  x = find(u)
  y = find(v)

  if x == y:
    return

  # 두 루트노드 중 원소 값이 더 작은 루트노드를 그래프의 루트노드로 선택한다
  if x > y:
    parent[u] = y
    # 본인이 루트노드면 하위 노드도 같이 바꿔준다
    for i in range(1, n+1):
      if parent[i] == x:
        parent[i] = y
  else:
    parent[v] = x
    for i in range(1, n+1):
      if parent[i] == y:
        parent[i] = x


for i in range(m):
  u, v = map(int, sys.stdin.readline().split())  
  union(u, v)

cnt = 0

for i in range(1, n+1):
  if i in parent:
    cnt += 1


print(cnt)