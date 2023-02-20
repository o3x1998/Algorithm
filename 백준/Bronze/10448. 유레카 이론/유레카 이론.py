T = int(input())
arr = [int(input()) for _ in range(T)]

def sol(num):
  tn = []
  for i in range(1, num):
    tmp = (i*(i+1))//2
    if tmp > num:
        break
    tn.append(tmp)

  for x in range(len(tn)):
    for y in range(len(tn)):
      for z in range(len(tn)):
        if (tn[x] + tn[y] + tn[z]) == num:
          print("1")
          return
  print("0")
        
for k in arr:
  sol(k)