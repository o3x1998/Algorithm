#5원, 2원으로 거슬러주는데 최소 갯수로
import sys

n = int(input())
rslt = 0
fail = True

i = n // 5 #5원으로 최대 몇개까지 가능한지
min_ = sys.maxsize + 1

for idx in range(0, i+1):
    tmp1 = n - (5 * idx)
    tmp2 = tmp1 // 2
    
    if (tmp1 % 2) == 0:
        fail = False
        cnt = idx + tmp2
        min_ = min(min_, cnt)

if fail:
    print('-1')
else: 
    print(min_)