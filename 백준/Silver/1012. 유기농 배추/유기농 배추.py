T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
loc = list()

def find(x, y):
  stack = []
  stack.append([x, y])

  while len(stack) > 0:
    tmp = stack.pop()
    n0 = tmp[0]
    n1 = tmp[1]
    loc[n0][n1] = 0

    for i in range(4):
      x_ = n0 + dx[i]
      y_ = n1 + dy[i]

      if x_ >= 0 and x_ < n and y_ >= 0 and y_ < m:
        if loc[x_][y_] == 1:
          stack.append([x_, y_])

def sol(n, m):
  cnt = 0

  for i in range(n):
    for j in range(m):
      if loc[i][j] == 1:
        cnt += 1
        find(i, j)

  return cnt


for _ in range(T):
  m, n, k = map(int, input().split())
  loc = [[0]*m for _ in range(n)]

  for i in range(k):
    x, y = map(int, input().split())
    loc[y][x] = 1

  print(sol(n, m))
