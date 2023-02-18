p1 = "AAAA"
p2 = "BB"
board = input()
result = []
cnt = 0
fail = 0

def change(cnt):
    a = cnt // 4
    b = (cnt % 4) // 2
    
    if (cnt % 4) % 2 > 0:
        return 1
    else:
        result.append(p1*a)
        result.append(p2*b)
        return 0

for x in board:
    if x == '.':
        fail = change(cnt)
        if fail: 
            break
        result.append(x)
        cnt = 0
        continue
    cnt += 1
fail = change(cnt)

if fail:
    print("-1")
else:
    print(''.join(result))