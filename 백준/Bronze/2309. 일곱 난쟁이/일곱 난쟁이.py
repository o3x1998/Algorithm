h = [int(input()) for _ in range(9)]
finish = False

#9명중 빠질 2명 고르기
for i in range(0, 8):
  for j in range(i+1, 9):
    tmp = h.copy()
    tmp[i] = 0
    tmp[j] = 0
    if sum(tmp) == 100:
      tmp.sort()
      for x in tmp:
        if x != 0:
          print(x)
      finish = True
      break
  if finish: break