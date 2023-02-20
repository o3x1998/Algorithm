n = int(input())
rslt = 0

def sol(m):
  arr = list(map(int, str(m)))
  tmp = m + sum(arr)

  if tmp == n:
    return True
  else:
    return False

for x in range(n, 0, -1):
  success = sol(x)

  if success:
    rslt = x

print(rslt)